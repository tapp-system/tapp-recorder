from threading import Thread
from time import sleep

import lgpio as gpio

from constants import B_RECORD, B_RES_SHUT, HIGH, LOW, L_BLUE, L_GREEN, L_RED, L_YELLOW
from globals import reset, shutdown, streaming

import audio
import tapp

handle = gpio.gpiochip_open(0)

def inputEvent(pin: int, cb = None):
    if not cb:
        print('Callback for input-event at pin: ' + pin + ' has no callback function')
        return

    def target():
        while True:
            if gpio.gpio_read(handle, pin) == 1: cb()

    Thread(target=target).start()
    print('Registered input-event for pin ' + pin)

    return

def registerInputs():
    gpio.gpio_claim_input(handle, B_RECORD, gpio.SET_PULL_DOWN)
    gpio.gpio_claim_input(handle, B_RES_SHUT, gpio.SET_PULL_DOWN)

    registerInputEvents()
    return

def registerInputEvents():
    inputEvent(B_RECORD, recordEvent)
    inputEvent(B_RES_SHUT, resShutEvent)
    return

def registerOutputs():
    gpio.gpio_claim_output(handle, L_RED, HIGH)
    gpio.gpio_claim_output(handle, L_BLUE, LOW)
    gpio.gpio_claim_output(handle, L_GREEN, LOW)
    gpio.gpio_claim_output(handle, L_YELLOW, LOW)
    return

def recordEvent():
    global streaming

    streaming = not streaming
    if streaming:
        tapp.startStream()
        audio.stream.start_stream()
    else:
        tapp.stopStream()
        audio.stream.stop_stream()

    gpio.gpio_write(handle, L_BLUE, HIGH if streaming else LOW)
    return

def resShutEvent():
    global reset
    global shutdown
    global streaming

    sleep(3)
    if gpio.gpio_read(handle, B_RES_SHUT) == 1: shutdown = True
    else: reset = True

    gpio.gpio_write(handle, L_BLUE, LOW)
    return

def setup():
    registerOutputs()
    registerInputs()

    gpio.gpio_write(handle, L_RED, LOW)
    return
