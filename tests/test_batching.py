from datetime import datetime
from src.messaging.batch_manager import MiniBatchManager
from src.messaging.message import Message
from src.workers.worker_pool import WorkerPool
import time


def test_batch_is_closed():
    pool = WorkerPool()
    manager = MiniBatchManager(1, pool)

    manager.on_message(Message("a", datetime.utcnow()))
    time.sleep(1.5)

    assert manager.current_batch is None
    pool.shutdown()
