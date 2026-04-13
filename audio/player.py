import pygame
from pathlib import Path

class SoundPlayer:
    _initialized = False

    def __init__(self):
        SoundPlayer.init()

        base = Path(__file__).resolve().parents[1]
        sounds_path = base / "assets" / "sounds"

        # preload sounds
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

    def play(self, sound_name: str | None):
        if sound_name is None:
            return

        sound = self._sounds.get(sound_name)

        if sound:
            sound.play()
        else:
            print(f"[WARN] Sound '{sound_name}' not found")
