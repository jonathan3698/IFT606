#! /usr/bin/env python3
"""
import subprocess

print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
HARDCODED - through ifconfig, need to figure out local adress/mask
nmapOutput = subprocess.check_output(["nmap", "-p", "22", "10.44.88.*"])
nmapOutput = subprocess.check_output(["nmap", "-p", "22", "-oG", "-", "192.168.0.*"])
nmapOutput = nmapOutput.decode("utf-8")
listedNmapString = list(filter(lambda x: "open" in x, nmapOutput.splitlines()))

for entry in listedNmapString:
    ip = entry.split()[1]
    print(ip)"""

import socket

host = socket.gethostname()
dataDecoded = None
errorOccured = False

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketClient:
		socketClient.connect((host, 50000))
		socketClient.sendall('I'.encode('utf-8'))
		data = socketClient.recv(1024)
		dataDecoded = data.decode('utf-8')
except:
	errorOccured = True

if not errorOccured:
	if dataDecoded != 'OK':
		print('ErrorOccured = false, dataDecoded =/= OK')
		#Try to infect machine here
	else:
		print('ErreurOccured = false, dataDecoded = OK')
else:
	print('ErrorOccured = true')