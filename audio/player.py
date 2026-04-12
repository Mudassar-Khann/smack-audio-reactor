import pygame
from pathlib import Path

class SoundPlayer:


    def paly(hit):
        if hit:
            base = Path(__file__).parent
            path = base.parent / "aasets" / "sounds"
            if hit == "soft":
                sound = pygame.mixer.Sound(path.write_text("anime-ahh.wav"))

            elif hit == "hard":
                sound = pygame.mixer.Sound(path.write_text("yamate-kudesai.wav"))

            return sound.play()










