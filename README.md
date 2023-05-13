# oslex

`oslex` is an OS-independent wrapper for [`shlex`](https://docs.python.org/3/library/shlex.html) and [`mslex`](https://pypi.org/project/mslex/).

Its main purpose is to provide functions similar in functionality to `shlex.quote()`, `shlex.split()` and `shlex.join()` on both Windows and POSIX-compatible platforms.

This goal is achieved by simply forwarding the calls to either `shlex` (from the standard library) on POSIX-compatible systems, or the excellent `mslex` library (written by Lawrence D'Anna / @smoofra) on Windows.

In other words, `oslex` is to `shlex`/`mslex` what `os-path` is to `posixpath`/`ntpath`.

## Licensing

This library itself is licensed under the MIT license.

`oslex` uses the [`mslex`](https://pypi.org/project/mslex/) library, which is distributed under the Apache 2.0 license.
