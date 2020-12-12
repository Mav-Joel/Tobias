#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël

from threading import Thread
import threading
import time

class Nedih():

    def threadHote(self):
        mon_thread=threading.Thread(target=self.hote)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre

    def threadMsg(self):
        mon_thread=threading.Thread(target=self.message)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre

    def hote(self):

        import socket

        host,port = ('',5569)
        socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.bind((host,port)) #Associer à Adresse IP
        print("Le serveur est initialisé")

        while True :

            self.threadMsg()
            socket.listen(2) #Lier à port défini dans le tuple plus haut
            connexion, address = socket.accept()

            data = connexion.recv(1024) #Recevoir une donnée
            data = data.decode("utf8")
            print("Recieved : "+data)
        
    def message(self):
        import socket

        while True :

            host, port = ('127.0.0.1',5568) # Même port que Hiden

            try :
                socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Indispensable
                socket.connect((host,port))
                
                data=input("Dire : \n")
                data=data.encode("utf8")
                socket.sendall(data)

                
            except :
                pass
                # print('Connexion échouée')
            
            time.sleep(5)

            

        
    
    def Main(self):
        self.threadHote()

if __name__ == "__main__":
    Nedih().Main()