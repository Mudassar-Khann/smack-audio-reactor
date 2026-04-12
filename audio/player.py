import pygame
from pathlib import Path

class SoundPlayer:

    _initialized = False

    BASE_DIR = Path(__file__).resolve().parents[1]
    path = BASE_DIR / "assets" / "sounds"

    sounds = {i.stem: str(i) for i in path.iterdir() if i.is_file()}


    @classmethod
    def init(cls):
        if not cls._initialized:
            pygame.mixer.init()
            cls._initialized = True


    def play(cls, hit):
        if hit:
            if hit == "soft":
                sound = pygame.mixer.Sound(cls.sounds["modi-ji-bkl"])

            elif hit == "hard":
                sound = pygame.mixer.Sound(cls.sounds["yamate-kudesai"])

            return sound.play



