#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
import os
import sys
import subprocess
import time

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

from Bibliotheque.NBook import *
from Bibliotheque.TBook import *
from Bibliotheque.DBook import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#Fonctions////////////////////////////////////////////////
class Security():
    
    def initialisationAutorizedKeys():
        """ Récupération des clées du fichier authorized_keys"""

        filePwd="/home/joel/.ssh/authorized_keys"
        archivePwd="/home/joel/Archétype/Tobito/Ressources/Archive/Archive_Keys.save"
        with open(archivePwd,"w") as variable :
            pass
        
        with open(filePwd,"r") as keysFile :
            keyfileContent=keysFile.read()
        
        with open(archivePwd,"w") as archiveFile :
            archiveFile.write(keyfileContent)
        
        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        print("Clées Publique autorisées récupérées")

    def initialisationCrontab():
        
        getCrontab=os.system("crontab -l >> /home/joel/Cron") 
        filePwd="/home/joel/Cron"
        archivePwd="/home/joel/Archétype/Tobito/Ressources/Archive/Archive_Crontab.save"

        with open(archivePwd,"w") as variable :
            pass
        
        with open(filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()
        
        with open(archivePwd,"w") as archiveFile :
            archiveFile.write(cronfileContent)
        
        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        print("Archive Créer")
        os.system("rm /home/joel/Cron")

    def autorized_keysCheck():

        filePwd="/home/joel/.ssh/authorized_keys"
        archivePwd="/home/joel/Archétype/Tobito/Ressources/Archive/Archive_Keys.save"

        try :

            with open(filePwd,"r") as keysFile :
                keyfileContent=keysFile.read()

        except :
            Notification("Le fichier Authorized_keys est introuvable")

        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()

        if archivefileContent != keyfileContent :
            Notification("Fichier des clées autorisées corrompue")

    def crontabCheck():

        getCrontab=os.system("crontab -l >> /home/joel/Cron") 
        filePwd="/home/joel/Cron"
        archivePwd="/home/joel/Archétype/Tobito/Ressources/Archive/Archive_Crontab.save"
        
        with open(filePwd,"r") as cronFile :
            cronfileContent=cronFile.read()

        with open(archivePwd,"r") as archiveFile :    
            archivefileContent=archiveFile.read()
        
        if archivefileContent != cronfileContent :
            Notification("Crontab Corrompue")
        
        os.system("rm /home/joel/Cron")


    def verify():

        Update(main,"nFichierHd","systeme")
        Notification("Mis à Jour")
        print("Updated")



        main=subprocess.getoutput("ls /home/{} | wc -l".format(Utilisateur))
        core=subprocess.getoutput("ls / | wc -l")

        homeDirectory=Recup("systeme","nFichierHd")
        racine=Recup("systeme","nFichierR")

        
      

        if int(main) > int(homeDirectory) :
            print("A File was just created in the Home Directory")
            Notification("Fichier créer dans le home directory de {}".format(Utilisateur))
            verify()
   
        elif int(main) < int(homeDirectory) :
            print("A File was just erased from the Home Directory")
            Notification("Fichier supprimer dans le home directory de {}".format(Utilisateur))
            verify()

        if int(core) > int(racine) :
            print("An important File was just created in the Root Directory")
            Notification("Fichier créer dans la racine de {}".format(Utilisateur))
            verify()

        elif int(core) < int(racine) :
            print("An important File was just erased from the Root directory")
            Notification("Fichier supprimer dans la racine de {}".format(Utilisateur))
            verify()



    def connexion():
       
        a=subprocess.getoutput("ss | egrep -i ssh | wc -l ")
        b = Recup("reseau","Liaison SSH Etablie","Information","Network")
        if int(b) == int(a) :
            pass 

        elif int(b) < int(a):
            Update(str(a),"Liaison SSH Etablie","reseau","Information","Network")
            Notification("Liaison SSH Etablie")
            print("SSh Connection Established")
            #SMS("0694232624","Quelqu'un est là ")


        else :
            Update(str(a),"Liaison SSH Etablie","reseau","Information","Network")
            Notification("Liaison SSH Arrêtée")
            print("SSh Connection Unestablished")

    def Processus():

        Pourcentage=subprocess.getoutput("top -b | awk '{print $9}' | head -n +15 | tail -n 8 |head -n 1")
        if len(Pourcentage) >= 5 :
            Notification("Un processus est gourmand")
            time.sleep(30)

