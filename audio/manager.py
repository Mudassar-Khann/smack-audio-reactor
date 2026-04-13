import random

class SoundManager:
    def __init__(self):
        self.random_sounds = {
            "soft": ["modi-ji-bkl", "s2", "s3"],
            "hard": ["yamate-kudesai", "h2", "h3"]
        }

        self.fixed_sounds = {
            "soft": "modi-ji-bkl",
            "hard": "yamate-kudesai"
        }

        self._last_played = None

    def get_random_sound(self, event: str | None):
        if event is None:
            return None

        sounds = self.random_sounds(event)
        if not sounds:
            return None

        if len(sounds) > 1:
            choices = [s for s in sounds if s != self._last_played]
        else:
            choices = sounds

        name = random.choice(choices)
        self._last_played = name
        return name
    def get_fixed_sound(self, event: str | None):
        if event is None:
            return None

        sounds = self.fixed_sounds(event)
        if not sounds:
            return None

        return sounds
