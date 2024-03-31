from pickle import dumps
from pyaudio import paAbort, paContinue, PyAudio
from struct import pack

from constants import CHANNELS, CHUNK, FORMAT, RATE
from globals import streaming

import tapp

def audioStreamCallback(inData: bytes | None, frameCount: int, timeInfo, statusFlags: tuple[bytes | None, int]):
    global streaming

    if not streaming: return (None, paAbort)

    data = dumps(inData)
    packedData = pack('Q', len(data)) + data
    tapp.transcriber.sendall(packedData)

    return (inData, paContinue)

audio = PyAudio()
stream: PyAudio.Stream

def open():
    global stream

    stream = audio.open(RATE, CHANNELS, FORMAT, True, frames_per_buffer=CHUNK, stream_callback=audioStreamCallback)

def close():
    stream.stop_stream()
    stream.close()
    audio.close()
    audio.terminate()
