import pickle, zlib, os
from functools import lru_cache

class CacheManager:
    def __init__(self, path, max_items=5000):
        self.path = path; os.makedirs(path, exist_ok=True)
    @lru_cache(maxsize=5000)
    def get(self, key):
        fname = os.path.join(self.path, f"{key}.cache")
        if os.path.exists(fname):
            data = zlib.decompress(open(fname,"rb").read())
            return pickle.loads(data)
    def set(self, key, value):
        data = zlib.compress(pickle.dumps(value))
        with open(os.path.join(self.path, f"{key}.cache"),"wb") as f:
            f.write(data)
    def clear(self):
        for f in os.listdir(self.path):
            os.remove(os.path.join(self.path,f))
