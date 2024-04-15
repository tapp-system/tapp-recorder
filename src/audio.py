from pickle import dumps
from pyaudio import paAbort, paContinue, PyAudio
from struct import pack

from constants import CHANNELS, CHUNK, FORMAT, RATE
from globals import streaming

import tapp

audio = PyAudio()
stream: PyAudio.Stream

def streamCallback(inData: bytes | None, framceCount: int, timeInfo,statusFlags: tuple[bytes | None, int]):
    global streaming

    if not streaming: return (None, paAbort)

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
        input=True,
        rate=RATE,
        stream_callback=streamCallback
    )

    return

def close():
    stream.stop_stream()
    stream.close()
    audio.close()
    audio.terminate()

    return
