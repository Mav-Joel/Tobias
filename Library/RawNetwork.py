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
import nmap
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.TBook import Tools

Utilisateur=os.environ["USER"]
MagicWord = Tools().getModuleData("localDbPassword","Tobias")

from Library.NBook import Network
from Library.DBook import Database
currentPc=subprocess.getoutput("hostname")

def Multi_Task_PCs(Programme,Ip,Pc):
        
    print("Multitasking ongoing")
    #Envoi du fichier de contrôle / Envoi du programme dans le fichier de contrôle
    os.system("scp -r /Users/{}/Archetype/Tobito/Multi_Task_Pcs {}:~/".format(Utilisateur,Pc)) 

    os.system("scp {} {}:/Users/{}/Multi_Task_Pcs ".format(Programme,Pc,Utilisateur))

    # Executer le programme
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(Ip,port=22 ,username='joel',password="GrpAmPMaverick&")
    stdin,stdout,stderr=ssh.exec_command("chmod u+x ~/Multi_Task_Pcs/* | ~/Multi_Task_Pcs/* >> ~/Multi_Task_Pcs/Rapport/Result")
    output= stdout.readlines()
    print( "\n".join(output))

    os.system("scp {}:~/Multi_Task_Pcs/Rapport/Result /Users/{}/Archetype/Tobito/Multi_Task_Pcs/Rapport ".format(Pc,Utilisateur))

class Ally_Computers():
    def __init__(self):
        self.MagicWord = Tools().getModuleData("localDbPassword","Tobias")
    
    def customRecup(self):
        registredComps=[]

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        Command = mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute(f"SELECT data FROM {currentPc} WHERE field='Ally_Computer'")

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
            Database(f"{currentPc}","id","name","field","data","NULL","RawNetworkA","Ally_Computer",joined_string).insertInDatabase()
        if self.customRecup() == "" :
            pass
        else :

            try :
            
                #checker()
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=self.MagicWord, port="8889",
                )

                Command = mydb.cursor()
                Command.execute("USE tobiasdb")
                Command.execute(f"SELECT data FROM {currentPc} WHERE field='Ally_Computer' AND data !='127.0.0.1'")

                for x in Command:
                    for lettre in x :

                        ssh=paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(lettre,port=22 ,username='joel',password=self.MagicWord)
                        Tools().Notification("La machine avec l'IP "+lettre+" est allumé")
                        time.sleep(1)

            except paramiko.ssh_exception.NoValidConnectionsError :
                print("[-] Connexion Impossible : \n"   +Database(f"{currentPc}","data","field","Ally_Computer").getFromDatabase()+" est hors d'atteinte")
                print("Pas de connexion Internet")

            except paramiko.ssh_exception.AuthenticationException :
                print("Mot de passe incorrect")
                print("\n")

            except OSError :
                print("[-] Connexion Impossible : \n"+Database(f"{currentPc}","data","field","Ally_Computer").getFromDatabase()+" est hors d'atteinte")

            except paramiko.ssh_exception.SSHException :
                print("Erreur")

            time.sleep(1)
    
class internetProtocol():
    def __init__(self):
        self.MagicWord = Tools().getModuleData("localDbPassword","Tobias")
        self.networkCSV = Database().getPaths('path','NetworkCSV')

    #Renvoi les hôtes actuellement connectés sur le réseau
    def getCurrentNetworkHostsFromDB(self):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )
        
       # MsgSystem("Getting Current Network Hosts from DB","...")
        
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT Information FROM reseau WHERE Nature='currentNetworkHosts'")
        for x in Command:
            for result in x :
                return result


    def findCurrentHosts(self):
        
        #MsgSystem("Finding Current Hosts","...")

        nm = nmap.PortScanner()
        nm.scan(hosts=Network().myIp("mask"), arguments='-n -sP -PE -PA21,23,80,3389') #Nouveau arguments
        hosts_list = nm.all_hosts()
        return hosts_list #Return a List 


    def getKnownNames(self,name):

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        Tools().MsgSystem("Finding the name of the recently connected IP","...")

        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT hostname FROM knownIps WHERE address='"+name+"'")
        for x in Command:
                for lettre in x :
                        return str(lettre)
    
    def rule(self,option): 
        toDoIfConnected = []
        toDoIfDisconnected = []

        with open(self.networkCSV,"r") as csvFile :
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
                    Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{List[i]} est inconnue est actuellement connectée").insertInDatabase()
                    Database("unknownIps","id","address","NULL",f"{List[i]}").insertInDatabase()
                   
                    recieved = self.rule("CONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Tools().Notification("{} viens de se connecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se connecter".format(recieved[x]))
                            if action == "TALK":
                                Tools().talktoMe("{} just connected".format(recieved[x]))
                          
                    if Database("reseau","Nature","Information",List[i]).getFromDatabase() == "" :
                        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"RawNetwork","Online",List[i]).insertInDatabase()
                        

                    else :
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",  
                        passwd=self.MagicWord, port="8889",
                        )

                        Command = mydb.cursor() 
                        Command.execute("USE tobiasdb") 
                        Ins=f"UPDATE reseau SET Nature='Online' WHERE Information='{List[i]}' AND Nature!='currentIp' AND Nature!='previousIp'"
                        Command.execute(Ins)
                        mydb.commit()

                    if Database("unknownIps","address","address",List[i]).getFromDatabase() is None :
                        Database("unknownIps","id","address","NULL",List[i]).insertInDatabase()
                    else : 
                        pass
                else : 
                      
                    recieved = self.rule("CONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Tools().Notification(f"{self.getKnownNames(List[i])} viens de se connecter")
                            if action == "TELL":
                                print(f"{self.getKnownNames(List[i])} viens de se connecter")
                            if action == "TALK":
                                Tools().talktoMe(f"{self.getKnownNames(List[i])} just connected")
                          
                    Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{List[i]} est connectée").insertInDatabase()
                    if Database("reseau","Nature","Information",List[i]).getFromDatabase() == "" :
                        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"RawNetwork","Online",List[i]).insertInDatabase()
                    else :
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",  
                        passwd=self.MagicWord, port="8889",
                        )
                        
                        Command = mydb.cursor() 
                        Command.execute("USE tobiasdb") 
                        Ins=f"UPDATE reseau SET Nature='Online' WHERE Information='{List[i]}' AND Nature!='currentIp' AND Nature!='previousIp'"
                        Command.execute(Ins)
                        mydb.commit()
                        
                    if Database("unknownIps","address","address",List[i]).getFromDatabase() is None :
                        Database("id","address","NULL",List[i]).insertInDatabase()
                    else : 
                        pass
            
            if len(a) > 1 :                  
                Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{len(List)} computers connected from last sweap").insertInDatabase()

            elif len(a) == 0: 
                pass
            else : 
                Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{len(List)} computers connected from last sweap").insertInDatabase()

            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=self.MagicWord, port="8889",
            )

            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 

            Ins="UPDATE reseau SET Information=\"{}\" WHERE Nature='currentNetworkHosts'".format(str(currentNetworkHosts))
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
                    Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{List[i]} est inconnue est actuellement disconnected").insertInDatabase()
                    Database("unknownIps","id","address","NULL",f"{List[i]}").insertInDatabase()
                
                    recieved = self.rule("DISCONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Tools().Notification("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TALK":
                                Tools().talktoMe("{} viens de se déconnecter".format(recieved[x]))
                            if action == "TELL":
                                print("{} viens de se déconnecter".format(recieved[x]))
                    
                    if Database("reseau","Nature","Information",List[i]).getFromDatabase() == "" :
                        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"RawNetwork","Offline",List[i]).insertInDatabase()
                  
                    else :
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",  
                        passwd=self.MagicWord, port="8889",
                        )
                        
                        Command = mydb.cursor() 
                        Command.execute("USE tobiasdb") 
                        Ins=f"UPDATE reseau SET Nature='Offline' WHERE Information='{List[i]}' AND Nature!='currentIp' AND Nature!='previousIp'"
                        Command.execute(Ins)
                        mydb.commit()
                        


                else : 

                    recieved = self.rule("DISCONNECTED")
                    for x in range(0,len(recieved)) : 
                        if List[i] == recieved[x] : 
                            action = recieved[x+1]
                            if action == "NOTIFY":
                                Tools().Notification(f"{self.getKnownNames(List[i])} viens de se déconnecter")
                            if action == "TELL":
                                print(f"{self.getKnownNames(List[i])} viens de se déconnecter")
                            if action == "TALK":
                                Tools().talktoMe(f"{self.getKnownNames(List[i])} viens de se déconnecter")
                        
                    Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{List[i]} est actuellement disconnected").insertInDatabase()

                    if Database("reseau","Nature","Information",List[i]).getFromDatabase() == "" :
                        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"RawNetwork","Offline",List[i]).insertInDatabase()
                  
                    else :
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",  
                        passwd=self.MagicWord, port="8889",
                        )
                        
                        Command = mydb.cursor() 
                        Command.execute("USE tobiasdb") 
                        Ins=f"UPDATE reseau SET Nature='Offline' WHERE Information='{List[i]}' AND Nature!='currentIp' AND Nature!='previousIp'"
                        Command.execute(Ins)
                        mydb.commit()

            if len(a) > 1 :                  
                print("{} computers disconnected from last sweap".format(len(List)))
            elif len(a) == 0: 
                pass
            else : 
                Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{len(List)} computers disconnected from last sweap").insertInDatabase()

            Tools().Rapport(f'currentNetworkHosts')
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=self.MagicWord, port="8889",
            )

            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 

            Ins="UPDATE reseau SET Information=\"{}\" WHERE Nature='currentNetworkHosts'".format(str(currentNetworkHosts))
            Command.execute(Ins)
            mydb.commit()
