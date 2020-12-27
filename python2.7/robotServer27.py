#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi
import argparse
import socket
import sys
from balla import balla
from saluta import saluta

parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, default="127.0.0.1",
                    help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
parser.add_argument("--port", type=int, default=9559,
                    help="Naoqi port number")

args = parser.parse_args()
session = qi.Session()
try:
    session.connect("tcp://" + args.ip + ":" + str(args.port))
except RuntimeError:
    print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port))
    print("Please check your script arguments. Run with -h option for help.")
    sys.exit(1)

posture_service = session.service("ALRobotPosture")
posture_service.goToPosture("StandInit", 1.0)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data   
        cmd = connection.recv(3)
        print('received "%s"' % cmd)

    finally:
        # Clean up the connection
        connection.close()

    if cmd == 'sit':
        posture_service.goToPosture("Sit", 1.0)
    elif cmd == 'sta':
        posture_service.goToPosture("Stand", 1.0)
    elif cmd == 'cro':
        posture_service.goToPosture("Crouch", 1.0)
    elif cmd == 'bal':
        posture_service.goToPosture("Stand", 1.0)
        balla()
    elif cmd == 'sal':
        posture_service.goToPosture("Stand", 1.0)
        saluta()

    print(posture_service.getPostureFamily())
