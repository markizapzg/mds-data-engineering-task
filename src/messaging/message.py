from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    payload: str
    timestamp: datetime
