from socket import AF_INET, socket, SOCK_STREAM
from time import sleep
from uuid import getnode

import re
import requests
import RPi.GPIO as gpio

from constants import API_KEY, HOST, LED_RED, SOCKET_PORT

transcriber = socket(AF_INET, SOCK_STREAM)

def getMacAddress() -> str:
    return ':'.join(re.findall('..', '%012x' % getnode()))

def connectTranscriber():
    mac = getMacAddress()
    if mac != getMacAddress():
        while True:
            gpio.output(LED_RED, gpio.HIGH)
            sleep(.5)
            gpio.output(LED_RED, gpio.LOW)
            sleep(.5)

    transcriber.connect((HOST, SOCKET_PORT))
    transcriber.sendall(mac)

    return

def setActive():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/activate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return

def setInactive():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/deactivate', headers={
            'x-macaddress': getMacAddress(),
            'x-api': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return

def startStream():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/startStream', headers={
            'x-macaddress': getMacAddress(),
            'x-api': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return

def stopStream():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/stopStream', headers={
            'x-macaddress': getMacAddress(),
            'x-api': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return

def tappSetup():
    connectTranscriber()
    setActive()

    return