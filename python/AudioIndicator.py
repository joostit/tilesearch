

from ToneGenerator import ToneGenerator
import threading
import time

class AudioIndicator:

    duration = 0.1
    amplitude = 1

    def __init__(self):
        self.Frequency = 1000
        self.Continue_Running = True
        pass

    def thread_function(self):

        while self.Continue_Running:
            print("Playing...")
            generator = ToneGenerator()
            generator.play(self.Frequency, self.duration, self.amplitude)
            time.sleep(1)


    def start_indicator(self):
        audio_thread = threading.Thread(target=self.thread_function, daemon=True)
        audio_thread.start()
