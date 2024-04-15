import lgpio as gpio

from constants import HIGH, L_GREEN
from globals import reset, shutdown
from gpio import handle
from setup import setup

import shutdown as s

def main():
    setup()

    gpio.gpio_write(handle, L_GREEN, HIGH)
    while True:
        if reset:
            # TODO reset functionality
            while True:
                pass
        elif shutdown:
            s.shutdown()
            break
        else: pass

    return


# Start sequence:
if __name__ == '__main__':
    main()
