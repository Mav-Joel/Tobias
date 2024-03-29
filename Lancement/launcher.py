#!/usr/bin/env python3
#-*-coding:utf-8-*-

import subprocess
import os
import getpass
import sys
user=os.environ["USER"]
import json
Utilisateur=os.environ["USER"]
sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi")
from Library.DBook import Database
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Locker")

class firstPart():
    
    def __init__(self):
        
        self.MagicWord = self.getModuleData("localDbPassword","Tobias")
        self.user = os.environ["USER"]
        self.name = subprocess.getoutput("hostname")


    def getModuleData(self,searchingFor,fieldName='user'):
        self.confs = Database().getPaths('path','ConfigurationJson')
        with open(self.confs,"r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def fromZeroToHero(self):

        """Install needed packages"""
        packages = [  
            "python-nmap",
            "PyQt5",
            "notify2",
            "django",
            "django-debug-toolbar",
            "gtts",
            "pyshark",
            "nginx",
            "speechRecognition" ,
            "paramiko",
            "install --pre scapy[basic]",
            "mechanicalsoup",
            "beautifulsoup4",
            "git",
            "pandas",
            "unidecode"
        ]

        for i in range (0,len(packages)):
            a = subprocess.getoutput(f"which {packages[i]}")
            if a != f"/usr/bin/{packages[i]}" :
                #print(f"{packages[i]} is not installed")
                os.system(f"pip3 install {packages[i]}")

    def createDatabases(self):

        import mysql
        import mysql.connector

        """Creates and configures the needed Databases"""

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=self.MagicWord,
            port="8889",
        )

        Command = mydb.cursor()
        Command.execute("CREATE DATABASE IF NOT EXISTS tobiasdb")


        Command = mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute(" \
        CREATE TABLE IF NOT EXISTS creator( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        name VARCHAR(100) NOT NULL, \
        type VARCHAR(100) NOT NULL, \
        command VARCHAR(100) NOT NULL, \
        category VARCHAR(100) NOT NULL, \
        pattern INT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS server( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        ipAddress VARCHAR(100) NOT NULL, \
        Password VARCHAR(100) NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS backbone( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        statut VARCHAR(100) NOT NULL, \
        ipAddress LONGTEXT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS coffreFort( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        name VARCHAR(50) NOT NULL, \
        Information LONGTEXT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS violet( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        name VARCHAR(50) NOT NULL, \
        username VARCHAR(100) NOT NULL, \
        address VARCHAR(50) NOT NULL, \
        type VARCHAR(100) NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS servCommands( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        Information LONGTEXT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS passwords( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        Information VARCHAR(300) NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS rapportExecution( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        Programme VARCHAR(50) NOT NULL, \
        Information LONGTEXT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS reseau( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        Network VARCHAR(200) NOT NULL, \
        Programme VARCHAR(200) NOT NULL, \
        Nature VARCHAR(100) NOT NULL, \
        Information LONGTEXT NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(f" \
        CREATE TABLE IF NOT EXISTS {self.name}( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        name VARCHAR(100) NOT NULL, \
        field VARCHAR(100) NOT NULL, \
        data VARCHAR(500) NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS knownIps( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        hostname VARCHAR(50) NOT NULL, \
        address VARCHAR(250) NOT NULL, \
        PRIMARY KEY (id) \
        )")

        Command.execute(" \
        CREATE TABLE IF NOT EXISTS unknownIps( \
        id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        address VARCHAR(250) NOT NULL, \
        PRIMARY KEY (id) \
        )")
   
    def rsaKeys(self):
        """Creates keys if you don't have rsa keys"""
        try :
            with open("/Users/{}/.ssh/id_rsa.pub".format(self.user),"r") :
                pass
        except IOError:
            a = input("Aucun fichier de clées trouvé , voulez vous créer un couple de clé rsa ?[yes/no]")

            if a == "yes" :
                b = input("Taille ? \n> ")
                os.system(f"ssh-keygen -t rsa -b {b}")

class window(object):

    def storeData(self):
        from Locker import toHash
        import hashlib
        import sys
        sys.path.insert(1,"/Users/joel/Archetype/Tobi")
        from Library.DBook import Database
        self.confs = Database().getPaths('path','ConfigurationJson')
        self.networkCSV = Database().getPaths('path','NetworkCSV')
        import json

        #Hash
        Mot_de_passe_Entre=(self.lineEdit_2.text())
        Mot_de_passe_Entre=Mot_de_passe_Entre.encode()
        Mot_de_passe_chiffre = hashlib.sha1(Mot_de_passe_Entre).hexdigest()

        Database("passwords","id","Information","NULL","{}".format(Mot_de_passe_chiffre)).insertInDatabase()

        #Conserver en fichier json
        newConfig = {

            "Configurations": [
                {
                    "Backbone": {

                        "ipScan" : "False",
                        "networkSpace" : "False" ,
                        "allow/Deny access" : "False"

                    },

                    "Riot": {

                        "authorized_keys" : "False",
                        "crontabCheck" : "False",
                        "connexions" : "False",
                        "processus" : "False"

                    },

                    "General" : {

                        "AllyComputer" : "False" ,
                        "Internet Protocol" : "False" ,
                        "Langue" : "FR"

                    },

                    "user": {
                        "name": self.lineEdit.text(),
                        "prenom": self.lineEdit_3.text(),
                        "phone number" : self.lineEdit_4.text(),
                        "adresse mail" : self.lineEdit_5.text(),
                        "password" : toHash.HASH(self.lineEdit_2.text())
                    },

                    "Tobias" : {
                        "name": "MainTobias",
                        "localDbPassword" : self.lineEdit_2.text(),
                        "MainServer": self.lineEdit_6.text()
                    }
                }
            ]
        }
        with open(self.confs,"w") as config :
            json.dump(newConfig,config,indent=2)

        with open(self.networkCSV,"w") as variable :
            variable.write("address,state,action")
            variable.write("\n0.0.0.0,CONNECTED,TELL")

    def setupUi(self, MainWindow):
        from PyQt5 import QtCore, QtGui, QtWidgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 481, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 60, 421, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 221, 18))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 150, 481, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 221, 18))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 113, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 40, 113, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 40, 113, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 80, 411, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 280, 481, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 241, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 50, 351, 32))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 410, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.storeData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        from PyQt5 import QtCore

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Mot de Passe"))
        self.label.setText(_translate("MainWindow", "Informations de connexion à Tobias"))
        self.label_2.setText(_translate("MainWindow", "Informations de complémentaire"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nom "))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Prenom"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Téléphone"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Adresse Mail"))
        self.label_3.setText(_translate("MainWindow", "Système de Base de données à utiliser"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Adresse Serveur de Backup"))
        self.pushButton.setText(_translate("MainWindow", "Valider"))

def PromptWindow():
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   