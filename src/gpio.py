import RPi.GPIO as gpio

from time import sleep

from constants import BUTTON_RECORD, BUTTON_RESET_SHUTDOWN, LED_BLUE, LED_GREEN, LED_RED, LED_YELLOW
from globals import reset, shutdown, streaming

import audio
import tapp

HIGH = gpio.HIGH
IN = gpio.IN
LOW = gpio.LOW
OUT = gpio.OUT
PULL_DOWN = gpio.PUD_DOWN
RISING = gpio.RISING

def gpioSetup():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)

    gpio.setup(LED_BLUE, OUT, initial=LOW)
    gpio.setup(LED_GREEN, OUT, initial=LOW)
    gpio.setup(LED_RED, OUT, initial=HIGH)
    gpio.setup(LED_YELLOW, OUT, initial=LOW)

    gpio.setup(BUTTON_RECORD, IN, pull_up_down=PULL_DOWN)
    gpio.setup(BUTTON_RESET_SHUTDOWN, IN, pull_up_down=PULL_DOWN)

    gpioRegisterEvents()

    sleep(2)
    gpio.output(LED_RED, LOW)
    return

def gpioRegisterEvents():
    gpio.add_event_detect(BUTTON_RECORD, RISING, gpioRecordEvent)
    gpio.add_event_detect(BUTTON_RESET_SHUTDOWN, RISING, gpioResetShutdownEvent)

    return

def gpioRecordEvent():
    global streaming

    sleep(.5)
    if not gpio.input(BUTTON_RECORD): return
    gpio.remove_event_detect(BUTTON_RECORD)
    sleep(.25)

    streaming = not streaming
    if streaming: 
        tapp.startStream()
        audio.stream.start_stream()
    else:
        audio.stream.stop_stream()
        tapp.stopStream()
    gpio.output(LED_BLUE, streaming)

    gpio.add_event_detect(BUTTON_RECORD, RISING, gpioRecordEvent)
    return

def gpioResetShutdownEvent():
    global reset
    global shutdown
    global streaming

    sleep(.5)
    if not gpio.input(BUTTON_RESET_SHUTDOWN): return
    gpio.remove_event_detect(BUTTON_RESET_SHUTDOWN)

    streaming = False
    sleep(3)
    if not gpio.input(BUTTON_RESET_SHUTDOWN): reset = True
    else: shutdown = True

    gpio.output(LED_BLUE, False)

    gpio.add_event_detect(BUTTON_RESET_SHUTDOWN, RISING, gpioResetShutdownEvent)
    return