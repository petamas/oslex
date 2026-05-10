from __future__ import annotations

import shlex
import sys
from typing import TYPE_CHECKING
from typing import Protocol

import mslex


class _SplitProtocol(Protocol):
    def __call__(
        self,
        command_str: str,
        /,
        *,
        ms_like_cmd: bool = True,
        ms_check: bool = True,
        ms_ucrt: bool | None = None,
        sh_comments: bool = False,
        sh_posix: bool = True,
    ) -> list[str]: ...


def split_ms(
    command_str: str,
    /,
    *,
    ms_like_cmd: bool = True,
    ms_check: bool = True,
    ms_ucrt: bool | None = None,
    sh_comments: bool = False,
    sh_posix: bool = True,
) -> list[str]:
    """
    Same as `oslex.split()`, except it always calls `mslex.split()`.
    """
    del sh_comments
    del sh_posix
    return mslex.split(
        command_str,
        like_cmd=ms_like_cmd,
        check=ms_check,
        ucrt=ms_ucrt,
    )


def split_sh(
    command_str: str,
    /,
    *,
    ms_like_cmd: bool = True,
    ms_check: bool = True,
    ms_ucrt: bool | None = None,
    sh_comments: bool = False,
    sh_posix: bool = True,
) -> list[str]:
    """
    Same as `oslex.split()`, except it always calls `shlex.split()`.
    """
    del ms_like_cmd
    del ms_check
    del ms_ucrt
    return shlex.split(
        command_str,
        comments=sh_comments,
        posix=sh_posix,
    )


if TYPE_CHECKING:
    _split_ms: _SplitProtocol = split_ms
    _split_sh: _SplitProtocol = split_sh

_split_os: _SplitProtocol = split_ms if sys.platform == 'win32' else split_sh


def split(
    command_str: str,
    /,
    *,
    ms_like_cmd: bool = True,
    ms_check: bool = True,
    ms_ucrt: bool | None = None,
    sh_comments: bool = False,
    sh_posix: bool = True,
) -> list[str]:
    """
    Split command line into arguments according to platform-specific rules.
    Calls `mslex.split()` on Windows, and `shlex.split()` on other platforms.
    Arguments:
    * command_str: str - Command string to split.
    * ms_like_cmd: bool - Passed to `mslex.split()` as `like_cmd` argument on Windows. Ignored on non-Windows platforms.
    * ms_check: bool - Passed to `mslex.split()` as `check` argument on Windows. Ignored on non-Windows platforms.
    * ms_ucrt: bool | None - Passed to `mslex.split()` as `ucrt` argument on Windows. Ignored on non-Windows platforms.
    * sh_comments: bool - Passed to `shlex.split()` as `comments` argument on non-Windows platforms. Ignored on Windows.
    * sh_posix: bool - Passed to `shlex.split()` as `posix` argument on non-Windows platforms. Ignored on Windows.
    """
    return _split_os(
        command_str,
        sh_comments=sh_comments,
        sh_posix=sh_posix,
        ms_like_cmd=ms_like_cmd,
        ms_check=ms_check,
        ms_ucrt=ms_ucrt,
    )
