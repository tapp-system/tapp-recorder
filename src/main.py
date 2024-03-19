import RPi.GPIO as GPIO

from constants import LED_GREEN, LED_YELLOW
from gpio import registerGPIOEvents, setupGPIO
from netSocket import connect
from audioStream import stream

def setup():
    setupGPIO()

    GPIO.output(LED_YELLOW, GPIO.HIGH)
    registerGPIOEvents()
    connect()
    GPIO.output(LED_YELLOW, GPIO.LOW)

    GPIO.output(LED_GREEN, GPIO.HIGH)

def main():
    setup()
    while True:
        stream()

if __name__ == '__main__':
    main()