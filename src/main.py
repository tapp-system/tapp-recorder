import RPi.GPIO as gpio

from constants import LED_GREEN
from globals import reset, shutdown
from setup import setup

import reset as r
import shutdown as s

def main():
    global reset
    global shutdown

    setup()

    gpio.output(LED_GREEN, gpio.HIGH)
    while True:
        if reset:
            r.reset()
            break

        if shutdown:
            s.shutdown()
            break

        pass

if __name__ == '__main__':
    main()