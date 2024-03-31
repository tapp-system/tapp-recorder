from globals import reset, shutdown, streaming

import RPi.GPIO as gpio

import audio
import main
import tapp

def reset():
    reset = False
    shutdown = False
    streaming = False

    audio.close()
    tapp.setInactive()
    tapp.transcriber.shutdown(0)
    tapp.transcriber.close()
    gpio.cleanup()

    return main()