import time
class HealthManager:
    def __init__(self,pool): self.pool=pool; self.last_check=0
    def check(self):
        if time.time()-self.last_check>300:
            with self.pool.get() as conn:
                assert conn.execute("PRAGMA integrity_check").fetchone()[0]=='ok'
            self.last_check=time.time()
