#!/bin/sh

# Setup GPIO PIN
echo modes 6 w > /dev/pigpio

# Enable WHITE LED
echo w 6 1 > /dev/pigpio

# Start Python script