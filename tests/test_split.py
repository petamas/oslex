import shlex
import sys

import mslex
import pytest

import oslex

# These tests are simply testing that keyword arguments exist both in oslex and in mslex/shlex.
# In many cases, the keyword arguments do not change the result of the split() function for the specific command_str.


def test_split_ms() -> None:
    command_str = "a 'b^ c'"

    assert oslex.split_ms(command_str) == mslex.split(command_str)
    assert oslex.split_ms(command_str, ms_like_cmd=False) == mslex.split(command_str, like_cmd=False)
    assert oslex.split_ms(command_str, ms_like_cmd=True) == mslex.split(command_str, like_cmd=True)
    assert oslex.split_ms(command_str, ms_check=False) == mslex.split(command_str, check=False)
    assert oslex.split_ms(command_str, ms_check=True) == mslex.split(command_str, check=True)
    assert oslex.split_ms(command_str, ms_ucrt=None) == mslex.split(command_str, ucrt=None)
    assert oslex.split_ms(command_str, ms_ucrt=False) == mslex.split(command_str, ucrt=False)
    assert oslex.split_ms(command_str, ms_ucrt=True) == mslex.split(command_str, ucrt=True)


def test_split_sh() -> None:
    command_str = "a 'b^ c'"

    assert oslex.split_sh(command_str) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_like_cmd=False) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_like_cmd=True) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_check=False) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_check=True) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_ucrt=None) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_ucrt=False) == shlex.split(command_str)
    assert oslex.split_sh(command_str, ms_ucrt=True) == shlex.split(command_str)


@pytest.mark.skipif(sys.platform != 'win32', reason='Testing Windows-specific functionality')
def test_split_win() -> None:
    command_str = "a 'b^ c'"

    assert oslex.split(command_str) == mslex.split(command_str)
    assert oslex.split(command_str, ms_like_cmd=False) == mslex.split(command_str, like_cmd=False)
    assert oslex.split(command_str, ms_like_cmd=True) == mslex.split(command_str, like_cmd=True)
    assert oslex.split(command_str, ms_check=False) == mslex.split(command_str, check=False)
    assert oslex.split(command_str, ms_check=True) == mslex.split(command_str, check=True)
    assert oslex.split(command_str, ms_ucrt=None) == mslex.split(command_str, ucrt=None)
    assert oslex.split(command_str, ms_ucrt=False) == mslex.split(command_str, ucrt=False)
    assert oslex.split(command_str, ms_ucrt=True) == mslex.split(command_str, ucrt=True)


@pytest.mark.skipif(sys.platform == 'win32', reason='Testing non-Windows-specific functionality')
def test_split_posix() -> None:
    command_str = "a 'b^ c'"

    assert oslex.split(command_str) == shlex.split(command_str)
    assert oslex.split(command_str, ms_like_cmd=False) == shlex.split(command_str)
    assert oslex.split(command_str, ms_like_cmd=True) == shlex.split(command_str)
    assert oslex.split(command_str, ms_check=False) == shlex.split(command_str)
    assert oslex.split(command_str, ms_check=True) == shlex.split(command_str)
    assert oslex.split(command_str, ms_ucrt=None) == shlex.split(command_str)
    assert oslex.split(command_str, ms_ucrt=False) == shlex.split(command_str)
    assert oslex.split(command_str, ms_ucrt=True) == shlex.split(command_str)
