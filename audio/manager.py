import random

class SoundManager:
    def __init__(self):
        self.sound_map = {
            "soft": ["modi-ji-bkl", "s2", "s3"],
            "hard": ["yamate-kudesai", "s4", "s5"]
        }

        self._last_played = None

    def get_sound(self, event: str | None):
        if event is None:
            return None

        sounds = self.sound_map.get(event)

        if not sounds:
            return None
        if len(sounds) > 1:
            choices = [s for s in sounds if s != self._last_played]
        else:
            choices = sounds

        name = random.choice(choices)
        self._last_played = name

        return name
