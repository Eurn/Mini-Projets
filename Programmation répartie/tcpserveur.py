#!/usr/bin/env python3
import socket
import sys
class tcpserveur():

    def __init__(self):

        self.ip = ""
        self.port = int(sys.argv[1])
        self.buff = 20
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip,self.port))
        self.socket.listen(1)


    def repondre(self):

        
        while 1 :
            connect, addr = self.socket.accept()
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1]))
            data = connect.recv(self.buff)
            if not data: break
            print('ok:', data.decode("utf-8")+'')
            connect.send(data)
        connect.close()


serverTest=tcpserveur();

serverTest.repondre();