import time
from concurrent.futures import ThreadPoolExecutor


class WorkerPool:
    def __init__(self, workers=10):
        self.executor = ThreadPoolExecutor(max_workers=workers)

    def submit(self, item):
        self.executor.submit(self.process, item)

    def process(self, item):
        # Simulacija obrade
        time.sleep(0.2)

    def shutdown(self):
        self.executor.shutdown(wait=True)
