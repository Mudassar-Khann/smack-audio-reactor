import sounddevice as sd
import numpy as np


class MicListener:


    def __init__(self, samplerate, channels, blocksize, callback):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize


        self.callback = callback

        self.stream = None

    def _audio_callback(self, indata, frames, time_info, status):
        """
        This runs in REAL-TIME AUDIO THREAD.

        """

        if status:
            print(f"[WARN] {status}")

        volume = np.abs(indata).mean()


        self.callback(volume)

    def start(self):
        self.stream = sd.InputStream(
            callback=self._audio_callback,
            channels=self.channels,
            samplerate=self.samplerate,
            blocksize=self.blocksize
        )
        self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
