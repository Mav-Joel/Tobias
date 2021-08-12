#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import os
import mysql.connector
import paramiko
from ToDoFrom import toDoFromWindow
from UpdateHosts import updateWindow
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.DBook import Database
from Library.TBook import Tools


MagicWord=Tools().getModuleData("localDbPassword","Tobias")

eligibleName = []
eligibleIP = []
display = []
commandList = []

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd=Tools().getModuleData("localDbPassword","Tobias"),
port="8889"
)

Command = mydb.cursor() 
Command.execute("USE tobiasdb") 
Command.execute("SELECT DISTINCT(hostname) FROM knownIps")

for x in Command:
    for lettre in x :
        eligibleName.append(lettre)

Command = mydb.cursor() 
Command.execute("USE tobiasdb") 
Command.execute("SELECT DISTINCT(address) FROM knownIps")

for x in Command:
    for lettre in x :
        eligibleIP.append(lettre)

Command = mydb.cursor() 
Command.execute("USE tobiasdb") 
Command.execute("SELECT DISTINCT(Information) FROM servCommands")

for x in Command:
    for lettre in x :
        commandList.append(lettre)

for i in range (0,len(eligibleName)) : 
    display.append(eligibleIP[i]+" "+eligibleName[i])


class ServerWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("localDbPassword","Tobias")


    def openAddWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = updateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def CommandeClique(self):
        liste = []

        item = self.listWidget_2.currentItem()
        liste.append(item.text())

        return liste
    
    def openTodoFrom(self):
 
        self.window = QtWidgets.QMainWindow()
        self.ui = toDoFromWindow()
        self.ui.setupUi(self.window)
        self.window.show()
   
    def send(self):  
        echantillon = []
        #Trouver les IPS
        for i in range(0,len(display)):
            items = self.listWidget_3.findItems(display[i],QtCore.Qt.MatchExactly)

            if len(items) > 0:
                Command = mydb.cursor() 
                Command.execute("USE tobiasdb") 
                
                for item in items:

                    ipStage1 = item.text()
                    ipStage2 = ipStage1.find(" ")
                    ipStage3 = ipStage1[:ipStage2]
                    echantillon.append(ipStage3)
                
        passwordTextBox = self.lineEdit.text()
        passwordList = passwordTextBox.split(",")

        usernameTextBox = self.lineEdit_3.text()
        usernameList = usernameTextBox.split(",") 

        #Si la combo box dit sauvegarder alors : sinon : 
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb")
        for i in range(0,len(echantillon)) :
            Command.execute("INSERT INTO server (id , ipAddress , Password ) VALUES ( NULL , '{}' , '{}')".format(echantillon[i],passwordList[i]))
            mydb.commit()

        commande = self.lineEdit_2.text()
       
            

        if self.lineEdit_2.text() != "" :
            
            Command = mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("INSERT INTO servCommands (id, Information) VALUES (NULL , '{}')".format(commande))
            mydb.commit()
            
            commandeList = commande.split(",")  

        
        else  :
            commandeList = self.CommandeClique()

        
        #Liste des IPS : echantillon[i]
        #Liste des mot de passe : passwordList[i]
        #Liste des commandes : commandeList[i]
        #Executer : 

        for i in range(0,len(echantillon)):

            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(echantillon[i],port=22 ,username=usernameList[i],password=passwordList[i])
            for i in range(0,len(commandeList)) : 
                stdin,stdout,stderr=ssh.exec_command(commandeList[i])
                output = stdout.readlines()
                print( "\n".join(output))
                # Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{output}").insertInDatabase()


    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 110, 351, 231))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragEnabled(True)
        
        for i in range(0,len(display)):
            self.listWidget.insertItem(i,display[i])
      
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 181, 18))
        self.label.setObjectName("label")
       
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(550, 160, 351, 151))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.itemClicked.connect(self.CommandeClique)
        
        for i in range(0,len(commandList)) :
            self.listWidget_2.insertItem(i,commandList[i])
     
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 410, 351, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
       
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 161, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openAddWindow)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 130, 181, 18))
        self.label_3.setObjectName("label_3")
       
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 320, 351, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 370, 71, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.send)
        
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(550, 30, 351, 81))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setDragEnabled(True)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 10, 181, 18))
        self.label_4.setObjectName("label_4")
      
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 410, 81, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 360, 351, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 360, 81, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
       
      
        MainWindow.setCentralWidget(self.centralwidget)
       
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 30))
        self.menubar.setObjectName("menubar")
        self.menuMTP = QtWidgets.QMenu(self.menubar)
        self.menuMTP.setObjectName("menuMTP")
      
        MainWindow.setMenuBar(self.menubar)
     
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionMulti_Task_Pc = QtWidgets.QAction(MainWindow)
        self.actionMulti_Task_Pc.setObjectName("actionMulti_Task_Pc")
        self.actionMulti_Task_Pc.triggered.connect(self.openTodoFrom)
        
        self.menuMTP.addAction(self.actionMulti_Task_Pc)
        self.menubar.addAction(self.menuMTP.menuAction())
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
       
        self.listWidget.setFont(font)
        self.listWidget_2.setFont(font)
        self.listWidget_3.setFont(font)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)
        self.label.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Serv Page"))
        self.label.setText(_translate("MainWindow", "Liste d\'ordinateurs éligibles"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.pushButton_3.setText(_translate("MainWindow", "Rajouter un ordinateur"))
        self.label_3.setText(_translate("MainWindow", "Liste de commandes crées"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Commande à réaliser"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label_4.setText(_translate("MainWindow", "Sujets d\'exécution"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Save"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Don\'t Save"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Nom d\'utilisateur"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Save"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Don\'t Save"))
        self.menuMTP.setTitle(_translate("MainWindow", "MTP"))
        self.actionMulti_Task_Pc.setText(_translate("MainWindow", "Multi Task/Pc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ServerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())