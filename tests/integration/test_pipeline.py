import unittest
from ..services import orchestrator
from ..core import Engine, Agent, Message

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        agents = {"agent1": Agent("agent1", "agent1")}
        engine = Engine(agents)
        orchestrator = orchestrator.Orchestrator(engine)
        # Set up the pipeline and assert its behavior
