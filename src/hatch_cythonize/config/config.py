import os
from collections.abc import Generator
from dataclasses import asdict, dataclass, field
from importlib import import_module
from os import path
from typing import Optional

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

from hatch_cythonize.config.autoimport import Autoimport
from hatch_cythonize.config.defaults import brew_path, get_default_compile, get_default_link
from hatch_cythonize.config.files import FileArgs
from hatch_cythonize.config.flags import EnvFlags, parse_env_args
from hatch_cythonize.config.includes import parse_includes
from hatch_cythonize.config.macros import DefineMacros, parse_macros
from hatch_cythonize.config.platform import ListedArgs, PlatformArgs, parse_platform_args
from hatch_cythonize.config.templates import Templates, parse_template_kwds
from hatch_cythonize.constants import DIRECTIVES, EXIST_TRIM, INCLUDE, LTPY311, MUST_UNIQUE
from hatch_cythonize.types import CallableT, ListStr

# fields tracked by this plugin
__known__ = frozenset(
    (
        "src",
        "env",
        "files",
        "includes",
        "libraries",
        "templates",
        "compile_py",
        "directives",
        "library_dirs",
        "compile_args",
        "define_macros",
        "compiled_sdist",
        "extra_link_args",
        "cythonize_kwargs",
    )
)


def parse_from_dict(cls: BuildHookInterface):
    given = cls.config.get("options", {})

    passed = given.copy()
    kwargs = {}
    for key, val in given.items():
        if key in __known__:
            parsed: any
            if key == "files":
                val: dict
                parsed: FileArgs = FileArgs(**val)
            elif key == "define_macros":
                val: list
                parsed: DefineMacros = parse_macros(val)
            elif key == "templates":
                val: dict
                parsed: Templates = parse_template_kwds(val)
            else:
                val: any
                parsed: any = val
            kwargs[key] = parsed
            passed.pop(key)
            continue

    compile_args = parse_platform_args(kwargs, "compile_args", get_default_compile)
    link_args = parse_platform_args(kwargs, "extra_link_args", get_default_link)
    envflags = parse_env_args(kwargs)
    cfg = Config(**kwargs, compile_args=compile_args, extra_link_args=link_args, envflags=envflags)

    for maybe_dep, spec in passed.copy().items():
        is_include = maybe_dep.startswith(INCLUDE)
        if is_include and spec:
            cfg.resolve_pkg(
                cls,
                parse_includes(maybe_dep, spec),
            )
            passed.pop(maybe_dep)
            continue
        elif is_include:
            passed.pop(maybe_dep)
            continue
        elif maybe_dep == "parallel" and passed.get(maybe_dep):
            comp = [
                PlatformArgs(arg="/openmp", platforms="windows"),
                PlatformArgs(arg="-fopenmp", platforms=["linux"]),
            ]
            link = [
                PlatformArgs(arg="/openmp", platforms="windows"),
                PlatformArgs(arg="-fopenmp", platforms="linux"),
                PlatformArgs(
                    arg="-lomp", platforms="darwin", arch=["x86_64"], marker=LTPY311, apply_to_marker=running_in_ci
                ),
            ]

            brew = brew_path()
            if brew:
                comp.extend(
                    [
                        PlatformArgs(
                            arg=f"-I{brew}/opt/llvm/include",
                            platforms=["darwin"],
                            depends_path=True,
                        ),
                        PlatformArgs(
                            arg=f"-I{brew}/opt/libomp/include",
                            platforms=["darwin"],
                            depends_path=True,
                        ),
                    ]
                )
                link.extend(
                    [
                        PlatformArgs(
                            arg=f"-L{brew}/opt/llvm/lib/c++ -Wl,-rpath,{brew}/llvm/lib/c++",
                            platforms=["darwin"],
                            depends_path=True,
                        ),
                        PlatformArgs(
                            arg=f"-L{brew}/opt/libomp/lib -Wl,-rpath,{brew}/opt/libomp/lib",
                            platforms=["darwin"],
                            depends_path=True,
                        ),
                    ]
                )

            cma = ({*cfg.compile_args}).union({*comp})
            cfg.compile_args = list(cma)
            seb = ({*cfg.extra_link_args}).union({*link})
            cfg.extra_link_args = list(seb)
            passed.pop(maybe_dep)

    cfg.compile_kwargs = passed
    return cfg


@dataclass
class Config:
    src: Optional[str] = field(default=None)  # noqa: UP007
    files: FileArgs = field(default_factory=FileArgs)
    includes: ListStr = field(default_factory=list)
    define_macros: DefineMacros = field(default_factory=list)
    libraries: ListStr = field(default_factory=list)
    library_dirs: ListStr = field(default_factory=list)
    directives: dict = field(default_factory=lambda: DIRECTIVES)
    compile_args: ListedArgs = field(default_factory=get_default_compile)
    compile_kwargs: dict = field(default_factory=dict)
    cythonize_kwargs: dict = field(default_factory=dict)
    extra_link_args: ListedArgs = field(default_factory=get_default_link)
    compiled_sdist: bool = field(default=False)
    envflags: EnvFlags = field(default_factory=EnvFlags)
    compile_py: bool = field(default=True)
    templates: Templates = field(default_factory=Templates)

    def __post_init__(self):
        self.directives = {**DIRECTIVES, **self.directives}

    @property
    def compile_args_for_platform(self):
        return self._arg_impl(self.compile_args)

    @property
    def compile_links_for_platform(self):
        return self._arg_impl(self.extra_link_args)

    def _post_import_attr(
        self,
        cls: BuildHookInterface,
        im: Autoimport,
        att: str,
        mod: any,
        extend: CallableT[[ListStr], None],
        append: CallableT[[str], None],
    ):
        attr = getattr(im, att)
        if attr is not None:
            try:
                libraries = getattr(mod, attr)
                if callable(libraries):
                    libraries = libraries()

                if isinstance(libraries, str):
                    append(libraries)
                elif isinstance(libraries, (list, Generator)):  # noqa: UP038
                    extend(libraries)
                elif isinstance(libraries, dict):
                    extend(libraries.values())
                else:
                    cls.app.display_warning(f"{im.pkg}.{attr} has an invalid type ({type(libraries)})")

            except AttributeError:
                cls.app.display_warning(f"{im.pkg}.{attr}")

    def resolve_pkg(
        self,
        cls: BuildHookInterface,
        im: Autoimport,
    ):
        mod = import_module(im.pkg)
        self._post_import_attr(
            cls,
            im,
            "include",
            mod,
            self.includes.extend,
            self.includes.append,
        )
        self._post_import_attr(
            cls,
            im,
            "libraries",
            mod,
            self.libraries.extend,
            self.libraries.append,
        )
        self._post_import_attr(
            cls,
            im,
            "library_dirs",
            mod,
            self.library_dirs.extend,
            self.library_dirs.append,
        )
        if im.required_call is not None:
            if hasattr(mod, im.required_call):
                call = getattr(mod, im.required_call)
                call()
            else:
                cls.app.display_warning(f"{im.pkg}.{im.required_call} is invalid")

    def _arg_impl(self, target: ListedArgs):
        args = {"any": []}

        def with_argvalue(arg: str):
            # be careful with e.g. -Ox flags
            matched = list(filter(lambda s: arg.startswith(s), MUST_UNIQUE))
            if matched:
                m = matched[0]
                args[m] = arg.split(" ")
            else:
                args["any"].append(arg.split(" "))

        for arg in target:
            # if compile-arg format, check platform applies
            if isinstance(arg, PlatformArgs):
                if arg.applies() and arg.is_exist(EXIST_TRIM):
                    with_argvalue(arg.arg)
            # else assume string / user knows what theyre doing and add to the call params
            else:
                with_argvalue(arg)

        flat = []

        def flush(it):
            if isinstance(it, list):
                for v in it:
                    flush(v)
            else:
                flat.append(it)

        # side effect
        list(map(flush, args.values()))
        return list({*flat})

    def asdict(self):
        d = asdict(self)
        d["envflags"]["env"] = self.envflags.masked_environ()
        d["templates"] = self.templates.asdict()
        return d

    def validate_include_opts(self):
        for opt in self.includes:
            if not path.exists(opt):
                msg = f"{opt} does not exist"
                raise ValueError(msg)


def running_in_ci() -> bool:
    return any(os.environ.get(env_var) in {"true", "1"} for env_var in ("CI", "GITHUB_ACTIONS"))
