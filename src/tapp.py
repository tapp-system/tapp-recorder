from socket import AF_INET, socket, SOCK_STREAM
from time import sleep
from uuid import getnode

import lgpio as gpio
import re
import requests

from constants import API_KEY, HOST, SOCKET_PORT

transcriber = socket(AF_INET, SOCK_STREAM)

def getMacAddress() -> str:
    return ':'.join(re.findall('..', '%012x' % getnode()))

def connectTranscriber():
    mac = getMacAddress()

    if mac != getMacAddress():
        while True:
            # TODO Red led blinking
            pass

    transcriber.connect((HOST, SOCKET_PORT))
    transcriber.sendall(mac)

    status = transcriber.recv(2).decode()

    if status != 'OK':
        while True:
            # TODO Red led blinking
            pass

    return

def activate():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/activate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def deactivate():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/deactivate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def startStream():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/startStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def stopStream():
    try:
        response = requests.get('https://' + HOST + '/api/v1/transcriber/stopStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def setup():
    connectTranscriber()
    activate()

    return
