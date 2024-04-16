from socket import AF_INET, socket, SOCK_STREAM
from uuid import getnode

import re
import requests

from constants import API_KEY, HOST, SOCKET_PORT

transcriber = socket(AF_INET, SOCK_STREAM)

def activate():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/activate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def close():
    return

def connect():
    mac = getMacAddress()

    if mac != getMacAddress():
        while True:
            # TODO
            pass

    transcriber.connect((HOST, SOCKET_PORT))
    transcriber.sendall(mac.encode())

    status = transcriber.recv(2).decode()

    if status != 'OK':
        while True:
            # TODO
            pass

    return

def deactivate():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/deactivate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def getMacAddress():
    return ':'.join(re.findall('..', '%012x' % getnode()))

def setup():
    connect()
    activate()

    return

def startStream():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/startStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def stopStream():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/stopStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
