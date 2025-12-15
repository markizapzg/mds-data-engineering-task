from src.workers.worker_pool import WorkerPool


def test_worker_pool_submit():
    pool = WorkerPool(workers=2)
    pool.submit("test")
    pool.shutdown()
