import audio
import gpio
import tapp

def setup():
    print("Setup Triggered")
    gpio.setup()
    gpio.yellow(True)
    audio.setup()
    tapp.setup()
    gpio.yellow(False)
    print("Setup complete")
    return
