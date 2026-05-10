# oslex

`oslex` is an OS-independent wrapper for [`shlex`](https://docs.python.org/3/library/shlex.html) and [`mslex`](https://pypi.org/project/mslex/).

Its main purpose is to provide functions similar in functionality to `shlex.quote()`, `shlex.split()` and `shlex.join()` on both Windows and POSIX-compatible platforms.

This goal is achieved by simply forwarding the calls to either `shlex` (from the standard library) on POSIX-compatible systems, or the excellent `mslex` library (written by Lawrence D'Anna / @smoofra) on Windows.

In other words, `oslex` is to `shlex`/`mslex` what `os.path` is to `posixpath`/`ntpath`.

## Reference

The three main interface functions are `oslex.join()`, `oslex.quote()` and `oslex.split()`.

They all support taking a single positional argument, and a variety of optional keyword arguments. Keyword arguments starting with `ms_` are passed to the underlying `mslex` function on Windows, and are ignored on non-Windows platforms. Keyword arguments starting with `sh_` are passed to the underlying `shlex` function on non-Windows platforms, and are ignored on Windows. The default values of keyword arguments are the same as for the underlying libraries.

In addition, each function has two extra variants: one with the suffix `_sh`, and one with the suffix `_ms`. They have the exact same interface as the main variants, except they always call the `shlex` or `mslex` library functions instead of deciding based on platform. They can be useful in situations when a specific implementation is needed regardless of platform, but support for `Path` arguments is desirable.

### `oslex.join()`

Quote arguments according to platform-specific rules, then join them to form a full command line. Returns `str`.

Calls `mslex.join()` on Windows, and `shlex.join()` on non-Windows platforms.

Arguments:

|Name|Type|Default|Kind|Description|
|----|----|-------|----|-----------|
|`command`|`Sequence[str\|Path]`|required|positional-only|Argument list to quote. Supports mixing `str` and `Path` arguments.<br/>`Path`s are converted to `str` before passing to the underlying `join()` function.|
|`ms_for_cmd`|`bool`|`True`|keyword-only|Passed to `mslex.join()` as `for_cmd` argument on Windows.<br/>Ignored on non-Windows platforms.<br/>See [`mslex.join()`'s documentation](https://mslex.readthedocs.io/en/latest/usage.html#mslex.join) for more details.|

### `oslex.quote()`

Quote argument according to platform-specific rules. Returns `str`.

Calls `mslex.quote()` on Windows, and `shlex.quote()` on non-Windows platforms.

Arguments:

|Name|Type|Default|Kind|Description|
|----|----|-------|----|-----------|
|`arg`|`str\|Path`|required|positional-only|Argument to quote.<br/>`Path`s are converted to `str` before passing to the underlying `quote()` function.|
|`ms_for_cmd`|`bool`|`True`|keyword-only|Passed to `mslex.quote()` as `for_cmd` argument on Windows.<br/>Ignored on non-Windows platforms.<br/>See [`mslex.quote()`'s documentation](https://mslex.readthedocs.io/en/latest/usage.html#mslex.quote) for more details.|

### `oslex.split()`

Split command line into arguments according to platform-specific rules. Returns `list[str]`.

Calls `mslex.split()` on Windows, and `shlex.split()` on non-Windows platforms.

Arguments:

|Name|Type|Default|Kind|Description|
|----|----|-------|----|-----------|
|`command_str`|`str`|required|positional-only|Command string to split.|
|`ms_like_cmd`|`bool`|`True`|keyword-only|Passed to `mslex.split()` as `like_cmd` argument on Windows.<br/>Ignored on non-Windows platforms.<br/>See [`mslex.split()`'s documentation](https://mslex.readthedocs.io/en/latest/usage.html#mslex.split) for more details.|
|`ms_check`|`bool`|`True`|keyword-only|Passed to `mslex.split()` as `check` argument on Windows.<br/>Ignored on non-Windows platforms.<br/>See [`mslex.split()`'s documentation](https://mslex.readthedocs.io/en/latest/usage.html#mslex.split) for more details.|
|`ms_ucrt`|`bool \| None`|`None`|keyword-only|Passed to `mslex.split()` as `ucrt` argument on Windows.<br/>Ignored on non-Windows platforms.<br/>See [`mslex.split()`'s documentation](https://mslex.readthedocs.io/en/latest/usage.html#mslex.split) for more details.|
|`sh_comments`|`bool`|`False`|keyword-only|Passed to `shlex.split()` as `comments` argument on non-Windows platforms.<br/>Ignored on Windows.<br/>See [`shlex.split()`'s documentation](https://docs.python.org/3/library/shlex.html#shlex.split) for more details.|
|`sh_posix`|`bool`|`True`|keyword-only|Passed to `shlex.split()` as `posix` argument on non-Windows platforms.<br/>Ignored on Windows.<br/>Ignored on Windows.<br/>See [`shlex.split()`'s documentation](https://docs.python.org/3/library/shlex.html#shlex.split) for more details.|

### `oslex.join_ms()`, `oslex.quote_ms()`, `oslex.split_ms()`

Same as `oslex.join()`, `oslex.quote()` and `oslex.split()`, except they always call `mslex` regardless of platform.

See documentation of arguments at the respective function. (Keyword arguments starting with `sh_` are always ignored.)

### `oslex.join_sh()`, `oslex.quote_sh()`, `oslex.split_sh()`

Same as `oslex.join()`, `oslex.quote()` and `oslex.split()`, except they always call `shlex` regardless of platform.

See documentation of arguments at the respective function. (Keyword arguments starting with `ms_` are always ignored.)

## Licensing

This library itself is licensed under the MIT license.

`oslex` uses the [`mslex`](https://pypi.org/project/mslex/) library, which is distributed under the Apache 2.0 license.
