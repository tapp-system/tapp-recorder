#!/bin/sh

# Setup GPIO PIN
echo modes 6 w > /dev/pigpio

# Enable WHITE LED
echo w 6 1 > /dev/pigpio

# Start Python script
# TODO Learn and try out VENV
# venv ./venv/Scripts/activate
sudo doppler run python ./src/main.py