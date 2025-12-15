from abc import ABC, abstractmethod
from .bucket import Bucket


class BucketingStrategy(ABC):
    @abstractmethod
    def create_buckets(self, files):
        pass


class SequentialBucketingStrategy(BucketingStrategy):
    MAX_SIZE = 10_000_000  # 10MB

    def create_buckets(self, files):
        buckets = []
        current = Bucket()

        for f in files:
            if current.size + f.size > self.MAX_SIZE:
                buckets.append(current)
                current = Bucket()

            current.add(f)

        if current.files:
            buckets.append(current)

        return buckets
