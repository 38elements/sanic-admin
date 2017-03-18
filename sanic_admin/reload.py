import os
import sys
import time
from subprocess import Popen
from signal import SIGTERM
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class RestartHandler(PatternMatchingEventHandler):

    def __init__(self, executable, args, patterns, before_each, after_each):
        super().__init__(patterns=patterns)
        self._before_each = before_each
        self._after_each = after_each
        self._args = ([executable, *args])
        self._start()
        self._last_time = 0
        self._skip_time = 0.75

    def _start(self):
        if self._before_each:
            exec(open(self._before_each).read())
        proc = Popen(self._args)
        if self._after_each:
            exec(open(self._after_each).read())
        self.pid = proc.pid
        self._last_time = time.time()

    def on_any_event(self, event):
        now = time.time()
        if (now - self._last_time) < self._skip_time:
            return
        os.kill(self.pid, SIGTERM)
        time.sleep(0.5)
        self._start()


def run(setting):
    if setting['before']:
        exec(open(setting['before']).read())

    handler = RestartHandler(
        sys.executable, sys.argv[1:], setting['patterns'],
        setting['before_each'], setting['after_each'])

    observer = Observer()
    paths = setting['paths']
    for path in paths:
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
    if setting['after']:
        exec(open(setting['after']).read())
    observer.join()


if __name__ == '__main__':
    run({
        'paths': [os.getcwd()],
        'patterns': ['*.py'],
        'before': None,
        'before_each': None,
        'after': None,
        'after_each': None,
        'app': 'app'
    })
