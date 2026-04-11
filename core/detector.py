class ImpactDetactor:
    def __init__(self, hthreshold, lthreshold):

        self.high_threshold = hthreshold
        self.low_threshold = lthreshold

    def detect(self, volume ):
        if volume > self.high_threshold:
            return "high"
        elif volume > self.low_threshold and volume < self.high_threshold:
            return "low"

        else: return None




