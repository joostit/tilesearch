

from ToneGenerator import ToneGenerator, Waves
import threading
import time
from timeloop import Timeloop
from datetime import timedelta

class AudioIndicator:


    def __init__(self):
        self.Frequency = 1000
        self.Continue_Running = True
        self.generator = ToneGenerator()
        self.tl = Timeloop()
        pass

    @tl.job(interval=timedelta(seconds=2))
    def sample_job_every_2s(self):
        print
        "2s job current time : {}".format(time.ctime())


    def doBeep(self):
        print("Beeping...")
        self.generator.play(1000, 250, Waves.Square)
        time.sleep(100)


    def start_indicator(self):
        self.tl.start(block=False)
