import time

class ImpactDetector:
    def __init__(self, low_threshold, high_threshold, spike_threshold=0.040, cooldown=2.0):
        if low_threshold >= high_threshold:
            raise ValueError("low_threshold must be less than high_threshold")

        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        self.spike_threshold = spike_threshold
        self.cooldown = cooldown

        self.last_hit = 0.0
        self.prev_volume = 0.0

    def detect(self, volume):
        now = time.perf_counter()


        spike = volume - self.prev_volume

        self.prev_volume = volume

        if spike < self.spike_threshold:
            return None
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



    def __repr__(self):
        return (f"ImpactDetector(low={self.low_threshold}, "
                f"high={self.high_threshold}, cooldown={self.cooldown})")
