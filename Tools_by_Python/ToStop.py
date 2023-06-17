import threading, sys, time
sys.dont_write_bytecode=True

class StoppableThread(threading.Thread):
    """Thread class with a stop() method."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()