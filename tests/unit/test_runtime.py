import unittest
from ..core import Engine

class TestRuntime(unittest.TestCase):
    def test_engine_run(self):
        agents = {"agent1": Agent("agent1", "agent1")}
        engine = Engine(agents)
        # Run the engine and assert its behavior
