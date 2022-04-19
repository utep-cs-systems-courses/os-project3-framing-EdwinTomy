#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, time
import archiver

sys.path.append("../lib")  # for params
import params, threading

switchesVarDefaults = (
    (('-l', '--listenPort'), 'listenPort', 50001),
    (('-?', '--usage'), "usage", False),  # boolean (set if present)
)

progName = "echoServer"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddress = ''  # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddress, listenPort))
s.listen(1)  # allow only one outstanding request
# s is a factory for connected sockets


def request_handler():
    print('Connected by', address)
    byte_arr = archiver.files_to_bytes(["francesco.txt", "sasageyo.txt"])
    conn.send(byte_arr)
    conn.shutdown(socket.SHUT_WR)


while True:
    conn, address = s.accept()  # wait until incoming connection request (and accept it)
    thread = threading.Thread(target=request_handler, args=())
    thread.start()
