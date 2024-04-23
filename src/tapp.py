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
            print("Activated")
            return
    except requests.exceptions.HTTPError as err:
        print("Not activated")
        raise SystemExit(err)

def close():
    transcriber.sendall("DISC".encode())
    transcriber.close()
    print("Tapp closed")
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
        print("Tapp something went wrong 0900")
        while True:
            pass

    print("Tapp connected")
    return

def deactivate():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/deactivate', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            print("Deactivated")
            return
    except requests.exceptions.HTTPError as err:
        print("Not deactivated")
        raise SystemExit(err)

def getMacAddress():
    return ':'.join(re.findall('..', '%012x' % getnode()))

def setup():
    connect()
    activate()

    print("Tapp setup finished")
    return

def startStream():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/startStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            print("Streaming")
            return
    except requests.exceptions.HTTPError as err:
        print("Not streaming")
        raise SystemExit(err)

def stopStream():
    try:
        response = requests.get('http://' + HOST + '/api/v1/transcriber/stopStream', headers={
            'x-macaddress': getMacAddress(),
            'x-apikey': API_KEY
        })

        if response.status_code == 200:
            print("Stop streaming")
            return
    except requests.exceptions.HTTPError as err:
        print("Not stop streaming")
        raise SystemExit(err)
