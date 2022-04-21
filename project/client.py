#! /usr/bin/env python3

# Echo client program
import socket, sys, re, time
import archiver

sys.path.append("../lib")  # for params
import params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--delay'), 'delay', "0"),
    (('-?', '--usage'), "usage", False),  # boolean (set if present)
)

progName = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    server_host, server_port = re.split(":", server)
    server_port = int(server_port)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(server_host, server_port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, sock_type, proto, canon_name, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, sock_type, proto))
        s = socket.socket(af, sock_type, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

delay = float(paramMap['delay'])  # delay before reading (default = 0s)
if delay != 0:
    print(f"sleeping for {delay}s")
    time.sleep(int(delay))
    print("done sleeping")

while 1:
    byte_arr = s.recv(1024)
    print("Hello")
    print(byte_arr)
    print("Received")
    if len(byte_arr) == 0:
        break
    archiver.unarchive(byte_arr, "client1")
print("Zero length read.  Closing")
s.close()
