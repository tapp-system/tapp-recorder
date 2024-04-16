from constants import L_GREEN
from gpio import blink

def reset():
    print('Reset triggered. Not working yet...')

    blink(L_GREEN, .5, 0)

    return
