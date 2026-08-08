from ..core import Engine
from ..utils import logging
logger = logging.logger

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.run()