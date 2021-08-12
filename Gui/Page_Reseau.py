#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os
import sys

sys.path.insert(1,"/Users/joel/Archetype/Tobi")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/creatorFiles")
import ast
import json
import subprocess
import sys
from threading import Thread

import mysql
import mysql.connector
import nmap
from Creator import creatorWindow
from Library.DBook import Database
from Library.NBook import Network
from Library.TBook import Tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from addPc import addPcWindow
from Network import NetworkconfWindow
from PageBackbone import bbWindow

magicWords=Tools().getModuleData("localDbPassword","Tobias")
Utilisateur=os.environ["USER"]
#Fonctions////////////////////////////////////////////////

class pageReseauUI(object):

        def __init__(self):
                self.confs = Database().getPaths('path','ConfigurationJson')
                self.launched = 0

        def getModuleData(self,searchingFor,fieldName='user'):
                with open(self.confs,"r") as config :
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
                if self.launched == 1:
                        self.listWidget_3.clear()
                self.launched = 1
                commands = []

                self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=magicWords,
                port="8889",
                )

                Command = self.mydb.cursor() 
                Command.execute("USE tobiasdb") 
                Command.execute("SELECT DISTINCT(Information) FROM coffreFort WHERE name='PredefReseau'")

                for x in Command:
                        for lettre in x :
                                commands.append(lettre)

                if commands != None :
                        for  i in range(len(commands)):
                                self.listWidget_3.insertItem(1,commands[i])

        def Scanip(self):

                toDisplay = []

                
                if self.lineEdit.text() == "" : 
                        Database("rapportExecution","id","Programme","Information","NULL","Tobias","{ Tobias Network's Client Message } : [-] Aucune adresse ip saisie").insertInDatabase()
                else : 

                        Tools().Notification("IP Scan ongoing")
                        Database("rapportExecution","id","Programme","Information","NULL","Tobias","IP Scan ongoing").insertInDatabase()


                        nm = nmap.PortScanner()
                        nm.scan(self.lineEdit.text(), '1-1024')
                        for host in nm.all_hosts(): #HÔTES SUR LE RESEAU
                                

                                
                                #Trying something
                                toDisplay.append('%s'  % (host))
                                toDisplay.append('Hostname : %s' % (nm[host].hostname()))
                                ###################################

                                
                                #Trying something
                                toDisplay.append('Etat : %s' % nm[host].state())
                                ###################################
                             
                                for proto in nm[host].all_protocols():

                                        #Trying something
                                        toDisplay.append('Protocol : %s' % proto)
                                        ###################################
                                        
                                        lport = nm[host][proto].keys()
                                        for port in lport:
                                          

                                                #Trying something
                                                toDisplay.append('port : %s' % (port))
                                                toDisplay.append('%s' % (nm[host][proto][port]['state']))
                                                ###################################
                                        
                                Tools().Notification("IP Scan is Done")
                                Database("rapportExecution","id","Programme","Information","NULL","Tobias","IP Scan is Done").insertInDatabase()

                joined_string = " - ".join(toDisplay)
                self.listWidget.insertItem(1,joined_string)
        
        def ScanT4(self):

                Database("rapportExecution","id","Programme","Information","NULL","Tobias","T4 IP Scan ongoing").insertInDatabase()

                Tools().Notification("T4 IP Scan ongoing")
                if self.lineEdit_2.text() != "" : 
                        ipToCheck = self.lineEdit_2.text()
                else : 
                        ipToCheck = Network().myIp("mask")
                toDisplay = subprocess.getoutput(f"nmap -T4 {ipToCheck} | tail +3")

                self.listWidget_2.insertItem(1,toDisplay)

                Database("rapportExecution","id","Programme","Information","NULL","Tobias","T4 IP Scan is Done").insertInDatabase()

                Tools().Notification("T4 IP Scan is Done")
               
        def execute(self,toExecute=False):

                if toExecute == False:
                        content = subprocess.getoutput(self.lineEdit_9.text())
                else :
                        content = subprocess.getoutput(toExecute)

                self.listWidget_2.insertItem(1,content)
                self.save(self.lineEdit_9.text())
                
        def save(self,thing):
                Database("coffreFort","id","name","Information","NULL","PredefReseau",thing).insertInDatabase()
                self.LoadData()

        def globalScan(self) :

                toDisplay = []

                Tools().Notification("Network IP Scan ongoing")
                Database("rapportExecution","id","Programme","Information","NULL","Tobias","Network IP Scan ongoing").insertInDatabase()
        

                nm = nmap.PortScanner()
                nm.scan(hosts=Network().myIp("mask"), arguments='-n -sP ')

                hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
                for host, status in hosts_list:
                        
                        toDisplay.append(host+" : "+status)
                        toDisplay.append(f'Host : {host} ({nm[host].hostname()})')
                        
                        
                Tools().Notification("The Network IP Scan is Done")
                Database("rapportExecution","id","Programme","Information","NULL","Tobias","The Network IP Scan is Done").insertInDatabase()
        
                
                for i in range(0,len(toDisplay)):
                        self.listWidget.insertItem(i,toDisplay[i])
        
        def feature(self):
                self.execute(self.listWidget_3.currentItem().text())

        def setupUi(self, MainWindow):
                
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1262, 695)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame_3 = QtWidgets.QFrame(self.centralwidget)
                self.frame_3.setGeometry(QtCore.QRect(10, 130, 621, 371))
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.listWidget = QtWidgets.QListWidget(self.frame_3)
                self.listWidget.setGeometry(QtCore.QRect(10, 60, 591, 291))
                self.listWidget.setObjectName("listWidget")
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                self.listWidget.setFont(font)
                self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
                self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 291, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                self.pushButton_5.setFont(font)
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
                self.pushButton_7.setGeometry(QtCore.QRect(310, 20, 291, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                self.pushButton_7.setFont(font)
                self.pushButton_7.setObjectName("pushButton_7")
                self.frame_4 = QtWidgets.QFrame(self.centralwidget)
                self.frame_4.setGeometry(QtCore.QRect(10, 10, 621, 91))
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit.setGeometry(QtCore.QRect(10, 10, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.lineEdit.setFont(font)
                self.lineEdit.setText("")
                self.lineEdit.setObjectName("lineEdit")
                self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
                self.pushButton_3.setGeometry(QtCore.QRect(500, 10, 88, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
                self.pushButton_6.setGeometry(QtCore.QRect(500, 50, 88, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_6.setFont(font)
                self.pushButton_6.setObjectName("pushButton_6")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 281, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setText("")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
                self.lineEdit_3.setGeometry(QtCore.QRect(170, 10, 241, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setText("")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget_2.setGeometry(QtCore.QRect(650, 60, 591, 581))
                self.listWidget_2.setObjectName("listWidget_2")
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                self.listWidget_2.setFont(font)
                self.frame_5 = QtWidgets.QFrame(self.centralwidget)
                self.frame_5.setGeometry(QtCore.QRect(650, 10, 591, 51))
                self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_5.setObjectName("frame_5")
                self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
                self.pushButton_4.setGeometry(QtCore.QRect(470, 10, 88, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setObjectName("pushButton_4")
                self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_5)
                self.lineEdit_9.setGeometry(QtCore.QRect(10, 10, 411, 31))
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.lineEdit_9.setFont(font)
                self.lineEdit_9.setText("")
                self.lineEdit_9.setObjectName("lineEdit_9")
                self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget_3.setGeometry(QtCore.QRect(10, 500, 621, 141))
                self.listWidget_3.setObjectName("listWidget_3")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.menuBar = QtWidgets.QMenuBar(MainWindow)
                self.menuBar.setGeometry(QtCore.QRect(0, 0, 1262, 30))
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
                self.actionVue_Compl_te = QtWidgets.QAction(MainWindow)
                self.actionVue_Compl_te.setObjectName("actionVue_Compl_te")
                self.actionADD = QtWidgets.QAction(MainWindow)
                self.actionADD.setObjectName("actionADD")
                self.actionNetwork_csv = QtWidgets.QAction(MainWindow)
                self.actionNetwork_csv.setObjectName("actionNetwork_csv")
                self.menuParam_tres.addAction(self.actionBackBone)
                self.menuAjouter_un_ordinateur.addAction(self.actionADD)
                self.menuConfiguration_R_seau.addAction(self.actionNetwork_csv)
                self.menuBar.addAction(self.menuParam_tres.menuAction())
                self.menuBar.addAction(self.menuAjouter_un_ordinateur.menuAction())
                self.menuBar.addAction(self.menuConfiguration_R_seau.menuAction())

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                font = QtGui.QFont()
                font.setFamily("Inconsolata SemiBold")
                font.setPointSize(13)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.listWidget_3.setFont(font)
       

                # EVENTS
                self.actionNetwork_csv.triggered.connect(self.modifyconf)
                self.actionBackBone.triggered.connect(self.pageBackbone)
                self.actionADD.triggered.connect(self.add)
                self.listWidget_3.itemDoubleClicked.connect(self.feature)


                self.pushButton_5.clicked.connect(self.globalScan)
                self.pushButton_4.clicked.connect(self.execute)
                self.pushButton_7.clicked.connect(self.openCreatorWindow)
                self.pushButton_3.clicked.connect(self.Scanip)
                self.pushButton_6.clicked.connect(self.ScanT4)
                self.LoadData()
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Network Page"))
                self.pushButton_5.setText(_translate("MainWindow", "Scan Réseau "))
                self.pushButton_7.setText(_translate("MainWindow", "Utiliser dans le mode Créateur"))
                self.lineEdit.setPlaceholderText(_translate("MainWindow", " Port Scan"))
                self.pushButton_3.setText(_translate("MainWindow", "Scan IP"))
                self.pushButton_6.setText(_translate("MainWindow", "Start"))
                self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " Scan T4"))
                self.lineEdit_3.setPlaceholderText(_translate("MainWindow", " Arguments"))
                self.pushButton_4.setText(_translate("MainWindow", "Start"))
                self.lineEdit_9.setPlaceholderText(_translate("MainWindow", " Commande à Executer"))
                self.menuParam_tres.setTitle(_translate("MainWindow", "SSH"))
                self.menuAjouter_un_ordinateur.setTitle(_translate("MainWindow", "Enregistrer un ordinateur"))
                self.menuConfiguration_R_seau.setTitle(_translate("MainWindow", "Configuration Réseau"))
                self.actionBackBone.setText(_translate("MainWindow", "BackBone"))
                self.actionVue_Compl_te.setText(_translate("MainWindow", "Vue Complète"))
                self.actionADD.setText(_translate("MainWindow", "ADD"))
                self.actionNetwork_csv.setText(_translate("MainWindow", "Network.csv"))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    pageReseauWindow = QtWidgets.QMainWindow()
    ui = pageReseauUI()
    ui.setupUi(pageReseauWindow)
    pageReseauWindow.show()
    sys.exit(app.exec_())
