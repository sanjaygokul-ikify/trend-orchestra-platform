from dataclasses import dataclass
from enum import Enum
from typing import Dict

@dataclass
class Agent:
    id: str
    name: str

@dataclass
class Message:
    agent_id: str
    message_type: "MessageType"
    payload: str

class MessageType(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"