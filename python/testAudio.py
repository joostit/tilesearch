import os
import time


while True:
    os.system("AUDIODRIVER=alsa AUDIODEV=hw:0,0 play -n -c1 synth 3 sine 1000")
    time.sleep(2)