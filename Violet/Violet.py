#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket    
from bs4 import BeautifulSoup
import requests

class Servs:

    def __init__(self):
        ip = self.getMyPublicIp()

    def getMyPublicIp(self):
        url = "https://www.monippublique.com/"

        session = requests.session()
        website = session.post(url)

        soup = BeautifulSoup(website.text, 'lxml')
        div = soup.find('span', {'class' : 'big-green'})
        return div.text
    
    def hote(self):

        host,port = ('',5566)
        prise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        prise.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
        prise.bind((host,port)) #Associer à Adresse IP
        print("Le serveur est initialisé")

        while True :

            prise.listen(10) #Lier à port défini dans le tuple plus haut
            connexion, address = prise.accept()

            data = connexion.recv(1024) #Recevoir une donnée
            data = data.decode("utf8")
            print("Recieved : "+data)
            print(connexion)
         

#EXECUTE
Server = Servs()
Server.hote()