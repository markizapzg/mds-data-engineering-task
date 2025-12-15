from src.files.file import File
from src.files.strategy import SequentialBucketingStrategy


def test_bucket_size_limit():
    files = [
        File("a", 6_000_000),
        File("b", 5_000_000),
        File("c", 4_000_000),
    ]

    strategy = SequentialBucketingStrategy()
    buckets = strategy.create_buckets(files)

    for bucket in buckets:
        assert bucket.size <= 10_000_000
