import threading
from .batch import MiniBatch


class MiniBatchManager:
    def __init__(self, batch_duration_seconds, worker_pool):
        self.batch_duration = batch_duration_seconds
        self.worker_pool = worker_pool

        self.lock = threading.Lock()
        self.current_batch = None
        self.timer = None

    def on_message(self, message):
        with self.lock:
            if self.current_batch is None:
                self._start_new_batch(message.timestamp)

            self.current_batch.add(message)

    def _start_new_batch(self, start_time):
        self.current_batch = MiniBatch(start_time)
        self.timer = threading.Timer(
            self.batch_duration,
            self._close_batch
        )
        self.timer.start()

    def _close_batch(self):
        with self.lock:
            batch = self.current_batch
            self.current_batch = None

        if batch:
            self.worker_pool.submit(batch)
