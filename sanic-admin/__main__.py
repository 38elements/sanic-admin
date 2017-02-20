import os
import sys
import time
import json
from subprocess import Popen
from signal import SIGTERM
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


SETTING_FILE_NAME = 'sanic-admin.json'


class RestartHandler(PatternMatchingEventHandler):

    def __init__(self, executable, args, patterns):
        super().__init__(patterns=patterns)
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


setting_file = None
setting = {
    'path': None,
    'patterns': ['*.py']
}
try:
    setting_file = open(SETTING_FILE_NAME, 'r')
except:
    pass

if setting_file:
    _setting = json.load(setting_file)
    setting_file.close()
    for key in setting.keys():
        if key in _setting:
            setting[key] = _setting[key]


path = setting['path'] if setting['path'] else os.getcwd()
observer = Observer()
handler = RestartHandler(sys.executable, sys.argv[1:], setting['patterns'])
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
