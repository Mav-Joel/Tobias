#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
import os
import sys
import subprocess
import time


sys.path.insert(1,"/Users/joel/Archetype/Tobi")

from Library.NBook import Network
from Library.TBook import Tools
from Library.DBook import Database

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

#Fonctions////////////////////////////////////////////////
class Security():

    def __init__(self):
        self.Utilisateur=os.environ["USER"]
        self.filePwd=f"/Users/{self.Utilisateur}/.ssh/authorized_keys"
        self.archivePwd=f"/Users/{self.Utilisateur}/Archetype/Tobi/System/Archive/Archive_Keys.save"
        self.archivePwdCron=f"/Users/{self.Utilisateur}/Archetype/Tobi/System/Archive/Archive_Crontab.save"
       
    def initialisationAutorizedKeys(self):
        """ Récupération des clées du fichier authorized_keys"""

        with open(self.filePwd,"r") as keysFile :
            keyfileContent=keysFile.read()
        
        with open(self.archivePwd,"w") as archiveFile :
            archiveFile.write(keyfileContent)
        
        print("Clées Publique autorisées récupérées")

    def initialisationCrontab(self):
        
        os.system(f"crontab -l >> /Users/{self.Utilisateur}/Cron") 

        self.filePwd=f"/Users/{self.Utilisateur}/Cron"
        self.archivePwd=f"/Users/{self.Utilisateur}/Archetype/Tobi/System/Archive/Archive_Crontab.save"

        with open(self.filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()
        
        with open(self.archivePwd,"w") as archiveFile :
            archiveFile.write(cronfileContent)
    
        print("Archive Crées")

        os.system(f"rm /Users/{self.Utilisateur}/Cron")

    def autorized_keysCheck(self):

        try :

            with open(self.filePwd,"r") as keysFile :
                keyfileContent=keysFile.read()

        except :
            Tools().Notification("Le fichier Authorized_keys est introuvable")

        with open(self.archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()

        if archivefileContent != keyfileContent :
            Tools().Notification("Fichier des clées autorisées corrompue")

    def crontabCheck(self):

        os.system(f"crontab -l >> /Users/{self.Utilisateur}/Cron") 
       
        with open(self.filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()

        with open( self.archivePwdCron,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        if archivefileContent != cronfileContent :
            Tools().Notification("Crontab Corrompue")
        
        os.system("rm /home/self.Utilisateur/Cron")

    def reload(self):
        self.initialisationAutorizedKeys()
        self.initialisationCrontab()
        
    def verify(self):

        Update(main,"nFichierHd","systeme")
        Tools().Notification("Mis à Jour")
        print("Updated")



        main=subprocess.getoutput("ls /Users/{} | wc -l".format(self.Utilisateur))
        core=subprocess.getoutput("ls / | wc -l")

        homeDirectory=Recup("systeme","nFichierHd")
        racine=Recup("systeme","nFichierR")

        
      

        if int(main) > int(homeDirectory) :
            print("A File was just created in the Home Directory")
            Tools().Notification("Fichier créer dans le home directory de {}".format(self.Utilisateur))
            verify()
   
        elif int(main) < int(homeDirectory) :
            print("A File was just erased from the Home Directory")
            Tools().Notification("Fichier supprimer dans le home directory de {}".format(self.Utilisateur))
            verify()

        if int(core) > int(racine) :
            print("An important File was just created in the Root Directory")
            Tools().Notification("Fichier créer dans la racine de {}".format(self.Utilisateur))
            verify()

        elif int(core) < int(racine) :
            print("An important File was just erased from the Root directory")
            Tools().Notification("Fichier supprimer dans la racine de {}".format(self.Utilisateur))
            verify()

    def connexion(self):
       
        a=subprocess.getoutput("ss | egrep -i ssh | wc -l ")
        b = Database("reseau","Information","Nature","Liaison SSH Etablie").getFromDatabase()

        if int(b[0]) == int(a) :
            pass 

        elif int(b[0]) < int(a):
            Database("reseau","Information",str(a),"Nature","Liaison SSH Etablie").updateValue()
            Tools().Notification("Liaison SSH Etablie")
            print("SSh Connection Established")
            #SMS("0694232624","Quelqu'un est là ")


        else :
            Database("reseau","Information",str(a),"Nature","Liaison SSH Etablie").updateValue()
            Tools().Notification("Liaison SSH Arrêtée")
            print("SSh Connection Unestablished")

    def Processus(self):

        Pourcentage=subprocess.getoutput("top -b | awk '{print $9}' | head -n +15 | tail -n 8 |head -n 1")
        if len(Pourcentage) >= 5 :
            Tools().Notification("Un processus est gourmand")

