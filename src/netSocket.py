from os import getenv
from socket import AF_INET, socket, SOCK_STREAM
from uuid import getnode

import re

HOST = getenv('TAPP_HOST')
PORT = int(getenv('TAPP_PORT'))

clientSocket = socket(AF_INET, SOCK_STREAM)

def connect():
    clientSocket.connect((HOST, PORT))

    mac = getMacAddress()
    if mac != getMacAddress(): return
    clientSocket.sendall(mac.encode('utf-8'))

def getMacAddress() -> str:
    return ':'.join(re.findall('..', '%012x' % getnode()))

connect()