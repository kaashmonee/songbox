import pyaudio
import wave
import sys

def main():
    CHUNK = 1024

    """
    # not entirely sure what this is doing...
    if len(sys.argv) < 2:
        print("Plays a wave file. \n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    # opening the wave file
    wf = wave.open(sys.argv[1], "rb")

    # instantiating pyaudio
    p = pyaudio.PyAudio()

    # opening a stream -- a channel with which it can 
    """
    CHUNK = 1024


    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    waveFilePath = "./learnpyaudio/assets/filename.wav"
    wf = wave.open(waveFilePath, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
    

if __name__ == "__main__":
    main()
