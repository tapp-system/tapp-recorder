from time import sleep

import os
import RPi.GPIO as gpio

from constants import LED_BLUE, LED_GREEN, LED_RED, LED_YELLOW

import audio
import tapp

def shutdown():
    gpio.output(LED_BLUE, gpio.LOW)
    gpio.output(LED_GREEN, gpio.LOW)
    gpio.output(LED_RED, gpio.LOW)
    gpio.output(LED_YELLOW, gpio.LOW)

    c = 0
    intervalTime = .25
    while c < 4:
        gpio.output(LED_YELLOW, gpio.HIGH)
        sleep(intervalTime / 2)
        gpio.output(LED_YELLOW, gpio.LOW)
        sleep(intervalTime / 2)

        c += 1

    audio.close()
    tapp.setInactive()
    tapp.transcriber.shutdown(0)
    tapp.transcriber.close()
    gpio.cleanup()
    os.system('shutdown now')
    return
