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

    def run(self):
        while not self.stopped():
            # Insert your thread's main logic here

            # Check for the stop event
            if self.stopped():
                # Perform cleanup actions if needed
                return  # Exit the run method and stop the thread