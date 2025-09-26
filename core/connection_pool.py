import sqlite3, queue
from contextlib import contextmanager

class ConnectionPool:
    def __init__(self, db_path, size=10):
        self._pool = queue.Queue(maxsize=size)
        for _ in range(size):
            conn = sqlite3.connect(db_path, check_same_thread=False)
            conn.execute("PRAGMA journal_mode=WAL")
            self._pool.put(conn)
    @contextmanager
    def get(self):
        conn = self._pool.get()
        try:
            yield conn
        finally:
            self._pool.put(conn)
    def close(self):
        while not self._pool.empty():
            self._pool.get().close()
