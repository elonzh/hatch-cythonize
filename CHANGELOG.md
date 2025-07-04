# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0] - 2025-05-26

### Features

- Support for python 3.7

## [0.6.0] - 2025-04-27

### Bug Fixes

- UnicodeDecodeError on non-utf locales
- Module name shoule be normalized as default dir_name joshua-auchincloss/hatch-cython#59
- Remove hatch from deps to speedup building joshua-auchincloss/hatch-cython#61
- Ruff and build actions

### Misc

- Add .idea files
- Rename it to hatch-cythonize
- Bump 0.6.0

## [0.6.0rc0] - 2024-04-28

### Bug Fixes

- Arch
- Ci ([#52](https://github.com/elonzh/hatch-cythonize/issues/52))

### Features

- V0.6.0rc0 (#46, #47, #50)

## [0.5.1] - 2024-02-19

### Bug Fixes

- Build permissions ([#28](https://github.com/elonzh/hatch-cythonize/issues/28))
- Ci
- No auto changelog
- Release ci [ci skip] ([#40](https://github.com/elonzh/hatch-cythonize/issues/40))
- Ci
- Release

### Features

- Gh releases

### Miscellaneous Tasks

- V0.5.1 ([#33](https://github.com/elonzh/hatch-cythonize/issues/33))
- Changelog
- #34 - ci
- Pr #35 - ci
- Add 3.12 for validation [ci skip]
- Pr #36 - ci
- Doc [ci skip]
- Changelog
- Pr #38 from dev
- Tighten ci ([#39](https://github.com/elonzh/hatch-cythonize/issues/39))
- Changelog
- V0.5.1

### Merge

- #29 from build
- Pr #37 from dev

### Release

- V0.5.1
- V0.5.1

## [0.5.0] - 2023-11-30

### Bug Fixes

- Depreciate `retain_intermediate_artifacts`
- Macos linkage
- Coverage
- Brew links
- Brew commands
- Random mac errs
- Random brew errs
- Build script, format

### Miscellaneous Tasks

- Changelog

### Testing

- Different lib structures
- Skip brew
- Tests

### Merge

- #26/v0.5.0

## [0.4.0] - 2023-09-14

### Bug Fixes

- Tests
- Tests
- Version [ci skip]
- Trigger build

### Miscellaneous Tasks

- Readme [ci skip]
- Lint [ci skip]
- Readme [ci skip]
- Pr #23 from joshua-auchincloss/v0.4.0-patch

### Refactor

- Plugin [ci skip]

### Testing

- Sdist [ci skip]
- Sdist pre-ext
- Platform specific files

### Merge

- Pr #22 from joshua-auchincloss/v0.4.0
- Pr #24 from joshua-auchincloss/v0.4.0-patch

## [0.3.0] - 2023-09-01

### Miscellaneous Tasks

- Readme [ci skip]

### Testing

- Template keywords

### Merge

- Pr #19 from joshua-auchincloss/v0.3.0

## [0.2.6] - 2023-08-31

### Bug Fixes

- Tests

### Features

- Add pythran support [ci skip]

### Miscellaneous Tasks

- Readme [ci skip]
- Version [ci skip]

### Testing

- Templated files

### Merge

- Pr #18 from joshua-auchincloss/v0.2.6

## [0.2.5] - 2023-08-30

### Miscellaneous Tasks

- Readme

### Testing

- Add macro support

### Merge

- Pr #16 from joshua-auchincloss/v0.2.5
- Pr #17 from joshua-auchincloss/v0.2.5

## [0.2.4] - 2023-08-29

### Miscellaneous Tasks

- Readme [ci skip]

### Refactor

- Memoize properties
- Config

### Testing

- Add `compile_py` option
- Module aliasing

### Merge

- Pr #15 from joshua-auchincloss/v0.2.4

## [0.2.3] - 2023-08-28

### Features

- Add exclude dir support

### Miscellaneous Tasks

- Readme [ci skip]

### Merge

- Pr #14 from joshua-auchincloss/v0.2.3

## [0.2.2] - 2023-08-28

### Bug Fixes

- Dict types
- Sorting error
- Sorting in tests

### Miscellaneous Tasks

- Readme [ci skip]
- Pr #12 from joshua-auchincloss/v0.2.1-post [ci skip]

### Testing

- Fix `Callable` in py38

### Merge

- Pr #13 from joshua-auchincloss/v0.2.2

## [0.2.1] - 2023-08-28

### Bug Fixes

- Add numpy to test deps
- Debug statements

### Testing

- Fix & integration tests
- Fix dir in tests
- Fix env vars

### Merge

- Pr #11 from joshua-auchincloss/v0.2.0-post

## [0.2.0] - 2023-08-27

### Bug Fixes

- Add dep on mac
- Debug
- No xcode install
- Build
- Deps
- Deps
- Add `CXX` variable
- Split args
- Coverage
- Coverage
- Revert runner
- `3.9` type compat
- Windows tests
- Build [ci skip]
- Prompt build

### Miscellaneous Tasks

- Pr #9 from joshua-auchincloss/v0.2.0-patch [ci skip]

### Refactor

- Devel [ci skip]

### Testing

- Architecture conditions
- Autoinclude
- Debug build
- Fix paths
- Add link guard
- Fix llvm links
- Explicit link & arch
- Use `c++` instead of `g+`
- Explicit arch
- Arch
- Fix args
- Fix cc
- Fix
- `g++`
- Build verbose
- Explicit runner arch
- Platform env vars
- Add marker integration
- Fix darwin ci bug

### Merge

- Pr #8 from joshua-auchincloss/v0.2.0
- Pr #10 from joshua-auchincloss/v0.2.0-patch

## [0.1.9] - 2023-08-26

### Bug Fixes

- Use `llvmlite`

### Miscellaneous Tasks

- Document & version [ci skip]

### Testing

- `os.name` -> `platform.platform()`
- Llvm

### Merge

- Pr #6 from joshua-auchincloss/v0.1.9
- Pr #7 from joshua-auchincloss/v0.1.9-patch

## [0.1.8] - 2023-08-25

### Features

- Support `.pxd`
- Add `openmp` support

### Miscellaneous Tasks

- Documentation [ci skip]
- Readme [ci skip]
- Version

### Merge

- Pr #5 from joshua-auchincloss/v0.1.8

## [0.1.7] - 2023-08-25

### Bug Fixes

- `_post_import_attr`
- Err format strs [ci skip]

### Merge

- Pr #4 from joshua-auchincloss/v0.1.7

## [0.1.6] - 2023-08-25

### Bug Fixes

- Add to `__known__`

### Testing

- Add 3.8, 3.9 support
- Add library aliasing

### Merge

- Pr #3 from joshua-auchincloss/v0.1.6

## [0.1.5] - 2023-08-25

### Testing

- Fix nested modules

### Merge

- Pr #2 from joshua-auchincloss/v0.1.5

## [0.1.4] - 2023-08-25

### Bug Fixes

- Config kwargs

## [0.1.3] - 2023-08-25

### Bug Fixes

- Test branches
- Test
- Tests
- No nil values

### Features

- Add std config

### Refactor

- Pyi & release [ci skip]

### Testing

- Fix nt & linux

### Merge

- Pr #1 from joshua-auchincloss/v0.1.3

## [0.1.2] - 2023-08-25

### Miscellaneous Tasks

- Readme [ci skip]

### Refactor

- Remove`__main__`

## [0.1.1] - 2023-08-25

### Bug Fixes

- Lint

### Features

- Includes & numpy support

## [0.1.0-patch] - 2023-08-25

### Bug Fixes

- Version & hooks

## [0.1.0-release] - 2023-08-24

### Bug Fixes

- Tests
- Nt file paths
- Normalized included files
- Dll
- Debug verbose
- Add .pyd
- Release

### Features

- Full cross-platform

### Testing

- Cross-platform
- Non norm
- Nt build
- Nt
- Nt build
- Debug

<!-- generated by git-cliff -->
