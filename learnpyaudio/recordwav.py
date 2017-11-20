import pyaudio
import wave
import sys

## TAKEN FROM https://abhgog.gitbooks.io/pyaudio-manual/content/installation.html
def record(outputFile):
    CHUNK = 1024  # measured in bytes
    FORMAT = pyaudio.paInt16
    CHANNELS = 2  # stereo
    RATE = 44100  # common sampling frequency
    RECORD_SECONDS = 5  # change this record for longer or shorter!

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

record("./learnpyaudio/assets/done.wav")
