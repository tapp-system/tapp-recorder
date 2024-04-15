from os import getenv
from pyaudio import paInt24

# AUDIO

CHANNELS = 2
CHUNK = 1024
FORMAT = paInt24
RATE = 192000


# GPIO
# Numbers are the GPIO numbers, not the actual PIN numbers
# Constants prefixed with B_ are buttons
# Constants prefixed with L_ are leds

B_RECORD = 13
B_RES_SHUT = 12

L_BLUE = 16
L_GREEN = 19
L_RED = 21
L_YELLOW = 20

HIGH = 1
LOW = 0


# TAPP

API_KEY = getenv('TAPP_API_KEY')
HOST = getenv('TAPP_HOST')
SOCKET_PORT = getenv('TAPP_SOCKET_PORT')
