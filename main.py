import sounddevice as sd
import numpy as np
from core.detector import ImpactDetector
from audio.player import SoundPlayer
from audio.manager import SoundManager

# low_threshold  = 0.050
# high_threshold = 0.088

imp = ImpactDetector(
    low_threshold  = 0.055,
    high_threshold = 0.15,
    spike_threshold = 0.045,
    cooldown = 1.5
)
sp  = SoundPlayer()

manager = SoundManager()

def callback(indata, frames, time_info, status):
    volume = np.abs(indata).mean()

    impact = imp.detect(volume)

    sound = manager.get_fixed_sound(impact)

    sp.play(sound)

with sd.InputStream(callback=callback, channels=1, samplerate=44100, blocksize=1024):
    input("Listening... press Enter to stop\n")
