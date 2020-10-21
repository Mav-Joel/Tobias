#!/usr/bin/env python3
#-*-coding:utf-8-*-
"""Importation base de donnée"""
import mysql
import mysql.connector
import paramiko

import os
import sys
import time
import subprocess
import csv
import gi
import nmap
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from Bibliotheque.TBook import Tools

Utilisateur=os.environ["USER"]
MagicWord = Tools().getModuleData("local dbpassword","Tobias")

from Bibliotheque.NBook import Network
from Bibliotheque.DBook import Database

def Multi_Task_PCs(Programme,Ip,Pc):
        
    print("Multitasking ongoing")
    #Envoi du fichier de contrôle / Envoi du programme dans le fichier de contrôle
    os.system("scp -r /home/joel/Archétype/Tobito/Multi_Task_Pcs {}:~/".format(Pc)) 

    os.system("scp {} {}:/home/joel/Multi_Task_Pcs ".format(Programme,Pc))

    # Executer le programme
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(Ip,port=22 ,username='joel',password="notmypassword")
    stdin,stdout,stderr=ssh.exec_command("chmod u+x ~/Multi_Task_Pcs/* | ~/Multi_Task_Pcs/* >> ~/Multi_Task_Pcs/Rapport/Result")
    output= stdout.readlines()
    print( "\n".join(output))

    os.system("scp {}:~/Multi_Task_Pcs/Rapport/Result /home/joel/Archétype/Tobito/Multi_Task_Pcs/Rapport ".format(Pc))

class Ally_Computers():
    
    def customRecup(self):
        registredComps=[]

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command = mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute("SELECT Information FROM systeme WHERE Programme='Ally_Computer'")

        for x in Command:
            for lettre in x :
                registredComps.append(lettre)

        return registredComps

    def currentSsh(self):

        currentSshList=[]
        numPcs=subprocess.getoutput("ps -elf | egrep 'ssh' | egrep '@[0-9]' | awk '{print $16}' | sed -re \"s/[a-z]//g\" | sed -re \"s/[A-Z]//g\" | sed -re \"s/@//g\" | wc -l")
        for i in range(1,int(numPcs)+1):
            Pcs=subprocess.getoutput("ps -elf | egrep 'ssh' | egrep '@[0-9]' | awk '{print $16}' | sed -re \"s/[a-z]//g\" | sed -re \"s/[A-Z]//g\" | sed -re \"s/@//g\"|head -n"+str(i)+" | tail -n1")
            currentSshList.append(Pcs)
        return currentSshList


    def Main(self):

        a=self.customRecup()
        b=self.currentSsh()
        toStock=set(b)-set(a)

        list_of_strings = [str(s) for s in toStock]
        joined_string = " ".join(list_of_strings)


        if joined_string == "" :
            pass
        else : 
            Stocker(joined_string,"Ally_Computer","systeme")
       
        if self.customRecup() == "" :
            pass
        else :

            try :
            
                #checker()
                mydb = mysql.connector.connect(
                host="localhost",
                user="Python",
                passwd=self.MagicWord,
                )

                Command = mydb.cursor()
                Command.execute("USE tobiasdb")
                Command.execute("SELECT Information FROM systeme WHERE Programme='Ally_Computer' AND Information !='127.0.0.1'")

                for x in Command:
                    for lettre in x :

                        ssh=paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(lettre,port=22 ,username='joel',password=self.MagicWord)
                        Notification("La machine avec l'IP "+lettre+" est allumé")
                        time.sleep(1)

            except paramiko.ssh_exception.NoValidConnectionsError :
                print("[-] Connexion Impossible : \n"   +Recup("systeme","Ally_Computer")+" est hors d'atteinte")
                print("Pas de connexion Internet")

            except paramiko.ssh_exception.AuthenticationException :
                print("Mot de passe incorrect")
                print("\n")

            except OSError :
                print("[-] Connexion Impossible : \n"+Recup("systeme","Ally_Computer")+" est hors d'atteinte")

            except paramiko.ssh_exception.SSHException :
                print("Erreur")

            time.sleep(1)
    
class internetProtocol():

    #Renvoi les hôtes actuellement connectés sur le réseau
    def getCurrentNetworkHostsFromDB(self):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )
        
       # MsgSystem("Getting Current Network Hosts from DB","...")
        
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT Information FROM reseau WHERE Network='currentNetworkHosts'")
        for x in Command:
            for result in x :
                return result


    def findCurrentHosts(self):
        
        #MsgSystem("Finding Current Hosts","...")

        nm = nmap.PortScanner()
        nm.scan(hosts=Network.monIPMask(), arguments='-n -sP -PE -PA21,23,80,3389') #Nouveau arguments
        hosts_list = nm.all_hosts()
        return hosts_list #Return a List 


    def getKnownNames(self,name):

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        MsgSystem("Finding the name of the recently connected IP","...")

        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT nom FROM knownIps WHERE adresse='"+name+"'")
        for x in Command:
                for lettre in x :
                        return str(lettre)
    
    def rule(self,option): 
        toDoIfConnected = []
        toDoIfDisconnected = []

        with open("/home/joel/Archétype/Tobi/Admin/Network.csv","r") as csvFile :
            csvContent = csv.reader(csvFile)
            next(csvContent)
            for lines in csvContent :
                address = lines[0]

                state = lines[1]

                action = lines[2]

                if state == "CONNECTED" : 
                    toDoIfConnected.append(address)
                    toDoIfConnected.append(action)
                else : 
                    toDoIfDisconnected.append(address)
                    toDoIfDisconnected.append(action)
        
        if option == "CONNECTED": 
            return toDoIfConnected
        elif option == "DISCONNECTED": 
            return toDoIfDisconnected
        else : 
            raise Exception("Not supposed to happen")


    def Main(self):
        List = []

        #DECL

        currentNetworkHosts = self.findCurrentHosts()
        registredNetworkHosts = self.getCurrentNetworkHostsFromDB()

        #MAIN
        if len(str(currentNetworkHosts)) > len(registredNetworkHosts):  #CONNEXIONS

            registredNetworkHosts = registredNetworkHosts.strip("[]")
            registredNetworkHosts = registredNetworkHosts.strip("\'")
            registredNetworkHosts = registredNetworkHosts.split("', '")

            a = set(currentNetworkHosts) - set(registredNetworkHosts)
            
            for _ in a : 
                List.append(_.strip("'"))
            
            for i in range(0,len(List)) : 
                if self.getKnownNames(List[i]) is None : 
                    print("{} est inconnue du système et s'est connectée".format(List[i]))
                   
                    recieved = self.rule("CONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Notification("{} viens de se connecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se connecter".format(recieved[x]))
                    
                    if Recup("reseau",List[i],"Information","Network") == "" :
                        Stocker(List[i],"Online","reseau","Network","Information")
                        
                        if Recup("unknownIps",List[i],"nom","adresse") is None :
                            Stocker(List[i],"Unknown","unknownIps","nom","adresse")
                        else : 
                            pass

                    else :
                        Update("Online",List[i],"reseau","Network","Information")
                        if Recup("unknownIps",List[i],"nom","adresse") is None :
                            Stocker(List[i],"Unknown","unknownIps","nom","adresse")
                        else : 
                            pass
                else : 
                      
                    recieved = self.rule("CONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Notification("{} viens de se connecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se connecter".format(recieved[x]))
                    
                    print("{} s'est connectée".format(self.getKnownNames(List[i])))
                    if Recup("reseau",List[i],"Information","Network") == "" :
                        Stocker(List[i],"Online","reseau","Network","Information")
                    else :
                        Update("Online",List[i],"reseau","Network","Information")
                        
                        if Recup("unknownIps",List[i],"nom","adresse") is None :
                            Stocker(List[i],"Unknown","unknownIps","nom","adresse")
                        else : 
                            pass
            
            if len(a) > 1 :                  
                print("{} personnes se sont connectées".format(len(List)))
            elif len(a) == 0: 
                pass
            else : 
                print("{} personne s'est connectée".format(len(List)))

            mydb = mysql.connector.connect(
            host="localhost",
            user="Python",
            passwd=self.MagicWord,
            )

            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 

            Ins="UPDATE reseau SET Information=\"{}\" WHERE Network='currentNetworkHosts'".format(str(currentNetworkHosts))
            Command.execute(Ins)
            mydb.commit()

        elif len(str(currentNetworkHosts)) == len(registredNetworkHosts): 
            pass
            
        else : #DECONNEXIONS

            registredNetworkHosts = registredNetworkHosts.strip("[]")
            registredNetworkHosts = registredNetworkHosts.strip("\'")
            registredNetworkHosts = registredNetworkHosts.split("', '")

            a = set(registredNetworkHosts) - set(currentNetworkHosts)

            for _ in a : 
                List.append(_.strip("'"))
            
            
            for i in range(0,len(List)) : 
                if self.getKnownNames(List[i]) is None : 
                    print("{} est inconnue du système et s'est déconnecté".format(List[i]))
                      
                    recieved = self.rule("DISCONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Notification("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TALK":
                                talktoMe("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se déconnecter".format(recieved[x]))
                    
                    if Recup("reseau",List[i],"Network","Information") == "" :
                        Stocker(List[i],"OffLine","reseau","Network","Information")
                    else :
                        Update("OffLine",List[i],"reseau","Network","Information")
                        
                        if Recup("unknownIps",List[i],"nom","adresse") is None :
                            Stocker(List[i],"Unknown","unknownIps","nom","adresse")
                        else : 
                            pass


                else : 

                    recieved = self.rule("DISCONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Notification("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TALK":
                                talktoMe("{} viens de se déconnecter".format(recieved[x]))
                        
                    print("{} s'est déconnecté".format(self.getKnownNames(List[i])))

                    if Recup("reseau",List[i],"Network","Information") == "" :
                        Stocker(List[i],"OffLine","reseau","Network","Information")
                    else :
                        Update("OffLine",List[i],"reseau","Network","Information")
            if len(a) > 1 :                  
                print("{} personnes se sont déconnectés".format(len(List)))
            elif len(a) == 0: 
                pass
            else : 
                print("{} personne s'est déconnectée".format(len(List)))

            print(currentNetworkHosts)
            mydb = mysql.connector.connect(
            host="localhost",
            user="Python",
            passwd=self.MagicWord,
            )

            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 

            Ins="UPDATE reseau SET Information=\"{}\" WHERE Network='currentNetworkHosts'".format(str(currentNetworkHosts))
            Command.execute(Ins)
            mydb.commit()
