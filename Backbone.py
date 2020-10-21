#!/usr/bin/env python3
#-*-coding:utf-8-*-
"""Native importations"""
import os
import sys
import subprocess
import time
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import mysql
import mysql.connector
import nmap
import json
"""Personnal importations"""

from Bibliotheque.NBook import Network
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database

#Init

"""Enregistrement des ports ouverts"""
class Backbone():
    def __init__(self):
        self.MagicWord = self.getModuleData("local dbpassword","Tobias")

    
    def getModuleData(self,searchingFor,fieldName='user'):
        with open("/home/joel/Archétype/Tobi/Admin/Configurations.json","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def getMyPorts(self,ip):

        """Get the open ports on the current computer"""

        currentPc=subprocess.getoutput("hostname")

        nm = nmap.PortScanner()
        nm.scan(ip, '1-1024')
        for host in nm.all_hosts(): 
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    Database(f"{currentPc}","id","name","field","data","NULL","openPorts","Hardware",f"{port}").insertInDatabase()

    """Surveillance des ports """

    # Run an ip test on myIp to compare it with the port scan I performed earlier

    def ipScan(self,ip):

        """Gestion des ports """
        portListe=[]
        dbListe=[]
        currentPc=subprocess.getoutput("hostname")

        """Myslq DB opening """

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT Information FROM reseau WHERE Network='Blade'")
    
        nm = nmap.PortScanner()
        nm.scan(ip, '1-1024')

        for host in nm.all_hosts(): 
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()  
                for port in lport:
                    portListe.append(port)

                    for x in Command:
                        for lettre in x :
                            dbListe.append(lettre)

        if len(portListe) == len(dbListe): 
            for i in range(0,len(dbListe)) :
                if portListe[i] == dbListe[i]:
                    pass

        elif len(portListe) > len(dbListe):
            
            answer = input("[+] The port "+str(set(portListe) - set(dbListe))+" Just opened , what do you want to do with it [drop/accept]? \n")
            
            if answer == "drop":
                openPorts=set(portListe) - set(dbListe)
            
                list_of_strings = [str(s) for s in openPorts]
                joined_string = " ".join(list_of_strings)

                os.system("/home/joel/Archétype/sysCommands/iptableHandler.bash Backbone {} ".format(joined_string))
            
            elif answer == "accept":
            
                Command = mydb.cursor() 
                Command.execute("USE tobiasdb") 
                sql = "DELETE FROM reseau WHERE Network = 'Blade'"
                Command.execute(sql)
                mydb.commit()

                nm = nmap.PortScanner()
                nm.scan(ip, '1-1024')
                for host in nm.all_hosts(): 
                    portListe=[]
                    for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        for port in lport:      
                            Database(f"{currentPc}","id","name","field","data","NULL","openPorts","Hardware",f"{port}").insertInDatabase()

                print("Updated")

            else :
                print("Wrong answer")
                print(answer)

        elif len(portListe) < len(dbListe):
            answer = print("The port : "+str(set(dbListe) - set(portListe))+" Just closed")
            
            nm = nmap.PortScanner()
            nm.scan(ip, '1-1024')
            for host in nm.all_hosts(): 
                portListe=[]
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:      
                        Database(f"{currentPc}","data",f"{port}","name","openPorts").updateValue()

                print("Updated")


        mydb.close()
                                                    
                

    """Network Space"""

    def networkSpace(self):

        myIp = Network.Mon_IP() #Méthode Provenant de NBook
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT Information FROM reseau WHERE Network='Blade'")

        previousIp=Recup("reseau","previousIp","Information","Network")
    
        if myIp == previousIp :
            pass 
    
        else :

            Notification("Vous avez changé d'espace Réseau")
            print("You have changed of Network Space")

            Update(str(myIp),"currentIp","reseau","Information","Network") 
            Update(str(myIp),"previousIp","reseau","Information","Network")
            
            Network.Reseau(myIp)
        

    def F_Nombre_Utilisateurs_Actuels(self):
        """Surveillance ssh """


        Nombre_Utilisateurs_Actuels=subprocess.getoutput("ss | egrep -i ssh |sort -u | uniq| wc -l")
        Nombre_Utilisateurs_Actuels=int(Nombre_Utilisateurs_Actuels)

        if Nombre_Utilisateurs_Actuels >= 1 :

            Nombre_Utilisateurs_Actuels=int(Nombre_Utilisateurs_Actuels)

        else :

            Nombre_Utilisateurs_Actuels=0
        return Nombre_Utilisateurs_Actuels



    def Liste_Autorisée(self):

        Liste_IP=Recup("backbone","Allowed","adresseIp","Statut")
        Liste_IP = Liste_IP.split()

        return Liste_IP

   
    def ipActuelles(self):
        
        adresseIp_Stage1=[]

        tail=1
        l=Backbone.F_Nombre_Utilisateurs_Actuels()
        tail=str(tail)
        o=0
        while o != l :

            a=subprocess.getoutput("ss | egrep -i ssh |sort -u | uniq| tail -n"+str(tail)+"|head -n1|uniq|awk '{print $6}'|sed -re \"s/:.+//g\"")
            adresseIp_Stage1.append(a)
            o=o+1
            tail=int(tail)
            tail=tail+1

        return adresseIp_Stage1

    def Comparaison(self):


        Nombre_Utilisateurs_Actuels=Backbone.F_Nombre_Utilisateurs_Actuels()
        p=Backbone.ipActuelles()
        m=Backbone.Liste_Autorisée()

        correct = 0
        trueList=[]
      
        for i in range(0,len(p)):
            for k in range(0,len(Backbone.Liste_Autorisée())):
                if p[i] == m[k]:
                    correct=correct+1
                    if correct >= 1 :
                        trueList.append(p[i])

                    else : 
                        pass

                else : 
                    pass
        
        badssh=list(set(p) - set(trueList))
        

        for h in range(0,len(badssh)):
            
            pts=subprocess.getoutput("who | egrep '"+badssh[h]+"' | sort -u | uniq | awk '{print $2}' ")

            a=subprocess.getoutput("ps -aux | egrep 'sshd:' | egrep 'joel@'"+str(pts)+"|awk '{print $2}' | xargs kill ")

            Notification(" Tentative de connexion non approuvé en cours")
            print("Denied Access")
            Database("backbone","id","statut","ipAddress","NULL","Unallowed",f"{badssh[h]}").insertInDatabase()


def Etapes_de_Fonctionnement():

    Backbone.F_Nombre_Utilisateurs_Actuels()
    Backbone.ipActuelles()
    Backbone.Comparaison()

# #Body////////////////////////////////////////////////!
# #unittest.main()