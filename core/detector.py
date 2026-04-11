class ImpactDetector:
    def __init__(self, high_threshold, low_threshold):
        self.high_threshold = high_threshold
        self.low_threshold = low_threshold

    def detect(self, volume):
        if volume >= self.high_threshold:
            return "high"
        elif volume >= self.low_threshold:
            return "low"
        return None
