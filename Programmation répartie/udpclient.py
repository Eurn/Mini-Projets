#!/usr/bin/env python3
import socket
import sys
class udpclient():
    """ Ici, le constructeur du client affecte les différentes variables au client"""
    def __init__(self,adresseDest,port):
        self.port=int(sys.argv[2])
        self.buff = 1024
        self.ip=sys.argv[3]; # On diffuse en broadcast afin de contacter tous les serveurs qui écoute au même port.
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP





    def envoyerMessage(self):
        """Ici, le client envois le paquet avec le message rentrée en paramètre lors de l'éxécution du fichier , au port renseigné également lors de l'éxécution du fichier"""
        self.socket.sendto(bytes(sys.argv[1] ,'utf8'), (self.ip, self.port))



    def recevoirMessage(self):
        """ Ici, on va faire une boucle qui va attendre 10 sec à chaque demande de récéption de réponses afin de voir s'il reste encore des serveurs qui ont répondu ou souhaitent répondre. Au bout de 10 sec, si aucun server n'a répondu
        la fonction s'arrête et la communication s'achève"""

        rep=True
        while rep == True:

            try:

                self.socket.settimeout(5)
                data =self.socket.recv(self.buff)
                print('"ok:', data.decode("utf-8")+'"')
            except socket.timeout:
                print("Plus de réponse")
                rep = False;


clientTest=udpclient("127.0.0.1",20002);   #On crée un client qui va effectuer l'envois et la récéption des messages.
clientTest.envoyerMessage();
clientTest.recevoirMessage();
print("Communcation achevée")