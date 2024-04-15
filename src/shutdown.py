from time import sleep

import lgpio
import os

from constants import HIGH, LOW, L_BLUE, L_GREEN, L_RED, L_YELLOW
from gpio import handle

import audio
import tapp

def shutdown():
    lgpio.gpio_write(handle, L_BLUE, LOW)
    lgpio.gpio_write(handle, L_GREEN, LOW)
    lgpio.gpio_write(handle, L_RED, LOW)
    lgpio.gpio_write(handle, L_YELLOW, LOW)

    counter = 0
    intervalTime = .25
    while counter < 4:
        lgpio.gpio_write(handle, L_YELLOW, HIGH)
        sleep(intervalTime)
        lgpio.gpio_write(handle, L_YELLOW, LOW)
        sleep(intervalTime)
        counter += 1

    audio.close()
    tapp.setInactive()
    tapp.transcriber.shutdown(0)
    tapp.transcriber.close()

    os.remove('shutdown now')
    return
