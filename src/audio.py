from pickle import dumps
from pyaudio import paComplete, paContinue, PyAudio
from struct import pack

from constants import CHANNELS, CHUNK, FORMAT, RATE

import globals as g
import tapp

audio = PyAudio()
stream: PyAudio.Stream

def close():
    stream.stop_stream()
    audio.close(stream)
    audio.terminate()
    print("Closed Audio")
    return

def streamCallback(inData: bytes | None, frameCount: int, timeInfo, statusFlags: tuple[bytes | None]):
    if not g.streaming: return (None, paComplete)

    data = dumps(inData)
    packedData = pack('Q', len(data)) + data
    tapp.transcriber.sendall(packedData)

    return (inData, paContinue)

def setup():
    global stream

    stream = audio.open(
        channels=CHANNELS,
        format=FORMAT,
        frames_per_buffer=CHUNK,
        input=True, rate=RATE,
        stream_callback=streamCallback
    )

    stream.stop_stream()
    print("Audio is ready!")
    return
