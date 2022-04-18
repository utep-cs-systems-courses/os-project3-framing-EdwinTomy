#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, time
import archiver
sys.path.append("../lib")       # for params
import params


switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50002),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

while True:
    conn, addr = s.accept() # wait until incoming connection request (and accept it)
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        byte_arr = archiver.files_to_bytes(["fiesta_salsa.txt"])
        conn.send(byte_arr)
        conn.shutdown(socket.SHUT_WR)

