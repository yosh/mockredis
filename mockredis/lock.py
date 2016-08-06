class MockRedisLock(object):
    """
    Poorly imitate a Redis lock object from redis-py
    to allow testing without a real redis server.
    """

    def __init__(self, redis, name, timeout=None, sleep=0.1,
                 blocking=True, blocking_timeout=None, thread_local=True):
        """Initialize the object."""

        self.redis = redis
        self.name = name
        self.acquired_until = None
        self.timeout = timeout
        self.sleep = sleep
        self.blocking = blocking
        self.blocking_timeout = blocking_timeout
        self.thread_local = bool(thread_local)

    def acquire(self, blocking=True):  # pylint: disable=R0201,W0613
        """Emulate acquire."""

        return True

    def release(self):   # pylint: disable=R0201
        """Emulate release."""

        return

    def extend(self, additional_time):  # pylint: disable=R0201,W0613
        """Emulate extend."""

        return

    def __enter__(self):
        self.acquire(blocking=True)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()
