from __future__ import annotations

import shlex
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Protocol

import mslex


class _JoinProtocol(Protocol):
    def __call__(
        self,
        command: Sequence[str | Path],
        /,
        *,
        ms_for_cmd: bool = True,
    ) -> str: ...


def join_ms(
    command: Sequence[str | Path],
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Same as `oslex.join()`, except it always calls `mslex.join()`.
    """
    return mslex.join(
        [str(arg) for arg in command],
        for_cmd=ms_for_cmd,
    )


def join_sh(
    command: Sequence[str | Path],
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Same as `oslex.join()`, except it always calls `shlex.join()`.
    """
    del ms_for_cmd
    return shlex.join(
        [str(arg) for arg in command],
    )


if TYPE_CHECKING:
    _join_ms: _JoinProtocol = join_ms
    _join_sh: _JoinProtocol = join_sh

_join_os: _JoinProtocol = join_ms if sys.platform == 'win32' else join_sh


def join(
    command: Sequence[str | Path],
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Quote arguments according to platform-specific rules, then join them to form a full command line.
    Calls `mslex.join()` on Windows, and `shlex.join()` on other platforms.
    Arguments:
    * command: Sequence[str | Path] - Argument to quote.
    * ms_for_cmd: bool - Passed to `mslex.join()` as `for_cmd` argument on Windows. Ignored on non-Windows platforms.
    """
    return _join_os(
        command,
        ms_for_cmd=ms_for_cmd,
    )
