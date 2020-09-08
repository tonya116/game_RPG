# -*- coding: utf-8 -*-

import socket, time
from config import *
import generate_all as ga





clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

quit = False
print("[ Server Started ]")

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:
		print("\n[ Server Stopped ]")
		quit = True

s.close()


"""

s = socket.socket()

s.bind(("", port))
s.listen(1)
c, a = s.accept()



print("connected", a)

while True:

    data = c.recv(1024)
    if not data:
        break

    name_of_hero = str(data)
    #ga.regenerate()
    print(ga.list_of_all)
    c.send(b"lol)
"""
