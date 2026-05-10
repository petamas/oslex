import shlex
import sys

import mslex
import pytest

import oslex

# These tests are simply testing that keyword arguments exist both in oslex and in mslex/shlex.
# In many cases, the keyword arguments do not change the result of the quote() function for the specific arg.


def test_quote_ms() -> None:
    arg = 'foo bar'

    assert oslex.quote_ms(arg) == mslex.quote(arg)
    assert oslex.quote_ms(arg, ms_for_cmd=False) == mslex.quote(arg, for_cmd=False)
    assert oslex.quote_ms(arg, ms_for_cmd=True) == mslex.quote(arg, for_cmd=True)


def test_quote_sh() -> None:
    arg = 'foo bar'

    assert oslex.quote_sh(arg) == shlex.quote(arg)
    assert oslex.quote_sh(arg, ms_for_cmd=False) == shlex.quote(arg)
    assert oslex.quote_sh(arg, ms_for_cmd=True) == shlex.quote(arg)


@pytest.mark.skipif(sys.platform != 'win32', reason='Testing Windows-specific functionality')
def test_quote_win() -> None:
    arg = 'foo bar'

    assert oslex.quote(arg) == mslex.quote(arg)
    assert oslex.quote(arg, ms_for_cmd=False) == mslex.quote(arg, for_cmd=False)
    assert oslex.quote(arg, ms_for_cmd=True) == mslex.quote(arg, for_cmd=True)


@pytest.mark.skipif(sys.platform == 'win32', reason='Testing non-Windows-specific functionality')
def test_quote_posix() -> None:
    arg = 'foo bar'

    assert oslex.quote(arg) == shlex.quote(arg)
    assert oslex.quote(arg, ms_for_cmd=False) == shlex.quote(arg)
    assert oslex.quote(arg, ms_for_cmd=True) == shlex.quote(arg)
