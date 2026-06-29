import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agent import add_numbers, is_leap_year, root_agent


def test_agent_exists():
    assert root_agent is not None


def test_add_numbers_tool():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_is_leap_year_tool():
    assert is_leap_year(2024) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True