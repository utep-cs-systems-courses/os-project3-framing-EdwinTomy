#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, time
import archiver
import threading

host = "127.0.0.1"  # Symbolic name meaning all available interfaces
port = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)  # allow only one outstanding request
# s is a factory for connected sockets


def request_handler():
    print('Connected by', address)
    byte_arr = archiver.archive(["francesco.txt", "sasageyo.txt"])
    conn.send(byte_arr)
    conn.shutdown(socket.SHUT_WR)


while True:
    conn, address = s.accept()  # wait until incoming connection request (and accept it)
    thread = threading.Thread(target=request_handler, args=())
    thread.start()







