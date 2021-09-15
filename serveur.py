#!/usr/bin/python3
# -*-coding:Utf-8 -*

import socket


#construction socket
connexion= socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#Connexion de la socket
connexion.bind(('', 1025))



#Faire écouter la socket
connexion.listen(5)


#Accepter des clients

ConnexionClient, infosConnex = connexion.accept()
