from messaging.batch_manager import MiniBatchManager
from messaging.source import MessageSource
from workers.worker_pool import WorkerPool
from files.processor import FileProcessor
from files.strategy import SequentialBucketingStrategy


def main():
    worker_pool = WorkerPool()

    batch_manager = MiniBatchManager(
        batch_duration_seconds=5,
        worker_pool=worker_pool
    )

    source = MessageSource(batch_manager)
    source.start()

    file_processor = FileProcessor(
        strategy=SequentialBucketingStrategy(),
        worker_pool=worker_pool
    )

    file_processor.process_nightly_files()

    worker_pool.shutdown()


if __name__ == "__main__":
    main()
