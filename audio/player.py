import pygame
from pathlib import Path
import time
class SoundPlayer:
    _initialized = False

    def __init__(self):
        SoundPlayer.init()
        base = Path(__file__).resolve().parents[1]
        sounds_path = base / "assets" / "sounds"


        self._sounds = {
            f.stem: pygame.mixer.Sound(str(f))
            for f in sounds_path.iterdir()
            if f.suffix == ".wav"
        }

    @classmethod
    def init(cls):
        if not cls._initialized:
            pygame.mixer.init()
            cls._initialized = True

    def play(self, hit: str | None):
        if hit is None:
            return
        sound_map = {
            "soft": "modi-ji-bkl",
            "hard": "yamate-kudesai"
        }
        name = sound_map.get(hit)
        if name and name in self._sounds:
            self._sounds[name].play()
        else:
            print(f"[WARN] No sound mapped for hit='{hit}'")

