import time
import random
from datetime import datetime
from .message import Message


class MessageSource:
    def __init__(self, manager):
        self.manager = manager

    def start(self, count=20):
        for i in range(count):
            msg = Message(
                payload=f"message-{i}",
                timestamp=datetime.utcnow()
            )
            self.manager.on_message(msg)

            # Poisson ~10 messages per minute
            time.sleep(random.expovariate(1 / 6))
