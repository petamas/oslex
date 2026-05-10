from __future__ import annotations

import shlex
import sys
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Protocol

import mslex


class _QuoteProtocol(Protocol):
    def __call__(
        self,
        arg: str | Path,
        /,
        *,
        ms_for_cmd: bool = True,
    ) -> str: ...


def quote_ms(
    arg: str | Path,
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Same as `oslex.quote()`, except it always calls `mslex.quote()`.
    """
    return mslex.quote(
        str(arg),
        for_cmd=ms_for_cmd,
    )


def quote_sh(
    arg: str | Path,
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Same as `oslex.quote()`, except it always calls `shlex.quote()`.
    """
    del ms_for_cmd
    return shlex.quote(
        str(arg),
    )


if TYPE_CHECKING:
    _quote_ms: _QuoteProtocol = quote_ms
    _quote_sh: _QuoteProtocol = quote_sh

_quote_os: _QuoteProtocol = quote_ms if sys.platform == 'win32' else quote_sh


def quote(
    arg: str | Path,
    /,
    *,
    ms_for_cmd: bool = True,
) -> str:
    """
    Quote argument according to platform-specific rules.
    Calls `mslex.quote()` on Windows, and `shlex.quote()` on other platforms.
    Arguments:
    * arg: str | Path - Argument to quote.
    * ms_for_cmd: bool - Passed to `mslex.quote()` as `for_cmd` argument on Windows. Ignored on non-Windows platforms.
    """
    return _quote_os(
        arg,
        ms_for_cmd=ms_for_cmd,
    )
