#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os
import nmap
import sys
from getpass import getpass
import hashlib
import signal
import webbrowser
import subprocess
import socket
from threading import Thread
import threading
import time
import notify2
from Bibliotheque.NBook import Network
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
from Network import NetworkconfWindow
import mysql.connector
import ast
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from Creator import creatorWindow
from addPc import addPcWindow
from PageBackbone import bbWindow
import pandas as pd
    
magicWords=Tools().getModuleData("local dbpassword","Tobias")
import json
Utilisateur=os.environ["USER"]

#Fonctions////////////////////////////////////////////////

def MyConverter(mydata):
        def cvt(data):
                try : 
                        return ast.litteral_eval(data)
                except Exception:
                        return str(data)
        return tuple(map(cvt,mydata))

        
class pageReseauUI(object):

        def getModuleData(self,searchingFor,fieldName='user'):
                with open(f"/home/{Utilisateur}/Archetype/Tobi/Admin/Configurations.json","r") as config :
                        content = json.load(config)

                for parameters in content['Configurations'] :
                        for keys,values in parameters[fieldName].items() : 
                                if searchingFor == keys :
                                       return values

        def pageBackbone(self): 
                self.window = QtWidgets.QMainWindow()
                self.ui = bbWindow()
                self.ui.setupUi(self.window)
                self.window.show()

        def modifyconf(self): 
                self.window = QtWidgets.QMainWindow()
                self.ui = NetworkconfWindow()
                self.ui.setupUi(self.window)
                self.window.show()

        def add(self): 
                self.window = QtWidgets.QMainWindow()
                self.ui = addPcWindow()
                self.ui.setupUi(self.window)
                self.window.show()

        def openCreatorWindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = creatorWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                
        def LoadData(self):

                if self.lineEdit_11.text() != "" :
                        magicWords = self.lineEdit_11.text() 
                else : 
                        magicWords = Tools().getModuleData("local dbpassword","Tobias")

                mydb = mysql.connector.connect(
                host="localhost",
                user="Python",
                passwd=magicWords,
                )

                Command = mydb.cursor()
                Command.execute("USE tobiasdb") 
                if self.lineEdit_7.text() != "" :

                        Command.execute(self.lineEdit_7.text())

                else : 
                        Command.execute("SELECT * FROM reseau")

                data = Command.fetchall()

                for row in data : 
                        self.addTable(MyConverter(row))

                Command.close()

        def addTable(self,columns):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)

                for i, column in enumerate(columns):
                        self.tableWidget.setItem(rowPosition, i , QtWidgets.QTableWidgetItem(str(column)))

        def threadHost(self):
                mon_thread=threading.Thread(target=self.Hebergeur)   #définit la fonction a executer en arrière-plan
                mon_thread.start()  

        def filepicker1(self):
                fileName = QFileDialog.getOpenFileName()
                self.lineEdit_10.setText(fileName[0])
        
        def filepicker2(self):
                fileName = QFileDialog.getOpenFileName()
                self.lineEdit_8.setText(fileName[0])

        def exec1(self):
                os.system(self.lineEdit_10.text())
        
        def exec2(self):
                os.system(self.lineEdit_8.text())

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1339, 697)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
             
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(1220, 410, 111, 31))
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.clicked.connect(self.LoadData)

                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(10, 10, 321, 361))
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                
                self.label1_2 = QtWidgets.QLabel(self.frame)
                self.label1_2.setGeometry(QtCore.QRect(120, 10, 61, 31))
                self.label1_2.setObjectName("label1_2")
                
                self.pushButton = QtWidgets.QPushButton(self.frame)
                self.pushButton.setGeometry(QtCore.QRect(220, 280, 88, 34))
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.Connecteur)

                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_2.setGeometry(QtCore.QRect(20, 240, 191, 31))
                self.lineEdit_2.setObjectName("lineEdit_2")
                
                self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_4.setGeometry(QtCore.QRect(20, 90, 151, 31))
                self.lineEdit_4.setText("")
                self.lineEdit_4.setObjectName("lineEdit_4")
                
                self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_6.setGeometry(QtCore.QRect(20, 50, 181, 31))
                self.lineEdit_6.setText("")
                self.lineEdit_6.setObjectName("lineEdit_6")
                
                self.pushButton_2 = QtWidgets.QPushButton(self.frame)
                self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 88, 34))
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(self.threadHost)

                self.label1_3 = QtWidgets.QLabel(self.frame)
                self.label1_3.setGeometry(QtCore.QRect(240, 80, 61, 31))
                self.label1_3.setObjectName("label1_3")
                self.label1_4 = QtWidgets.QLabel(self.frame)
                self.label1_4.setGeometry(QtCore.QRect(120, 200, 61, 31))
                self.label1_4.setObjectName("label1_4")
                
                self.label1 = QtWidgets.QLabel(self.frame)
                self.label1.setGeometry(QtCore.QRect(120, 130, 111, 31))
                self.label1.setObjectName("label1")
                
                self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_16.setGeometry(QtCore.QRect(20, 320, 191, 31))
                self.lineEdit_16.setObjectName("lineEdit_16")
                
                self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_17.setGeometry(QtCore.QRect(20, 280, 191, 31))
                self.lineEdit_17.setObjectName("lineEdit_17")
                
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(360, 10, 321, 251))
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                
                self.label1_5 = QtWidgets.QLabel(self.frame_2)
                self.label1_5.setGeometry(QtCore.QRect(120, 10, 101, 31))
                self.label1_5.setObjectName("label1_5")
                
                self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit_8.setGeometry(QtCore.QRect(20, 150, 151, 31))
                self.lineEdit_8.setText("")
                self.lineEdit_8.setObjectName("lineEdit_8")
                
                self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit_10.setGeometry(QtCore.QRect(20, 50, 181, 31))
                self.lineEdit_10.setText("")
                self.lineEdit_10.setObjectName("lineEdit_10")
                
                self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_9.setGeometry(QtCore.QRect(20, 90, 88, 34))
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_9.clicked.connect(self.exec1)

                self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_10.setGeometry(QtCore.QRect(20, 190, 88, 34))
                self.pushButton_10.setObjectName("pushButton_10")
                self.pushButton_10.clicked.connect(self.exec2)
                
                self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_11.setGeometry(QtCore.QRect(210, 50, 88, 34))
                self.pushButton_11.setObjectName("pushButton_11")
                self.pushButton_11.clicked.connect(self.filepicker1)

                self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_12.setGeometry(QtCore.QRect(180, 150, 88, 34))
                self.pushButton_12.setObjectName("pushButton_12")
                self.pushButton_12.clicked.connect(self.filepicker2)

                self.label1_8 = QtWidgets.QLabel(self.frame_2)
                self.label1_8.setGeometry(QtCore.QRect(120, 90, 111, 31))
                self.label1_8.setObjectName("label1_8")
                
                self.frame_3 = QtWidgets.QFrame(self.centralwidget)
                self.frame_3.setGeometry(QtCore.QRect(700, 10, 621, 361))
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                
                self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
                self.lineEdit_3.setGeometry(QtCore.QRect(20, 20, 181, 32))
                self.lineEdit_3.setObjectName("lineEdit_3")
                
                self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
                self.pushButton_6.setGeometry(QtCore.QRect(200, 20, 51, 31))
                self.pushButton_6.setObjectName("pushButton_6")
                
                self.listWidget = QtWidgets.QListWidget(self.frame_3)
                self.listWidget.setGeometry(QtCore.QRect(10, 60, 591, 291))
                self.listWidget.setObjectName("listWidget")
                self.listWidget.setDragEnabled(True)

                self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
                self.pushButton_5.setGeometry(QtCore.QRect(260, 20, 91, 31))
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_5.clicked.connect(self.globalScan)

                self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
                self.pushButton_7.setGeometry(QtCore.QRect(360, 20, 201, 31))
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_7.clicked.connect(self.openCreatorWindow)

                self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
                self.tableWidget.setGeometry(QtCore.QRect(10, 450, 1311, 192))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(13)
                self.tableWidget.setRowCount(0)
                
                self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_7.setGeometry(QtCore.QRect(10, 410, 1031, 31))
                self.lineEdit_7.setText("")
                self.lineEdit_7.setObjectName("lineEdit_7")
                
                self.frame_4 = QtWidgets.QFrame(self.centralwidget)
                self.frame_4.setGeometry(QtCore.QRect(360, 280, 321, 91))
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                
                self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit.setGeometry(QtCore.QRect(10, 10, 151, 31))
                self.lineEdit.setText("")
                self.lineEdit.setObjectName("lineEdit")
                
                self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
                self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 88, 31))
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(self.Scanip)

                self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit_9.setGeometry(QtCore.QRect(10, 50, 291, 31))
                self.lineEdit_9.setText("")
                self.lineEdit_9.setObjectName("lineEdit_9")
               
                self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_11.setGeometry(QtCore.QRect(1050, 410, 161, 31))
                self.lineEdit_11.setText("")
                self.lineEdit_11.setObjectName("lineEdit_11")
                self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Password)


                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.menuBar = QtWidgets.QMenuBar(MainWindow)
                self.menuBar.setGeometry(QtCore.QRect(0, 0, 1339, 30))
                self.menuBar.setObjectName("menuBar")
                self.menuParam_tres = QtWidgets.QMenu(self.menuBar)
                self.menuParam_tres.setObjectName("menuParam_tres")
                self.menuAjouter_un_ordinateur = QtWidgets.QMenu(self.menuBar)
                self.menuAjouter_un_ordinateur.setObjectName("menuAjouter_un_ordinateur")
                self.menuConfiguration_R_seau = QtWidgets.QMenu(self.menuBar)
                self.menuConfiguration_R_seau.setObjectName("menuConfiguration_R_seau")
                MainWindow.setMenuBar(self.menuBar)
                self.actionBackBone = QtWidgets.QAction(MainWindow)
                self.actionBackBone.setObjectName("actionBackBone")
                self.actionBackBone.triggered.connect(self.pageBackbone)
                self.actionVue_Compl_te = QtWidgets.QAction(MainWindow)
                self.actionVue_Compl_te.setObjectName("actionVue_Compl_te")
                self.actionADD = QtWidgets.QAction(MainWindow)
                self.actionADD.setObjectName("actionADD")
                self.actionADD.triggered.connect(self.add)
                self.actionNetwork_csv = QtWidgets.QAction(MainWindow)
                self.actionNetwork_csv.setObjectName("actionNetwork_csv")
                self.menuParam_tres.addAction(self.actionBackBone)
                self.menuAjouter_un_ordinateur.addAction(self.actionADD)
                self.menuConfiguration_R_seau.addAction(self.actionNetwork_csv)
                self.menuBar.addAction(self.menuParam_tres.menuAction())
                self.menuBar.addAction(self.menuAjouter_un_ordinateur.menuAction())
                self.menuBar.addAction(self.menuConfiguration_R_seau.menuAction())
                self.actionNetwork_csv.triggered.connect(self.modifyconf)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Network Page"))
                self.pushButton_4.setText(_translate("MainWindow", "Afficher BD"))
                self.label1_2.setText(_translate("MainWindow", "Sockets"))
                self.pushButton.setText(_translate("MainWindow", "Se connecter"))
                self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Adresse du Serveur"))
                self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Port 5567 par défaut"))
                self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Hôte Localhost par défaut"))
                self.pushButton_2.setText(_translate("MainWindow", "Héberger"))
                self.label1_3.setText(_translate("MainWindow", "Serveur"))
                self.label1_4.setText(_translate("MainWindow", "Client"))
                self.label1.setText(_translate("MainWindow", "Etat serveur : Off"))
                self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "Data"))
                self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "Port"))
                self.label1_5.setText(_translate("MainWindow", "Sockets Custom"))
                self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Chemin du client"))
                self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Chemin du serveur"))
                self.pushButton_9.setText(_translate("MainWindow", "Héberger"))
                self.pushButton_10.setText(_translate("MainWindow", "Se connecter"))
                self.pushButton_11.setText(_translate("MainWindow", "..."))
                self.pushButton_12.setText(_translate("MainWindow", "..."))
                self.label1_8.setText(_translate("MainWindow", "Etat serveur : Off"))
                self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Commande à Executer"))
                self.pushButton_6.setText(_translate("MainWindow", "OK"))
                self.pushButton_5.setText(_translate("MainWindow", "Scan Réseau "))
                self.pushButton_7.setText(_translate("MainWindow", "Utiliser dans le mode Créateur"))
                self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Commande Mysql"))
                self.lineEdit.setPlaceholderText(_translate("MainWindow", "Port Scan"))
                self.pushButton_3.setText(_translate("MainWindow", "Scan IP"))
                self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Commande à Executer"))
                self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Mot de Passe BD"))
                self.menuParam_tres.setTitle(_translate("MainWindow", "SSH"))
                self.menuConfiguration_R_seau.setTitle(_translate("MainWindow", "Configuration Réseau"))
                self.actionBackBone.setText(_translate("MainWindow", "BackBone"))
                self.actionVue_Compl_te.setText(_translate("MainWindow", "Vue Complète"))
                self.menuAjouter_un_ordinateur.setTitle(_translate("MainWindow", "Enregistrer un ordinateur"))
                self.actionADD.setText(_translate("MainWindow", "ADD"))
                self.actionNetwork_csv.setText(_translate("MainWindow", "Network.csv"))


        def update(self):
                self.label1.adjustSize()
                
        def Hebergeur(self):
                self.label1.setText("Etat serveur : On")
                self.update()

                if self.lineEdit_6.text() != "" : 

                        host,port = (self.lineEdit_6.text(),5567)
                        
                        if self.lineEdit_4.text() != "" : 

                                host,port = (self.lineEdit_6.text(),self.lineEdit_4.text())
                        else : 
                                pass

                else :
                        host,port = ('',5567)

                        if self.lineEdit_4.text() != "" : 

                                host,port = ('',int(self.lineEdit_4.text()))
                        else : 
                                pass
                        

                prise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                prise.bind((host,port)) #Associer à Adresse IP
                print("Le serveur est initialisé")

                while True :

                        prise.listen(10) #Lier à port défini dans le tuple plus haut
                        connexion, address = prise.accept()

                        data = connexion.recv(2048) #Recevoir une donnée
                        data = data.decode("utf8")
                    #Jean
                        print(data)
                        with open(f"/home/{Utilisateur}/jordanBruno.csv","a") as variable : 
                                variable.write(data)
                                df = pd.DataFrame(data=data, index="test")
                                print(df)
                        self.update()
                      

                connexion.close()
                prise.close()


                self.label1.setText("Etat serveur : Off")

        
        def Connecteur(self):

                if self.lineEdit_2.text() != "" : 

                        host,port = (self.lineEdit_2.text(),5567)
                        
                        if self.lineEdit_17.text() != "" : 
                                print(self.lineEdit_17.text())
                                print(self.lineEdit_2.text())
                                host,port = (self.lineEdit_2.text(),int(self.lineEdit_17.text()))
                        else : 
                                pass

                else :

                        host,port = ('',5567)

                        if self.lineEdit_17.text() != "" : 

                                host,port = ('',int(self.lineEdit_17.text()))
                        else : 
                                pass
                        
                try :
                        socket_Nedih = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Indispensable
                        socket_Nedih.connect((host,port))
                        
                        print("{ Tobias Socket's Client Message } : [+] Connecté") 
                        
                        if self.lineEdit_16.text() != "" :

                                data=self.lineEdit_16.text()

                        else : 

                                data="Hey je suis connecté"

                        data=data.encode("utf8")
                        socket_Nedih.sendall(data)

                except :
                        print("{ Tobias Socket's Client Message } : [-] Failed") 

                finally :
                        socket_Nedih.close()
     

        def Scanip(self):

                toDisplay = []

                
                if self.lineEdit.text() == "" : 
                        print("{ Tobias Network's Client Message } : [-] Aucune adresse ip saisie")
                else : 

                        print("IP Scan ongoing")

                        nm = nmap.PortScanner()
                        nm.scan(self.lineEdit.text(), '1-1024')
                        for host in nm.all_hosts(): #HÔTES SUR LE RESEAU
                                

                                print('Host : %s (%s)' % (host, nm[host].hostname()))
                                
                                #Trying something
                                toDisplay.append('%s'  % (host))
                                toDisplay.append('%s' % (nm[host].hostname()))
                                ###################################

                                print('State : %s' % nm[host].state())
                                
                                #Trying something
                                toDisplay.append('%s' % nm[host].state())
                                ###################################
                             
                                for proto in nm[host].all_protocols():
                                
                                        print('----------')
                                        print('Protocol : %s' % proto)

                                        #Trying something
                                        toDisplay.append('%s' % proto)
                                        ###################################
                                        
                                        lport = nm[host][proto].keys()
                                        for port in lport:
                                          
                                                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

                                                #Trying something
                                                toDisplay.append('port : %s' % (port))
                                                toDisplay.append('%s' % (nm[host][proto][port]['state']))
                                                ###################################
                                        
                                print("The IP Scan is Done")

                for i in range(0,len(toDisplay)):
                        self.listWidget.insertItem(i,toDisplay[i])
        

        def globalScan(self) :

                toDisplay = []

                print("Network IP Scan ongoing")        
                Tools().Notification("Network IP Scan ongoing")
                print("Network IP Scan ongoing")
        

                nm = nmap.PortScanner()
                nm.scan(hosts=Network().myIp("mask"), arguments='-n -sP -PE -PA21,23,80,3389')
             
                hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
             
                for host, status in hosts_list:
             
                        print(host+" : "+status)
                        toDisplay.append(host+" : "+status)

                        nm.scan(host, '1-1024')

                        print('Host : %s (%s)' % (host, nm[host].hostname()))
                        toDisplay.append('Host : %s (%s)' % (host, nm[host].hostname()))

                        for proto in nm[host].all_protocols():

                                print('Protocol : %s' % proto)
                                toDisplay.append('Protocol : %s' % proto)

                                lport = nm[host][proto].keys()
        
                                for port in lport:

                                        print(('port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])))
                                        toDisplay.append(('port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])))
                        
                print("The Network IP Scan is Done")
                
                for i in range(0,len(toDisplay)):
                        self.listWidget.insertItem(i,toDisplay[i])
        

        def getResult(self):
                self.LoadData()

#def pageReseauWindow():
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    pageReseauWindow = QtWidgets.QMainWindow()
    ui = pageReseauUI()
    ui.setupUi(pageReseauWindow)
    pageReseauWindow.show()
    sys.exit(app.exec_())
