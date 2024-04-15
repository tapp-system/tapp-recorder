import lgpio

from constants import HIGH, LOW, L_YELLOW

import audio
import gpio
import tapp

def setup():
    gpio.setup()

    lgpio.gpio_write(gpio.handle, L_YELLOW, HIGH)
    tapp.setup()
    audio.setup()
    lgpio.gpio_write(gpio.handle, L_YELLOW, LOW)

    return
