import random
from .file import File


class FileProcessor:
    def __init__(self, strategy, worker_pool):
        self.strategy = strategy
        self.worker_pool = worker_pool

    def process_nightly_files(self, count=100):
        files = self._generate_files(count)
        buckets = self.strategy.create_buckets(files)

        for bucket in buckets:
            self.worker_pool.submit(bucket)

    def _generate_files(self, count):
        files = []
        for i in range(count):
            size = int(random.expovariate(1 / 2_000_000))
            files.append(File(name=f"file_{i}", size=size))
        return files
