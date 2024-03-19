from pickle import dumps
from pyaudio import paAbort, paContinue, paInt24, PyAudio
from struct import pack

import RPi.GPIO as GPIO
import time

from constants import LED_BLUE
from netSocket import clientSocket

CHANNELS = 2
CHUNK = 1024
FORMAT = paInt24
RATE = 192000

streaming = False

def streamCallback(inData: bytes | None, frameCount: int, timeInfo, statusFlags: tuple[bytes | None, int]):
    if not streaming: return (None, paAbort)

    GPIO.output(LED_BLUE, GPIO.HIGH)
    a = dumps()
    message = pack("Q", len(a))+a
    clientSocket.sendall(message)
    GPIO.output(LED_BLUE, GPIO.LOW)

    return (inData, paContinue)

audio = PyAudio()
audioStream = audio.open(channels=CHANNELS, format=FORMAT, frames_per_buffer=CHUNK, input=True, rate=RATE, stream_callback=streamCallback)

def stream():
    global streaming

    while streaming:
        audioStream.start_stream()

        startTime = time.time()
        while time.time() - startTime < 5: pass

        audioStream.stop_stream()
