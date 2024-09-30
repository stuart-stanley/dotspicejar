"""
turn gooy grbl protocol into something useful.

- provides/properties
  - connected?
  - status (last):
    - running/idle
    - alarm
    - position data
- active:
  - asyncio get status
- msgs:
  - status change w/ status
  - alarm?
  -
"""
import threading
import serial
import time

_STATUS_POLL_INTERVAL__S = 5

class _Watch:
    def __init__(self, match_text, exclusive=False, callback=None):
        self.correlation_id = time.time()
        self.match_text = match_text
        self.exclusive = exclusive
        self.callback = callback

    def __str__(self):
        rs = "(coid={},text='{}',exc={},cb={})".format(
            self.correlation_id, self.match_text, self.exclusive, self.callback)
        return rs


class HamsterWheel(threading.Thread):
    def __init__(self, serial="/dev/cu.usbserial-141520"):
        super().__init__(name="drill", daemon=True)
        self.__keep_running = True
        self.__serial_path = serial
        self.__serial_port = None
        self.__serial_ready = False
        self.__last_status_time = time.time()
        self.__status_poll_outstanding = False
        self.__watches = []

    def run(self):
        while self.__keep_running:
            try:
                self.__safe_run()
            except Exception as ex:
                print("safe-exception", ex)

    def __safe_run(self):
        while self.__keep_running:
            if self.__serial_port is None:
                self.__connect()
                continue
            # kciks go here
            self.__do_read()

    def __do_read(self):
        data = self.__serial_port.read_until()
        print("data=",data)
        new_watches = []
        for watch in self.__watches:
            keep = True   # TODO: not sure this is thread safe
            if watch.match_text in data:
                print("matched", watch)
                if watch.callback is not None:
                    if watch.callback(data, watch):
                        keep = False
            if keep:
                new_watches.append(watch)
        self.__watches = new_watches

    def do_status_poll(self):
        assert not self.__status_poll_outstanding, "TODO: recover"
        self.__serial_port

    def __connect(self):
        print("connecting to", self.__serial_path)
        self.__serial_ready = False
        self.__serial_port = serial.Serial(port=self.__serial_path, baudrate=115200)
        # TODO: handle kaboom
        print("Connected", self.__serial_port.is_open)
        self.__do_watch_for(rb"[MSG:'$H'|'$X' to unlock]", exclusive=True, cb=self.__connected)

    def __connected(self, found_text, watcher):
        print("connect saw grbl data")
        self.__serial_ready = True
        return True

    def __do_watch_for(self, txt, exclusive=False, cb=None):
        watch = _Watch(txt, exclusive, cb)
        self.__watches.append(watch)

if __name__ == "__main__":
    da = HamsterWheel()
    da.start()
    time.sleep(100)
