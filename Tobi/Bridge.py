#!/usr/bin/env python3
#-*-coding:utf-8-*-
from Bibliotheque.NBook import Network
import socket 

class Bridge():

    def message(self):

        host, port = ('192.168.1.31',5566) # Même port que Hiden

        try :
            prise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Indispensable
            prise.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            prise.connect((host,port))
            
            # data=Network().myIp("ip")
            data="close"
            data=data.encode("utf8")
            prise.sendall(data)
            prise.close()

        except :
            raise Exception("Failed to Contact MyBerry")

# Bridge().message()