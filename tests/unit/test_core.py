import unittest
from ..core import Agent, Message, Engine, MessageType

class TestCore(unittest.TestCase):
    def test_agent_create(self):
        agent = Agent("agent1", "agent1")
        self.assertEqual(agent.id, "agent1")
        self.assertEqual(agent.name, "agent1")

    def test_message_create(self):
        message = Message("agent1", MessageType.INFO, "Hello, world!")
        self.assertEqual(message.agent_id, "agent1")
        self.assertEqual(message.message_type, MessageType.INFO)
        self.assertEqual(message.payload, "Hello, world!")

    def test_engine_create(self):
        agents = {"agent1": Agent("agent1", "agent1")}
        engine = Engine(agents)
        self.assertEqual(engine.agents, agents)
