import threading
import time


class Timer:
    def __init__(self):
        self.time_left = 30
        self.on = False
        self.thread = None
        
    def countdown(self):
        while self.time_left > 0 and self.on:
            time.sleep(1)
            self.time_left -= 1

    def start(self):
        if not self.on:
            self.on = True
            self.time_left = 30
            self.thread = threading.Thread(target=self.countdown)
            self.thread.start()

    def stop(self):
        self.on = False
        self.thread = None

    def reset(self):
        self.stop()
        self.time_left = 30 
