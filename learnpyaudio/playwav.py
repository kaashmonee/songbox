import pyaudio
import wave
import sys

class SongPlayer:
    def __init__(self):
        self.CHUNK = 1024

        self.waveFilePath = "./learnpyaudio/assets/filename.wav"
        self.wf = wave.open(self.waveFilePath, 'rb')

        # instantiate PyAudio (1)
        self.p = pyaudio.PyAudio()

        # open stream basically opens up a channel for playing
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True)

        # read data
        self.data = self.wf.readframes(self.CHUNK)

        # play stream (3)

    def play(self):
        while len(self.data) > 0:
            self.stream.write(self.data)
            self.data = self.wf.readframes(self.CHUNK)

        # stop stream (4)
        self.stream.stop_stream()
        self.stream.close()

        # close PyAudio (5)
        self.p.terminate()
    

def main():
    player = SongPlayer()
    player.play()
if __name__ == "__main__":
    main()
