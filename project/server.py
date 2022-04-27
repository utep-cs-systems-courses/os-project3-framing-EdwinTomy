#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, time
import archiver
import threading

sys.path.append("../lib")       # for params
import params

# Declaring vars for proxy
switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "framingServer"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

# Creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(5)              # allow five outstanding requests


def request_handler(conn, address):
    print('Connected by', address)
    byte_arr = conn.recv(1024)
    archiver.unarchive(byte_arr, "new")
    conn.send("Files received".encode())
    conn.shutdown(socket.SHUT_WR)


count = 0
while count < 5:
    conn, address = s.accept()  # wait until incoming connection request (and accept it)
    thread = threading.Thread(target=request_handler, args=(conn,address,))
    thread.start()
    count += 1







