#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket, binascii, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
host = 'botsy'
port = 3000
sock.connect((host,port))
print "connected"

while 1:
	sock.send("getbuttons\n")
	data = sock.recv(2048)
	print binascii.hexlify(data)
	time.sleep(1)
