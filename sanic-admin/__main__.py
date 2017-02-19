import os
import sys
import time
from subprocess import Popen
from signal import SIGTERM
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class RestartHandler(PatternMatchingEventHandler):

    def __init__(self, executable, args):
        super().__init__(patterns=['*.py'])
        self._args = ([executable, *args])
        self._start()
        self._last_time = 0
        self._skip_time = 0.75

    def _start(self):
        proc = Popen(self._args)
        self.pid = proc.pid
        self._last_time = time.time()

    def on_any_event(self, event):
        now = time.time()
        if (now - self._last_time) < self._skip_time:
            return
        os.kill(self.pid, SIGTERM)
        time.sleep(0.5)
        self._start()


path = os.getcwd()
observer = Observer()
handler = RestartHandler(sys.executable, sys.argv[1:])
observer.schedule(handler, path, recursive=True)
observer.start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        os.kill(handler.pid, SIGTERM)
        time.sleep(0.6)
        observer.stop()
        break
observer.join()
