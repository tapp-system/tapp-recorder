from reset import reset
from setup import setup
from shutdown import shutdown

import globals as g
import gpio

def main():
    print("Starting main-loop...")
    gpio.green(True)
    while True:
        if g.reset:
            reset()
            break
        elif g.shutdown:
            shutdown()
            break
        else: pass

    return

if __name__ == '__main__':
    setup()
    main()
