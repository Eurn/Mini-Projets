#!/usr/bin/env python3
import socket
import sys
class udpserveur():

    def __init__(self):
        self.port=int(sys.argv[1])
        self.ip=""
        self.buff = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.socket.bind((self.ip, self.port))

    def repondre(self):
        while True:
            data, addr = self.socket.recvfrom(self.buff) # buffer size is 1024 bytes
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1]))
            print ('ok:', data.decode("utf-8")+'')
            self.socket.sendto(bytes(""+data.decode("utf-8"),'utf-8'),addr)




serverTest=udpserveur();

serverTest.repondre();