from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WatchHandler(FileSystemEventHandler):
    def __init__(self, queue): self.q=queue
    def on_any_event(self,e):
        if not getattr(e,'is_directory',False): self.q.put(e)

class FileWatcher:
    def __init__(self, paths, queue):
        self.obs=Observer(); self.queue=queue
        for p in paths: self.obs.schedule(WatchHandler(queue), p, recursive=True)
    def start(self): self.obs.start()
    def stop(self): self.obs.stop(); self.obs.join()
