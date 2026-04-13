import sounddevice as sd
import numpy as np
from core.detector import ImpactDetector
from audio.player import SoundPlayer

low_threshold  = 0.050
high_threshold = 0.088

imp = ImpactDetector(low_threshold, high_threshold)
sp  = SoundPlayer()

def callback(indata, frames, time_info, status):   # ← renamed parameter
    volume = np.abs(indata).mean()
    impact = imp.detect(volume)
    sp.play(impact)                                # ← play and return immediately

with sd.InputStream(callback=callback, channels=1, samplerate=44100, blocksize=1024):
    input("Listening... press Enter to stop\n")
