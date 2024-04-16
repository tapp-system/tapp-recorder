from subprocess import run

from constants import L_YELLOW

import audio
import gpio
import tapp

def shutdown():
    gpio.deactivate()
    audio.stream.stop_stream()
    tapp.stopStream()
    tapp.deactivate()
    gpio.blink(L_YELLOW, .2, 10)

    audio.close()
    gpio.close()
    tapp.close()

    run(['shutdown', 'now'])
    return