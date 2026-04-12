import time

class ImpactDetector:
    def __init__(self, low_threshold, high_threshold, cooldown=3.0):
        if low_threshold >= high_threshold:
            raise ValueError("low_threshold must be less than high_threshold")

        self.high_threshold = high_threshold
        self.low_threshold = low_threshold
        self.cooldown = cooldown
        self.last_hit = 0.0

    def detect(self, volume):
        now = time.perf_counter()


        if volume >= self.high_threshold:
            event = "hard"
        elif volume >= self.low_threshold:
            event = "soft"
        else:
            return None

        if (now - self.last_hit) >= self.cooldown:
            self.last_hit = now
            return event

        return None
