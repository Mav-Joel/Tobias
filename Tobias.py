#!/usr/bin/env python3
#-*-coding:utf-8-*-

""" Native modules importations"""

import os
import sys
import json 
import mysql
import mysql.connector

# from Backbone import *
from firstStart import PromptWindow
from firstStart import *
# from Riot import *

# from Bibliotheque.NBook import *
# from PyQt5 import QtCore, QtGui, QtWidgets
# from Page_Reseau import pageReseauUI
# from Page_Stockage import *
# from Notes import notesWindow
# from RawNetwork import *    
# from RawNetwork import internetProtocol  
# from Creator import creatorWindow
# from Page_Stockage import pageStockageMainWindow
# from importExport import importExportWindow
# from Handler import handlerWindow
# from SendMail import sendMailWindow
# from ToDoFrom import toDoFromWindow
# from Page_Serveur import ServerWindow
# from Page_Configuration import confWIndow
# from Rapport import rapportWindow
# from Lookfor import LookforWindow

user=os.environ["USER"] 
magicWords=os.environ["MDP"]

featureContent=[]

mydb = mysql.connector.connect(
host="localhost",
user="Python",
passwd=magicWords,
)

Command = mydb.cursor() 
Command.execute("USE tobiasdb") 
Command.execute("SELECT DISTINCT(name) FROM creator WHERE type='Feature'")

for x in Command:
    for lettre in x :
        featureContent.append(lettre)

class Ui_MainWindow(object):

    def start(self):
        getCommands = []
        toDo = []
        item = self.listWidget.currentItem()
      
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT command FROM creator WHERE type='Feature' AND name='{}'".format(item.text()))
        for x in Command : 
            for lettre in x : 
                getCommands.append(lettre)

        for i in range(0,len(getCommands)):
            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 
            Command.execute("SELECT command FROM creator WHERE name='{}'".format(getCommands[i]))
            for x in Command : 
                for lettre in x : 
                    toDo.append(lettre)
       
        list_of_strings = [str(s) for s in toDo]
        joined_string = " ".join(list_of_strings)
       
        os.system(joined_string) 


    def openLfW(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = LookforWindow()
        self.ui.setupUi(self.window)
        self.window.show()  

    def openRapportWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = rapportWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openConfigWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = confWIndow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openServerWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ServerWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openTodoFrom(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = toDoFromWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMail(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = sendMailWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openPacketWindow(self):
        print("Please write your password in the terminal")
        os.system("sudo /home/joel/Archétype/Tobi/packets.py")

    def openHandlerMainWindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = handlerWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openImportExportMainWindow(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = importExportWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPageStockageMainWindow(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = pageStockageMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def opencreatorWindow(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = creatorWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    
    def openNotesWindow(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = notesWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindows(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = pageReseauUI()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openFirstStart(self):
       
        self.window = QtWidgets.QMainWindow()
        self.ui = window()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 177)
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 81))
        
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
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

        for i in range(0,len(featureContent)):
            self.listWidget.insertItem(i,featureContent[i])
      
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1049, 30))
        self.menuBar.setObjectName("menuBar")
        
        self.menuOutils = QtWidgets.QMenu(self.menuBar)
        self.menuOutils.setObjectName("menuOutils")
      
        self.menuR_seau = QtWidgets.QMenu(self.menuBar)
        self.menuR_seau.setObjectName("menuR_seau")
      
        self.menuInternet = QtWidgets.QMenu(self.menuBar)
        self.menuInternet.setObjectName("menuInternet")
       
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
       
        self.actionImport_Export = QtWidgets.QAction(MainWindow)
        self.actionImport_Export.setObjectName("actionImport_Export")
        self.actionImport_Export.triggered.connect(self.openImportExportMainWindow)

        self.actionArchiver = QtWidgets.QAction(MainWindow)
        self.actionArchiver.setObjectName("actionArchiver")
       
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
        
        self.actionVeraCrypt = QtWidgets.QAction(MainWindow)
        self.actionVeraCrypt.setObjectName("actionVeraCrypt")
      
        self.actionH_berger = QtWidgets.QAction(MainWindow)
        self.actionH_berger.setObjectName("actionH_berger")
        
        self.actionModifier_le_fichier_de_configuration = QtWidgets.QAction(MainWindow)
        self.actionModifier_le_fichier_de_configuration.setObjectName("actionModifier_le_fichier_de_configuration")
        self.actionModifier_le_fichier_de_configuration.triggered.connect(self.openConfigWindow)
       
        self.actionPage_Createur = QtWidgets.QAction(MainWindow)
        self.actionPage_Createur.setObjectName("actionPage_Createur")
        self.actionPage_Createur.triggered.connect(self.opencreatorWindow)
        
        self.actionVoice_Feedback = QtWidgets.QAction(MainWindow)
        self.actionVoice_Feedback.setObjectName("actionVoice_Feedback")
        self.actionVoice_Feedback.triggered.connect(self.openRapportWindow)
      
        self.actionPage_Internet = QtWidgets.QAction(MainWindow)
        self.actionPage_Internet.setObjectName("actionPage_Internet")
       
        self.menuOutils.addAction(self.actionBloc_Note)

        self.menuOutils.addAction(self.actionImport_Export)
        self.menuOutils.addAction(self.actionHandler)
       
        self.menuR_seau.addAction(self.actionLobby_2)
        self.menuR_seau.addAction(self.actionPaquets)
       
        self.actionModifier_une_base_de_donn_e = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_base_de_donn_e.setObjectName("actionModifier_une_base_de_donn_e")
        
        self.menuInternet.addAction(self.actionMail)
        self.menuInternet.addAction(self.actionRecherche)
        self.menuInternet.addAction(self.actionPage_Internet)
       
        self.menuStockage.addAction(self.actionCoffre_Fort)
        self.menuStockage.addAction(self.actionArchiver_2)
        self.menuStockage.addAction(self.actionVeraCrypt)

        
        self.menuServeur.addAction(self.actionLobby)
        self.menuServeur.addAction(self.actionH_berger)
      
        self.menuConfiguration.addAction(self.actionModifier_le_fichier_de_configuration)
        self.menuConfiguration.addAction(self.actionVoice_Feedback)
        self.menuConfiguration.addAction(self.actionModifier_une_base_de_donn_e)

        self.menuCreator.addAction(self.actionPage_Createur)
      
        self.menuBar.addAction(self.menuOutils.menuAction())
        self.menuBar.addAction(self.menuR_seau.menuAction())
        self.menuBar.addAction(self.menuInternet.menuAction())
        self.menuBar.addAction(self.menuStockage.menuAction())
        self.menuBar.addAction(self.menuServeur.menuAction())
        self.menuBar.addAction(self.menuConfiguration.menuAction())
        self.menuBar.addAction(self.menuCreator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias"))
        self.label.setText(_translate("MainWindow", "Bonjour Joel"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuR_seau.setTitle(_translate("MainWindow", "Réseau"))
        self.menuInternet.setTitle(_translate("MainWindow", "Internet"))
        self.menuStockage.setTitle(_translate("MainWindow", "Stockage"))
        self.menuServeur.setTitle(_translate("MainWindow", "Serveur"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuCreator.setTitle(_translate("MainWindow", "Createur"))
        
        self.actionBloc_Note.setText(_translate("MainWindow", "Bloc Note"))
        self.actionBloc_Note.setStatusTip(_translate("MainWindow", "Opens the Bloc Note"))
        self.actionBloc_Note.setShortcut(_translate("MainWindow", "Ctrl+n"))

        self.actionImport_Export.setText(_translate("MainWindow", "Import/Export"))
        self.actionArchiver.setText(_translate("MainWindow", "getFromDB"))
        self.actionMail.setText(_translate("MainWindow", "Mail"))
        self.actionRecherche.setText(_translate("MainWindow", "Recherche"))
        self.actionCoffre_Fort.setText(_translate("MainWindow", "Coffre Fort"))
        
        self.actionArchiver_2.setText(_translate("MainWindow", "getFromDB"))
        self.actionArchiver_2.triggered.connect(self.openLfW)
        self.actionLobby.setText(_translate("MainWindow", "Page Server"))
        
        self.actionLobby_2.setText(_translate("MainWindow", "Page Réseau"))
        self.actionLobby_2.setShortcut(_translate("MainWindow", "Ctrl+r"))

        self.actionPaquets.setText(_translate("MainWindow", "Paquets"))
        self.actionHandler.setText(_translate("MainWindow", "Handler"))
        self.actionVeraCrypt.setText(_translate("MainWindow", "VeraCrypt"))
        self.actionH_berger.setText(_translate("MainWindow", "Transférer"))
        self.actionModifier_le_fichier_de_configuration.setText(_translate("MainWindow", "Modifier le fichier de configuration"))
        self.actionPage_Createur.setText(_translate("MainWindow", "Page Createur"))

        self.actionPage_Createur.setShortcut(_translate("MainWindow", "Ctrl+w"))
        self.actionPage_Internet.setText(_translate("MainWindow", "Page Internet"))

        self.actionVoice_Feedback.setText(_translate("MainWindow", "Voice Feedback"))
        self.actionModifier_une_base_de_donn_e.setText(_translate("MainWindow", "Modifier une base de donnée"))


class Tobias():
    
    user=os.environ["USER"] #User's name
    magicWords=os.environ["MDP"]
    
    def __init__(self):
       
        """Informations about Tobias displayed in the python interpreter """

        self.nom="Tobias"

    def firstStartSequence(self):
     
        print("Launching startSequence")

        """ Execute the Start Sequence everytime Tobias is summoned 
            Make sure the packages are here and configure what needs to be for the first start """
        
        #Install packages
        firstStart().fromZeroToHero() #Work in Progress
       
        #Creates and deploy databases
        firstStart().createDatabases() #Works
       
        #First Start interface and input password
        PromptWindow()

        #Creates rsa'keys
        firstStart().rsaKeys()
       
        #Port Scan
        Backbone.getMyPorts(Network.Mon_IP())

        #Get the athorized_keys file copy
        # Security.initialisationAutorizedKeys()

        #Get the Crontab file copy
        # Security.initialisationCrontab()

        #Get Network Informations , initialize values in the database
        os.system("/home/{}/Archétype/Tobi/systembuds/network.bash".format(self.user))

        #Get the diffrent ips on my network
        Network.Routine(Network.Mon_IP())

        #Do an in-depth check on the ips
        Network.Reseau(Network.Mon_IP())
        

    def startSequence(self):
        pass
        
    def threads(self,something):
        mon_thread=threading.Thread(target=something)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre


    def loopSequence(self):
        """ Execute every methods in order to make them properly available to the user """
        

        print("Launching loopSequence")
        
       
        while True :

            #BackBone
            if self.getModuleData("ipScan","Backbone") == "True" :
                self.threads(Backbone.ipScan(Network.Mon_IP()))

            if self.getModuleData("networkSpace","Backbone") == "True" :
                self.threads(Backbone.networkSpace())
            
            if self.getModuleData("allow/Deny access","Backbone") == "True" :
                self.threads(Etapes_de_Fonctionnement())

            #Riot
            if self.getModuleData("authorized_keys","Riot") == "True" :
                self.threads(Security.autorized_keysCheck())
            
            if self.getModuleData("crontabCheck","Riot") == "True" :
                self.threads(Security.crontabCheck())   
    
            if self.getModuleData("connexions","Riot") == "True" :
                self.threads(Security.connexion())
    
            if self.getModuleData("processus","Riot") == "True" :
                self.threads(Security.Processus())
            
            #RawNetwork
            if self.getModuleData("AllyComputer","General") == "True" :
                self.threads(Ally_Computers().Main())
    
            if self.getModuleData("Internet Protocol","General") == "True" :
                internetProtocol().Main()

            time.sleep(0.2)


    def stopSequence(self): 

        print("Launching stopSequence")

        """ Execute the stopSequence everytime the user wants to stop Tobias 
            Make sure everything is ready to be closed and close it """
        pass

    def reload(self):
        os.system("mysql -u Python -p$MDP -D tobiasdb -e 'DROP DATABASE tobiasdb'")

    def terminalMode(self):
        
        print("Launching Terminal Mode")

        """Terminal Version of Tobias"""

        pass
    
    def rawMode(self):
        
        print("Launching Raw Mode")

        """ Arguments only Version of Tobias"""
        
        pass
        
    #CONFIGURATIONS

    def getTextConfig(self):
        with open("/home/joel/Archétype/Tobi/Admin/Configurations.json","r") as variable :
            return variable.read()

    def getModuleData(self,searchingFor,fieldName='user'):
        with open("/home/joel/Archétype/Tobi/Admin/Configurations.json","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values


def threadLoop():
        mon_thread=threading.Thread(target=Tobias().loopSequence)   #définit la fonction a executer en arrière-plan
        mon_thread.start()    #lance la fonction, sans faire freeze la fenêtre


#Tobias Main Tasks
    
if __name__ == "__main__":
    if len(sys.argv) > 1 :
        if sys.argv[1] == "Start":
            Tobias().reload()
            Tobias().firstStartSequence() #Working
        elif sys.argv[1] == "Reload" :
            Tobias().reload()
        elif sys.argv[1] == "Config" :
            print(Tobias().getTextConfig())
    else :
        threadLoop()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())



