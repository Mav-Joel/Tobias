#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël

from threading import Thread
import threading
import time
import socket 

class Hiden():

    def threadHote(self):
        mon_thread=threading.Thread(target=self.hote)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre

    def threadMsg(self):
        mon_thread=threading.Thread(target=self.message)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre

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
         
    def message(self):

        while True :

            host, port = ('127.0.0.1',8081) # Même port que Hiden

            try :
                prise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Indispensable
                # prise.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
                prise.connect((host,port))
                
                data=input("Dire : \n")
                data=data.encode("utf8")
                prise.sendall(data)

                
            except :
                pass
               

Hiden().threadHote()
Hiden().threadMsg()