from core.detector import ImpactDetector
from audio.player import SoundPlayer
from audio.manager import SoundManager
from core.listener import MicListener
from config import Config, SETTINGS

from queue import Queue
import threading
import logging


# load detector config
det_cfg = SETTINGS["detector"]

detector = ImpactDetector(
    low_threshold=det_cfg["low_threshold"],
    high_threshold=det_cfg["high_threshold"],
    spike_threshold=det_cfg["spike_threshold"],
    cooldown=det_cfg["cooldown"]
)

player = SoundPlayer()
manager = SoundManager()


event_queue = Queue()


def on_volume(volume):
    """
    Runs in audio thread (via listener)

    """
    impact = detector.detect(volume)

    if impact:
        event_queue.put(impact)


def worker():

    while True:
        impact = event_queue.get()

        sound = manager.get_fixed_sound(impact)
        # You can use manager method to get_random and get fixed sound

        player.play(sound)

        if Config.DEBUG:
            print(f"[DEBUG] {impact}")
            logging.info(f"Impact: {impact}")


threading.Thread(target=worker, daemon=True).start()


listener = MicListener(
    samplerate=Config.SAMPLE_RATE,
    channels=Config.CHANNELS,
    blocksize=Config.BLOCK_SIZE,
    callback=on_volume
)

listener.start()

input("Listening... press Enter to stop\n")

listener.stop()
