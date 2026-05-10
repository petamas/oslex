import shlex
import sys

import mslex
import pytest

import oslex

# These tests are simply testing that keyword arguments exist both in oslex and in mslex/shlex.
# In many cases, the keyword arguments do not change the result of the join() function for the specific command.


def test_join_ms() -> None:
    command = ['a', 'b c', 'd']

    assert oslex.join_ms(command) == mslex.join(command)
    assert oslex.join_ms(command, ms_for_cmd=False) == mslex.join(command, for_cmd=False)
    assert oslex.join_ms(command, ms_for_cmd=True) == mslex.join(command, for_cmd=True)


def test_join_sh() -> None:
    command = ['a', 'b c', 'd']

    assert oslex.join_sh(command) == shlex.join(command)
    assert oslex.join_sh(command, ms_for_cmd=False) == shlex.join(command)
    assert oslex.join_sh(command, ms_for_cmd=True) == shlex.join(command)


@pytest.mark.skipif(sys.platform != 'win32', reason='Testing Windows-specific functionality')
def test_join_win() -> None:
    command = ['a', 'b c', 'd']

    assert oslex.join(command) == mslex.join(command)
    assert oslex.join(command, ms_for_cmd=False) == mslex.join(command, for_cmd=False)
    assert oslex.join(command, ms_for_cmd=True) == mslex.join(command, for_cmd=True)


@pytest.mark.skipif(sys.platform == 'win32', reason='Testing non-Windows-specific functionality')
def test_join_posix() -> None:
    command = ['a', 'b c', 'd']

    assert oslex.join(command) == shlex.join(command)
    assert oslex.join(command, ms_for_cmd=False) == shlex.join(command)
    assert oslex.join(command, ms_for_cmd=True) == shlex.join(command)
