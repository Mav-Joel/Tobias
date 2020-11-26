#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
import os
import sys
import subprocess
import time

import notify2

from Bibliotheque.NBook import Network
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
Utilisateur=os.environ["USER"]

#Fonctions////////////////////////////////////////////////
class Security():
    
    def initialisationAutorizedKeys(self):
        """ Récupération des clées du fichier authorized_keys"""

        filePwd=f"/home/{Utilisateur}/.ssh/authorized_keys"
        archivePwd=f"/home/{Utilisateur}/Archetype/Tobito/Ressources/Archive/Archive_Keys.save"
        with open(filePwd,"r") as keysFile :
            keyfileContent=keysFile.read()
        
        with open(archivePwd,"w") as archiveFile :
            archiveFile.write(keyfileContent)
        
        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        print("Clées Publique autorisées récupérées")

    def initialisationCrontab(self):
        
        os.system("crontab -l >> /home/Utilisateur/Cron") 
        filePwd=f"/home/{Utilisateur}/Cron"
        archivePwd=f"/home/{Utilisateur}/Archetype/Tobito/Ressources/Archive/Archive_Crontab.save"

        with open(filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()
        
        with open(archivePwd,"w") as archiveFile :
            archiveFile.write(cronfileContent)
        
        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        print("Archive Créer")
        os.system(f"rm /home/{Utilisateur}/Cron")

    def autorized_keysCheck(self):

        filePwd=f"/home/{Utilisateur}/.ssh/authorized_keys"
        archivePwd=f"/home/{Utilisateur}/Archetype/Tobito/Ressources/Archive/Archive_Keys.save"

        try :

            with open(filePwd,"r") as keysFile :
                keyfileContent=keysFile.read()

        except :
            Tools().Notification("Le fichier Authorized_keys est introuvable")

        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()

        if archivefileContent != keyfileContent :
            Tools().Notification("Fichier des clées autorisées corrompue")

    def crontabCheck(self):

        getCrontab=os.system("crontab -l >> /home/Utilisateur/Cron") 
        filePwd=f"/home/{Utilisateur}/Cron"
        archivePwd=f"/home/{Utilisateur}/Archetype/Tobito/Ressources/Archive/Archive_Crontab.save"
        
        with open(filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()

        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        if archivefileContent != cronfileContent :
            Tools().Notification("Crontab Corrompue")
        
        os.system("rm /home/Utilisateur/Cron")


    def verify(self):

        Update(main,"nFichierHd","systeme")
        Tools().Notification("Mis à Jour")
        print("Updated")



        main=subprocess.getoutput("ls /home/{} | wc -l".format(Utilisateur))
        core=subprocess.getoutput("ls / | wc -l")

        homeDirectory=Recup("systeme","nFichierHd")
        racine=Recup("systeme","nFichierR")

        
      

        if int(main) > int(homeDirectory) :
            print("A File was just created in the Home Directory")
            Tools().Notification("Fichier créer dans le home directory de {}".format(Utilisateur))
            verify()
   
        elif int(main) < int(homeDirectory) :
            print("A File was just erased from the Home Directory")
            Tools().Notification("Fichier supprimer dans le home directory de {}".format(Utilisateur))
            verify()

        if int(core) > int(racine) :
            print("An important File was just created in the Root Directory")
            Tools().Notification("Fichier créer dans la racine de {}".format(Utilisateur))
            verify()

        elif int(core) < int(racine) :
            print("An important File was just erased from the Root directory")
            Tools().Notification("Fichier supprimer dans la racine de {}".format(Utilisateur))
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
            time.sleep(30)

