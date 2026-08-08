from typing import Dict, List
from .types import Agent, Message
from .exceptions import InvalidMessageError, AgentNotFoundError
import logging

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, agents: Dict[str, Agent]):
        self.agents = agents

    def process_message(self, message: Message) -> None:
        try:
            agent_id = message.agent_id
            agent = self.agents.get(agent_id)
            if agent is None:
                raise AgentNotFoundError(f"Agent {agent_id} not found")
            agent.process_message(message)
        except InvalidMessageError as e:
            logger.error(f"Invalid message: {e}")
            # Send error message to sender
            sender_agent_id = message.sender_agent_id
            error_message = Message(
                agent_id=sender_agent_id,
                message_type=MessageType.ERROR,
                payload=str(e)
            )
            self.process_message(error_message)
        except AgentNotFoundError as e:
            logger.error(f"Agent not found: {e}")
            # Send error message to sender
            sender_agent_id = message.sender_agent_id
            error_message = Message(
                agent_id=sender_agent_id,
                message_type=MessageType.ERROR,
                payload=str(e)
            )
            self.process_message(error_message)

    def run(self) -> None:
        while True:
            # Get message from queue
            message_queue = self.get_message_queue()
            if message_queue:
                message = message_queue[0]
                self.process_message(message)
                # Remove message from queue
                self.get_message_queue().remove(message)

    def get_message_queue(self) -> List[Message]:
        # Simulate message queue for demonstration purposes
        return [Message(agent_id="agent1", message_type=MessageType.INFO, payload="Hello, world!")]