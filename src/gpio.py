from threading import Thread
from time import sleep

import lgpio as gpio

from constants import B_RECORD, B_RES_SHUT, HIGH, LOW, L_BLUE, L_GREEN, L_RED, L_YELLOW, PULL_DOWN

import audio
import globals as g
import tapp

handle = gpio.gpiochip_open(0)

def blink(pin: int, interval: float, iterations: int = 0):
    def blinkInterval(pin: int, interval: float):
        gpio.gpio_write(handle, pin, HIGH)
        sleep(interval)
        gpio.gpio_write(handle, pin, LOW)
        sleep(interval)
        return

    if iterations <= 0:
        while True:
            blinkInterval(pin, interval)
    else:
        iteration = 0
        while iteration < iterations:
            blinkInterval(pin, interval)
            iteration += 1

    return

def close():
    gpio.gpio_free(handle, B_RECORD)
    gpio.gpio_free(handle, B_RES_SHUT)
    gpio.gpio_free(handle, L_BLUE)
    gpio.gpio_free(handle, L_GREEN)
    gpio.gpio_free(handle, L_RED)
    gpio.gpio_free(handle, L_YELLOW)
    gpio.gpiochip_close(handle)
    return

def deactivate():
    gpio.gpio_write(handle, L_BLUE, LOW)
    gpio.gpio_write(handle, L_GREEN, LOW)
    gpio.gpio_write(handle, L_RED, LOW)
    gpio.gpio_write(handle, L_YELLOW, LOW)
    return

def inputEvent(pin: int, cb = None):
    def target(pin: int, cb):
        while True:
            if gpio.gpio_read(handle, pin) == 0: pass
            sleep(.5)
            if gpio.gpio_read(handle, pin) == 1:
                cb()
                sleep(.5)

    if not cb:
        print('Callback for input event at pin: ' + str(pin) + ' has no callback function!')
        return

    Thread(target=target, args=(pin, cb)).start()
    print('Registered input event at pin: ' + str(pin) + ' has no callback function!')
    return

def recordEvent():
    g.streaming = not g.streaming
    if g.streaming:
        tapp.startStream()
        audio.stream.start_stream()
    else:
        tapp.stopStream()
        audio.stream.stop_stream()

    gpio.gpio_write(handle, L_BLUE, HIGH if g.streaming else LOW)
    return

def registerInputs():
    gpio.gpio_claim_input(handle, B_RECORD, PULL_DOWN)
    gpio.gpio_claim_input(handle, B_RES_SHUT, PULL_DOWN)

    inputEvent(B_RECORD, recordEvent)
    inputEvent(B_RES_SHUT, resShutEvent)

    return

def registerOutputs():
    gpio.gpio_claim_output(handle, L_RED, HIGH)
    gpio.gpio_claim_output(handle, L_BLUE, LOW)
    gpio.gpio_claim_output(handle, L_GREEN, LOW)
    gpio.gpio_claim_output(handle, L_YELLOW, LOW)

    return

def resShutEvent():
    g.streaming = False
    gpio.gpio_write(handle, L_BLUE, LOW)

    sleep(5)
    if gpio.gpio_read(handle, B_RES_SHUT) == 1: g.shutdown = True
    else: g.reset = True

    return

def setup():
    registerOutputs()
    registerInputs()

    gpio.gpio_write(handle, L_RED, LOW)
    return
