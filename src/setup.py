import audio
import gpio
import tapp

def setup():
    audio.setup()
    gpio.setup()
    tapp.setup()
    return
