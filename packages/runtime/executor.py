from typing import Dict
from . import Executor
from packages.core.engine import Engine
from packages.core.types import Agent, Message
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, agents: Dict[str, Agent]):
        self.engine = Engine(agents)

    def run(self) -> None:
        self.engine.run()

    def process_message(self, message: Message) -> None:
        self.engine.process_message(message)