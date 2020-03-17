#!/usr/bin/env python3
import socket
import sys
class tcpclient():

    def __init__(self):

            self.port = int(sys.argv[2])
            self.ip = sys.argv[3]
            self.buff = 1024
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            


    def envoyerMessage(self):
        self.socket.connect((self.ip,self.port)) 
        self.socket.send(bytes(sys.argv[1] ,'utf8'))


    def recevoirMessage(self):
        rep=True
        while rep == True:
            try:      
                self.socket.settimeout(5)
                data, addr =self.socket.recvfrom(self.buff)
                print('"ok:', data.decode("utf-8")+'"')
            except socket.timeout:
                print("Plus de réponse")
                rep = False;
                self.socket.close()


clientTest = tcpclient() 
clientTest.envoyerMessage()
clientTest.recevoirMessage()
