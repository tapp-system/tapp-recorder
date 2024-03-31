import RPi.GPIO as gpio

from constants import LED_YELLOW
from gpio import gpioSetup
from tapp import tappSetup

import audio

def setup():
    gpioSetup()

    gpio.output(LED_YELLOW, gpio.HIGH)
    tappSetup()
    audio.open()
    gpio.output(LED_YELLOW, gpio.LOW)
    return
