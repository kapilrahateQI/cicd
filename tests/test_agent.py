import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agent import root_agent


def test_agent_exists():
    assert root_agent is not None