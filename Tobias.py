#!/usr/bin/env python3
#-*-coding:utf-8-*-
import getpass
import os
import subprocess   
import sys
import json
import threading
 
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Security")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Library")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/creatorFiles")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/System")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Violet")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Web")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Archives")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/customDB")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Gui")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Lancement")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Locker")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Settings")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/sysCommands")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/System")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Violet")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Web")


Utilisateur=os.environ["USER"]

class Ui_MainWindow(object):

    def __init__(self):

        import mysql
        import mysql.connector
        from Library.TBook import Tools
        
        magicWords=Tools().getModuleData("localDbPassword","Tobias")
        print(magicWords)
        #Display
        self.featureContent=[]
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=magicWords,
        port="8889",
        )

        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE type='Feature'")

        for x in Command:
            for lettre in x :
                self.featureContent.append(lettre)

    def start(self):
        import mysql
        import mysql.connector

        getCommands = []
        toDo = []
        item = self.listWidget.currentItem()
      
        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT command FROM creator WHERE type='Feature' AND name='{}'".format(item.text()))
        for x in Command : 
            for lettre in x : 
                pass
        

        lettre = str(lettre)
        lettre = lettre.strip("[]")
        lettre = lettre.replace("',","")
        lettre = lettre.replace("'","")
        lettre = lettre.split()

        for i in range(0,len(lettre)):
            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb") 
            Command.execute("SELECT command FROM creator WHERE name='{}'".format(lettre[i]))
            for x in Command : 
                for lettre in x : 
                    toDo.append(lettre)
       
        list_of_strings = [str(s) for s in toDo]
        joined_string = " ".join(list_of_strings)

        print(joined_string)
        os.system(joined_string) 

    def openLfW(self):
        from Lookfor import LookforWindow
        from PyQt5 import QtCore, QtGui, QtWidgets

    
        self.window = QtWidgets.QMainWindow()
        self.ui = LookforWindow()
        self.ui.setupUi(self.window)
        self.window.show()  

    def openTransfer(self):
        from Lookfor import LookforWindow
        from PyQt5 import QtCore, QtGui, QtWidgets

    
        self.window = QtWidgets.QMainWindow()
        self.ui = LookforWindow()
        self.ui.setupUi(self.window)
        self.window.show()  

    def openRapportWindow(self):
        from PyQt5 import QtCore, QtGui, QtWidgets
        from Rapport import rapportWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = rapportWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openConfigWindow(self):
        from Page_Configuration import confWIndow
        from PyQt5 import QtCore, QtGui, QtWidgets


        self.window = QtWidgets.QMainWindow()
        self.ui = confWIndow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openServerWindow(self):
        from Page_Serveur import ServerWindow
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.window = QtWidgets.QMainWindow()
        self.ui = ServerWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openTodoFrom(self):
        from ToDoFrom import toDoFromWindow
        from PyQt5 import QtCore, QtGui, QtWidgets


        self.window = QtWidgets.QMainWindow()
        self.ui = toDoFromWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMail(self):
        from SendMail import sendMailWindow
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.window = QtWidgets.QMainWindow()
        self.ui = sendMailWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openPacketWindow(self):
        Utilisateur=os.environ["USER"]
        sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi")
        from Library.DBook import Database
        
        path = Database().getPaths('packets','Executables')
        print("Please write your password in the terminal")
        os.system(f"{path}")

    def openHandlerMainWindow(self):
        from Handler import handlerWindow 
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.window = QtWidgets.QMainWindow()
        self.ui = handlerWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openRawMainWindow(self):
        from Raw import RawWindow 
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.window = QtWidgets.QMainWindow()
        self.ui = RawWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openArchive(self):
        from Archives.Archivist import Archivisty
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.window = QtWidgets.QMainWindow()
        self.ui = Archivisty()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openPageStockageMainWindow(self):
        from Page_Stockage import pageStockageMainWindow
        from PyQt5 import QtCore, QtGui, QtWidgets
        
        self.window = QtWidgets.QMainWindow()
        self.ui = pageStockageMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def opencreatorWindow(self):
        from Creator import creatorWindow
        from PyQt5 import QtCore, QtGui, QtWidgets
        
        self.window = QtWidgets.QMainWindow()
        self.ui = creatorWindow()
        self.ui.setupUi(self.window)
        self.window.show()
 
    def openNotesWindow(self):
        from Notes import notesWindow
        from PyQt5 import QtCore, QtGui, QtWidgets
        
        self.window = QtWidgets.QMainWindow()
        self.ui = notesWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindows(self):
        from Page_Reseau import pageReseauUI
        from PyQt5 import QtCore, QtGui, QtWidgets
        
        self.window = QtWidgets.QMainWindow()
        self.ui = pageReseauUI()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        from PyQt5 import QtCore, QtGui, QtWidgets
        sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi")
        from Library.DBook import Database
        image = Database().getPaths('icon','Images')
     
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 177)
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
       
        self.label.setFont(font)
        self.label.setObjectName("label")
          
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 10, 261, 111))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.start)

        for i in range(0,len(self.featureContent)):
            self.listWidget.insertItem(i,self.featureContent[i])
      
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1049, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setNativeMenuBar(False)
        
        self.menuOutils = QtWidgets.QMenu(self.menuBar)
        self.menuOutils.setObjectName("menuOutils")
      
        self.menuR_seau = QtWidgets.QMenu(self.menuBar)
        self.menuR_seau.setObjectName("menuR_seau")
      
        self.menuStockage = QtWidgets.QMenu(self.menuBar)
        self.menuStockage.setObjectName("menuStockage")
       
        self.menuServeur = QtWidgets.QMenu(self.menuBar)
        self.menuServeur.setObjectName("menuServeur")
      
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
       
        self.menuCreator = QtWidgets.QMenu(self.menuBar)
        self.menuCreator.setObjectName("menuCreator")
        
        MainWindow.setMenuBar(self.menuBar)
       
        self.actionBloc_Note = QtWidgets.QAction(MainWindow)
        self.actionBloc_Note.setObjectName("actionBloc_Note")
        self.actionBloc_Note.triggered.connect(self.openNotesWindow)

        self.actionArchiver = QtWidgets.QAction(MainWindow)
        self.actionArchiver.setObjectName("actionArchiver")
        self.actionArchiver.triggered.connect(self.openArchive)

        self.actionMail = QtWidgets.QAction(MainWindow)
        self.actionMail.setObjectName("actionMail")
        self.actionMail.triggered.connect(self.openMail)
       
        self.actionRecherche = QtWidgets.QAction(MainWindow)
        self.actionRecherche.setObjectName("actionRecherche")
       
        self.actionCoffre_Fort = QtWidgets.QAction(MainWindow)
        self.actionCoffre_Fort.setObjectName("actionCoffre_Fort")
        self.actionCoffre_Fort.triggered.connect(self.openPageStockageMainWindow)
        
        self.actionArchiver_2 = QtWidgets.QAction(MainWindow)
        self.actionArchiver_2.setObjectName("actionArchiver_2")
        # self.actionArchiver_2.triggered.connect()
        
        self.actionLobby = QtWidgets.QAction(MainWindow)
        self.actionLobby.setObjectName("actionLobby")
        self.actionLobby.triggered.connect(self.openServerWindow)
       
        self.actionLobby_2 = QtWidgets.QAction(MainWindow)
        self.actionLobby_2.setObjectName("actionLobby_2")
        self.actionLobby_2.triggered.connect(self.openWindows)

        self.actionPaquets = QtWidgets.QAction(MainWindow)
        self.actionPaquets.setObjectName("actionPaquets")
        self.actionPaquets.triggered.connect(self.openPacketWindow)
      
        self.actionHandler = QtWidgets.QAction(MainWindow)
        self.actionHandler.setObjectName("actionHandler")
        self.actionHandler.triggered.connect(self.openHandlerMainWindow)
        
        self.actionRaw = QtWidgets.QAction(MainWindow)
        self.actionRaw.setObjectName("actionRAw")
        self.actionRaw.triggered.connect(self.openRawMainWindow)
        
        self.actionH_berger = QtWidgets.QAction(MainWindow)
        self.actionH_berger.setObjectName("actionH_berger")
        self.actionH_berger.triggered.connect(self.openTransfer)
        
        self.actionModifier_le_fichier_de_configuration = QtWidgets.QAction(MainWindow)
        self.actionModifier_le_fichier_de_configuration.setObjectName("actionModifier_le_fichier_de_configuration")
        self.actionModifier_le_fichier_de_configuration.triggered.connect(self.openConfigWindow)
       
        self.actionPage_Createur = QtWidgets.QAction(MainWindow)
        self.actionPage_Createur.setObjectName("actionPage_Createur")
        self.actionPage_Createur.triggered.connect(self.opencreatorWindow)
        
        self.actionVoice_Feedback = QtWidgets.QAction(MainWindow)
        self.actionVoice_Feedback.setObjectName("actionVoice_Feedback")
        self.actionVoice_Feedback.triggered.connect(self.openRapportWindow)
      
        self.menuOutils.addAction(self.actionBloc_Note)

        self.menuOutils.addAction(self.actionHandler)
        self.menuOutils.addAction(self.actionRaw)
       
        self.menuR_seau.addAction(self.actionLobby_2)
        self.menuR_seau.addAction(self.actionPaquets)
       
        self.menuStockage.addAction(self.actionCoffre_Fort)
        self.menuStockage.addAction(self.actionArchiver)

        
        self.menuServeur.addAction(self.actionLobby)
        self.menuServeur.addAction(self.actionH_berger)
        
        self.menuComputers = QtWidgets.QMenu(self.menuBar)
        self.menuComputers.setObjectName("menuComputers")
        
        self.menuConfiguration.addAction(self.actionModifier_le_fichier_de_configuration)
        self.menuConfiguration.addAction(self.actionVoice_Feedback)
        self.menuCreator.addAction(self.actionPage_Createur)
        
        self.actionComputers = QtWidgets.QAction(MainWindow)
        self.actionComputers.setObjectName("actionComputers")
        self.menuComputers.addAction(self.actionComputers)
        
        self.menuBar.addAction(self.menuOutils.menuAction())
        self.menuBar.addAction(self.menuR_seau.menuAction())
        self.menuBar.addAction(self.menuStockage.menuAction())
        self.menuBar.addAction(self.menuServeur.menuAction())
        self.menuBar.addAction(self.menuConfiguration.menuAction())
        self.menuBar.addAction(self.menuCreator.menuAction())
        self.menuBar.addAction(self.menuComputers.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        from PyQt5 import QtCore
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias"))
        self.label.setText(_translate("MainWindow", "Bonjour Joel"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuR_seau.setTitle(_translate("MainWindow", "Réseau"))
        self.menuStockage.setTitle(_translate("MainWindow", "Stockage"))
        self.menuServeur.setTitle(_translate("MainWindow", "Serveur"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuCreator.setTitle(_translate("MainWindow", "Createur"))
        
        self.actionBloc_Note.setText(_translate("MainWindow", "Bloc Note"))
        self.actionBloc_Note.setStatusTip(_translate("MainWindow", "Opens the Bloc Note"))
        self.actionBloc_Note.setShortcut(_translate("MainWindow", "Ctrl+n"))

        self.actionMail.setText(_translate("MainWindow", "Mail"))
        self.actionRecherche.setText(_translate("MainWindow", "Recherche"))
        self.actionCoffre_Fort.setText(_translate("MainWindow", "Coffre Fort"))
        
        self.actionLobby.setText(_translate("MainWindow", "Page Server"))
        
        self.actionLobby_2.setText(_translate("MainWindow", "Page Réseau"))
        self.actionLobby_2.setShortcut(_translate("MainWindow", "Ctrl+r"))

        self.actionPaquets.setText(_translate("MainWindow", "Paquets"))
        self.actionHandler.setText(_translate("MainWindow", "Handler"))
        self.actionRaw.setText(_translate("MainWindow", "Raw"))
        self.actionArchiver.setText(_translate("MainWindow", "Archiver"))
        self.actionH_berger.setText(_translate("MainWindow", "Transférer"))
        self.actionModifier_le_fichier_de_configuration.setText(_translate("MainWindow", "Modifier le fichier de configuration"))
        self.actionPage_Createur.setText(_translate("MainWindow", "Page Createur"))
        self.actionPage_Createur.setShortcut(_translate("MainWindow", "Ctrl+w"))
        self.actionVoice_Feedback.setText(_translate("MainWindow", "Voice Feedback"))
        self.menuComputers.setTitle(_translate("MainWindow", "Nodes"))
        self.menuComputers.setTitle(_translate("MainWindow", "Nodes"))
        self.actionComputers.setText(_translate("MainWindow", "Computers"))

class ByPass(Ui_MainWindow):

    def login(self):
        from PyQt5 import QtCore, QtGui, QtWidgets

        if self.lineEdit_2.text() == "Joel":
            if self.lineEdit.text() == "Joel":
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.close()
                self.window.show()  
            
            else : 
                    print("WRONG PASSWORD")
                    sys.exit(0)
        else :
            print("WRONG PASSWORD")
            sys.exit(0)

    def setupUi(self, MainWindow):
        sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi")
        from Library.DBook import Database
        image = Database().getPaths('icon','Images')

        self.MainWindow = MainWindow
        from PyQt5 import QtCore, QtGui, QtWidgets
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 40, 221, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 221, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit.returnPressed.connect(self.login)
        self.pushButton.clicked.connect(self.login)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 161, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(image))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(150, 160, 105, 22))
        self.radioButton.setObjectName("radioButton")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.radioButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
       
        self.lineEdit_2.setFont(font)
        self.lineEdit.setFont(font)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        from PyQt5 import QtCore
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Authentification"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.radioButton.setText(_translate("MainWindow", "Keep Token"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

class Tobias(ByPass):
    
    def __init__(self):
        from Library.DBook import Database        
        self.confs = Database().getPaths('path','ConfigurationJson')
        self.networkB = Database().getPaths('network','sysCommandsDirectory')
        from PyQt5 import QtCore, QtGui, QtWidgets

        self.user=os.environ["USER"] #User's name
        
        try : 
            open(f"/Users/{self.user}/Archetype/Tobi/.started.txt")
        
        except IOError:  

                self.firstStartSequence() #Working
                    
        #Launching Sequence
        if len(sys.argv) > 1 :
            if sys.argv[1] == "Terminal" :
                # self.terminalMode()
                pass
            elif sys.argv[1] == "Reload" :
                from Riot import Security
                Security().reload()

        else :

            self.threadLoop()
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = ByPass()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
               
    def threadLoop(self):
        import threading

        mon_thread=threading.Thread(target=self.loopSequence)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre
            
    def firstStartSequence(self):
        from launcher import firstPart,PromptWindow
        from Library.NBook import Network
        from Library.DBook import Database
        from Backbone import Backbone
        from Riot import Security
        from PyQt5 import QtCore, QtGui, QtWidgets

        databasePassword = getpass.getpass("Mot de passe de base de donnée : ")
        os.environ['MDP'] = databasePassword
        newConfig = {
        "Configurations": [
            {
            "Backbone": {
                "ipScan": "False",
                "networkSpace": "False",
                "allow/Deny access": "False"
            },
            "Riot": {
                "authorized_keys": "False",
                "crontabCheck": "False",
                "connexions": "False",
                "processus": "False"
            },
            "General": {
                "AllyComputer": "False",
                "Internet Protocol": "False",
                "Langue": "FR"
            },
            "user": {
                "name": "Toula",
                "prenom": "Joel",
                "phone number": "0694232624",
                "adresse mail": "joel.toula@gmail.com"
            },
            "Tobias": {
                "name": "MainTobias",
                "localDbPassword": databasePassword
            }
            }
        ]
        }
        with open(f"{self.confs}","w") as config :
            json.dump(newConfig,config,indent=2)
        
        print("Launching startSequence")

        """ Execute the Start Sequence everytime Tobias is summoned 
            Make sure the packages are here and configure what needs to be for the first start """
        
        #Get the Basic install for Tobias
        firstPart().fromZeroToHero() 

        #Creates and deploy databases
        firstPart().createDatabases() #Works
        
        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"Tobias","currentIp",Network().myIp("ip")).insertInDatabase()
        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"Tobias","Liaison SSH Etablie","0").insertInDatabase()
        Database("reseau","id","Network","Programme","Nature","Information","NULL",Network().myIp("ip"),"Tobias","previousIp",Network().myIp("ip")).insertInDatabase()
        Database("rapportExecution","id","Programme","Information","NULL","firstStart","Online").insertInDatabase()

       
        #First Start interface and input password
        Database("backbone","id","statut","ipAddress","NULL","Allowed",f"{Network().myIp('ip')}").insertInDatabase()

        #Creates rsa'keys
        firstPart().rsaKeys()
        
        #Port Scan
        Backbone().getMyPorts()

        #Get the athorized_keys file copy
        Security().initialisationAutorizedKeys()

        #Get the Crontab file copy
        Security().initialisationCrontab()


        #Get the diffrent ips on my network
        Network().currentNH(Network().myIp("ip"))

        #Do an in-depth check on the ips
        Network().networkScan(Network().myIp("ip"))

        with open(f"/Users/{self.user}/Archetype/Tobi/.started.txt","w") as variable :
                variable.write("Started")

        PromptWindow()
        
    def loopSequence(self):

        import time
        from multiprocessing import Process
        from RawNetwork import Ally_Computers,internetProtocol
        from Backbone import Backbone
        from Riot import Security
        from Library.NBook import Network


        """ Execute every methods in order to make them properly available to the user """
               
        print("Launching loopSequence")
        
       
        while True :

            #BackBone
            if self.getModuleData("ipScan","Backbone") == "True" :
                loopBackboneIpScan = threading.Thread(target=Backbone().innerPortScan())
                loopBackboneIpScan.start()


            if self.getModuleData("networkSpace","Backbone") == "True" :
                loopBackboneNetworkSpace = threading.Thread(target=Backbone().networkSpace())
                loopBackboneNetworkSpace.start()
            
            if self.getModuleData("allow/Deny access","Backbone") == "True" :
                loopBackbone = threading.Thread(target=Backbone().Etapes_de_Fonctionnement())
                loopBackbone.start()

            # Riot 
            if self.getModuleData("authorized_keys","Riot") == "True" :
                loopRiot = threading.Thread(target=Security().autorized_keysCheck())
                loopRiot.start()

            # if self.getModuleData("crontabCheck","Riot") == "True" :
            #     print("starting")   
            #     loopCrontab = threading.Thread(target=Security().crontabCheck())
            #     loopCrontab.start()
    
            if self.getModuleData("connexions","Riot") == "True" :
                loopRiot = threading.Thread(target=Security().connexion())
                loopRiot.start()
    
            if self.getModuleData("processus","Riot") == "True" :
                loopRiotProc = threading.Thread(target=Security().Processus())
                loopRiotProc.start()
            
            #RawNetwork
          #  if self.getModuleData("AllyComputer","General") == "True" :
           #     self.threads(Ally_Computers().Main())
    
            if self.getModuleData("Internet Protocol","General") == "True" :
                loopRaw = threading.Thread(target=internetProtocol().Main())
                loopRaw.start()
            
            time.sleep(0.5)
            
    def stopSequence(self): 

        print("Launching stopSequence")

        """ Execute the stopSequence everytime the user wants to stop Tobias 
            Make sure everything is ready to be closed and close it """
        pass

    def rawMode(self):
        
        print("Launching Raw Mode")

        """ Arguments only Version of Tobias"""
        
        pass

    def getModuleData(self,searchingFor,fieldName='user'):
        import json
        with open(f"{self.confs}","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values


#Tobias Main Task
if __name__ == "__main__":
    Tobias()
        



