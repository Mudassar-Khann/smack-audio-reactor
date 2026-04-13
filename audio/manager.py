import random
from config import SOUNDS


class SoundManager:
    """
    Responsible for:
    - choosing WHICH sound to play

    DOES NOT:
    - play sounds
    """

    def __init__(self):
        self.random_sounds = SOUNDS["random"]
        self.fixed_sounds = SOUNDS["fixed"]

        self._last_played = None

    def get_random_sound(self, event):
        if event is None:
            return None

        sounds = self.random_sounds.get(event)
        if not sounds:
            return None

        # avoid repeating same sound
        if len(sounds) > 1:
            choices = [s for s in sounds if s != self._last_played]
        else:
            choices = sounds

        name = random.choice(choices)
        self._last_played = name
        return name

    def get_fixed_sound(self, event):
        if event is None:
            return None

        return self.fixed_sounds.get(event)
