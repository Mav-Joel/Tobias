#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import subprocess

import mysql
import mysql.connector
import nmap
Utilisateur=os.environ["USER"]

#---------------CUSTOM MODULES--------------------------
from Bibliotheque.NBook import Network
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database
#---------------END CUSTOM MODULES--------------------------

class Backbone():

    def __init__(self):
        
        #---------------DECL--------------------------
        self.MagicWord = Tools().getModuleData("local dbpassword","Tobias")
        self.monIp = Network().myIp("ip")
        self.portList = []
        #---------------END DECL--------------------------
        
        #---------------MYSQL DATABASE--------------------------
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="Python",
            passwd=self.MagicWord,
        )
        #---------------END MYSQL DATABASE--------------------------
  
    def getMyPorts(self):

        #---------------DECL--------------------------
        currentPc=subprocess.getoutput("hostname")
        #---------------END DECL--------------------------

        nm = nmap.PortScanner()
        nm.scan(self.monIp, '1-1024')
        for host in nm.all_hosts(): 
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    self.portList.append(port)

        #---------------CUSTOM METHODS--------------------------
        Database(f"{currentPc}","id","name","field","data","NULL","openPorts","Hardware",f"{self.portList}").insertInDatabase()
        #---------------END CUSTOM METHODS--------------------------

    def innerPortScan(self):

        #---------------DECL--------------------------
        self.portList=[]
        dbListe=[]
        currentPc=subprocess.getoutput("hostname")
        ip = self.monIp
        #---------------END DECL--------------------------

        #---------------MYSQL DATABASE--------------------------
        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"SELECT data FROM {currentPc} WHERE name='openPorts'")
        #---------------END MYSQL DATABASE--------------------------
    
        nm = nmap.PortScanner()
        nm.scan(ip, '1-1024')

        for host in nm.all_hosts(): 
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()  
                for port in lport:
                    self.portList.append(port)

        for x in Command:
            for lettre in x :
                pass
    
        lettre = lettre.strip("[]")
        lettre = lettre.strip("\'")
        lettre = lettre.split(", ")
        dbListe = lettre
        dbListe = [int(i) for i in dbListe if dbListe[0] != ""]
        
        if len(self.portList) == len(dbListe): 
            for i in range(0,len(dbListe)) :
                if self.portList[i] == dbListe[i]:
                    pass

        elif len(self.portList) > len(dbListe):
           
            rest = set(self.portList).difference(set(dbListe))
            answer = input(f"[+] The port {rest} Just opened , what do you want to do with it [drop/accept]? \n")
            
            if answer == "drop":

                openPorts = [str(s) for s in rest]
                strOpenPorts = " ".join(openPorts)

                os.system("/home/{}/Archetype/sysCommands/iptableHandler.bash Backbone {} ".format(Utilisateur,strOpenPorts))
            
            elif answer == "accept":
                if Database().checkIfExists("data",f"{currentPc}","name","openPorts") is True : 
                    Database(f"{currentPc}","data",f"{self.portList}","name","openPorts").updateValue()
                else :    
                    Database(f"{currentPc}","id","name","field","data","NULL","openPorts","Hardware",f"{self.portList}").insertInDatabase()

            else :
                raise Exception("WRONG ANSWER")

        elif len(self.portList) < len(dbListe):
            
            rest = set(dbListe).difference(set(self.portList))
            answer = print(f"The port : {rest} Just closed")
            
            Database(f"{currentPc}","data",f"{self.portList}","name","openPorts").updateValue()

        else :
            raise Exception("The Matrix is bugged")

        self.mydb.close()
                                                    
    def networkSpace(self):

        previousIp=Database("reseau","Information","Nature","previousIp").getFromDatabase()
    
        if self.monIp != previousIp[0] :
            Tools().Notification(f"Vous avez changé d'espace Réseau\nPrevious IP : {previousIp[0]} \n Current IP : {self.monIp}")

            Database('reseau',"Information",self.monIp,"Nature","currentIp").updateValue()
            Database('reseau',"Information",self.monIp,"Nature","previousIp").updateValue()
            
            Network().networkScan(self.monIp)
        
    def F_Nombre_Utilisateurs_Actuels(self):
        """Surveillance ssh """


        Nombre_Utilisateurs_Actuels=subprocess.getoutput("ss | egrep -i ssh |sort -u | awk '{print $5}' | egrep 'ssh' | wc -l")
        Nombre_Utilisateurs_Actuels=int(Nombre_Utilisateurs_Actuels)

        if Nombre_Utilisateurs_Actuels <= 1 :
            Nombre_Utilisateurs_Actuels=0

        return Nombre_Utilisateurs_Actuels

    def Liste_Autorisée(self):

        Liste_IP=Database("backbone","ipAddress","statut","Allowed").getFromDatabase()

        return Liste_IP

    def ipActuelles(self):
        
        adresseIp_Stage1=[]

        tail=1
        l=self.F_Nombre_Utilisateurs_Actuels()
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


        p=self.ipActuelles()
        m=self.Liste_Autorisée()

        correct = 0
        trueList=[]
      
        for i in range(0,len(p)):
            for k in range(0,len(self.Liste_Autorisée())):
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

            os.system("ps -aux | egrep 'sshd:' | egrep 'joel@'"+str(pts)+"|awk '{print $2}' | xargs kill ")
            Database("backbone","id","statut","ipAddress","NULL","Unallowed",f"{badssh[h]}").insertInDatabase()
            Tools().Notification(" Tentative de connexion non approuvé en cours")
            print("Denied Access")

    def Etapes_de_Fonctionnement(self):
        self.Comparaison()

#TESTS