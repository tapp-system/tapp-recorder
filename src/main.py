import RPi.GPIO as GPIO

from gpio import LED_GREEN, LED_YELLOW, registerGPIOEvents, setupGPIO
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