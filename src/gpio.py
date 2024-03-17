import RPi.GPIO as GPIO
import time

from audioStream import audio, audioStream, clientSocket, streaming

LED_BLUE = 36
LED_GREEN = 35
LED_RED = 40
LED_YELLOW = 38

BUTTON_RECORD = 33
BUTTON_SHUTDOWN = 32

def setupGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(LED_BLUE, GPIO.OUT, GPIO.LOW)
    GPIO.setup(LED_GREEN, GPIO.OUT, GPIO.LOW)
    GPIO.setup(LED_RED, GPIO.OUT, GPIO.HIGH)
    GPIO.setup(LED_YELLOW, GPIO.OUT, GPIO.LOW)

    GPIO.setup(BUTTON_SHUTDOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_RECORD, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    time.sleep(2)
    GPIO.output(LED_RED, GPIO.LOW)

def registerGPIOEvents():
    GPIO.add_event_detect(BUTTON_SHUTDOWN, GPIO.RISING, callback=shutdownEvent)
    GPIO.add_event_detect(BUTTON_RECORD, GPIO.RISING, callback=recordEvent)

def shutdownEvent(channel):
    audioStream.stop_stream()
    audioStream.close()
    audio.terminate()
    clientSocket.shutdown(0)
    clientSocket.close()

    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_YELLOW, GPIO.LOW)
    GPIO.cleanup()

def recordEvent(channel):
    global streaming
    time.sleep(1)
    if not input(BUTTON_RECORD): return
    GPIO.remove_event_detect(BUTTON_RECORD)
    time.sleep(2)

    if streaming:
        streaming = False
        GPIO.output(LED_BLUE, GPIO.LOW)
    else:
        streaming = True
        GPIO.output(LED_BLUE, GPIO.HIGH)

    GPIO.add_event_detect(BUTTON_RECORD, GPIO.RISING, callback=recordEvent)