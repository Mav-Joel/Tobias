#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import os
import mysql.connector
from Block import blockWindow
from Bibliotheque.DBook import Database
from Bibliotheque.TBook import Tools
from Lookfor import LookforWindow
from Quickset import Quickset1Window
from QuicksetS import Quickset2Window

from Bibliotheque.TBook import Tools

class creatorWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")
        self.fill()

    def fill(self):
        self.primaryContent=[]
        self.secondaryContent=[]
        self.featureContent=[]
        self.globalContent=[]
        self.globalPrimaryItems=[]
        self.Weird = []

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Primaire' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.primaryContent.append(lettre)

        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Secondaire' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.secondaryContent.append(lettre)


        Command.execute("USE tobiasdb") 
        Command.execute("SELECT name FROM creator")

        for x in Command:
            for lettre in x :
                self.globalContent.append(lettre)

        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE type='Feature'")

        for x in Command:
            for lettre in x :
                self.featureContent.append(lettre)

        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Primaire'")

        for x in Command:
            for lettre in x :
                self.globalPrimaryItems.append(lettre)
        
        # for i in range(0,len(self.primaryContent)):
        #     self.listWidget.insertItem(i,self.primaryContent[i])
      
        # for y in range(0,len(self.secondaryContent)):
        #     self.listWidget_3.insertItem(y,self.secondaryContent[y])

        # for z in range(0,len(self.featureContent)):
        #     self.listWidget_4.insertItem(z,self.featureContent[z])

    def pattern(self):
        argsList = []
        
        #Récupérer le pattern
        newPattern = input("Commande \n")

        for caracters in newPattern : 
            argsList.append(caracters)

        #Trouver la position des arguments
        List = []
        argument = [] #Put arguments inside
        found = 0
        position = 0

        print(argsList)

        for elements in range (0,len(argsList)):
            if argsList[elements] == "$" : 
                List.append(position)

                found = found + 1
                position = position + 1

            else : 
                position = position + 1

        for case in range (0,len(argsList)) : 
            for i in range (0,len(List)):
                argsList[List[i]]  = argument[i]
                argsList[List[i]+1]  = "toremove"
                    
    def openQSW2(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = Quickset2Window()
        self.ui.setupUi(self.window)
        self.window.show() 
    
    def openQSW1(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = Quickset1Window()
        self.ui.setupUi(self.window)
        self.window.show()  

    def openLfW(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = LookforWindow()
        self.ui.setupUi(self.window)
        self.window.show()  
    
    def openWindows(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = blockWindow()
        self.ui.setupUi(self.window)
        self.window.show()
     
    def save(self):
        indexObjets = []
        nObjets = self.listWidget_2.count()

        #Récupérer les éléments
        for i in range(0,nObjets):
            items = self.listWidget_2.item(i).text()
            indexObjets.append(items)

        if nObjets > 0:
            Command = mydb.cursor() 
            Command.execute("USE tobiasdb") 
            
            for items in indexObjets:
                Command.execute("INSERT INTO creator (id , name , type , command , category) VALUES (NULL , '{}' , 'Feature' , '{}', 'Primaire')".format(self.lineEdit.text(),items))
                mydb.commit()
                    
    def execute(self):
        firstStageCommands=[]
        commandstoExecute=[]
        

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )
        
        #Déterminer les éléments de type Fonctionnalité
        for i in range(0,len(self.featureContent)-1):
            items = self.listWidget_2.item(i).text()

            Command = mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='{}'".format(items)) 

            for x in Command:
                for lettre in x :
                    #Interpretes them into commands
                    firstStageCommands.append(lettre)
                    print(firstStageCommands)
                    
        #Déterminer les commandes de ces éléments
             
        for i in range(0,len(firstStageCommands)):
            Command = mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='"+firstStageCommands[i]+"' AND type='Bloc'") 
            for x in Command:   
                for lettre in x :
                    commandstoExecute.append(lettre)
                    print(commandstoExecute)
                
        #Executes them
        print(commandstoExecute)
        list_of_strings = [str(s) for s in commandstoExecute]
        joined_string = " ".join(list_of_strings)
        print(joined_string)

        os.system(joined_string)

    def getItems(self):
        Commande=[]
        indexObjets = []
        nObjets = self.listWidget_2.count()

        for i in range(0,nObjets):
            items = self.listWidget_2.item(i).text()
            indexObjets.append(items)

        if nObjets > 0:

            for item in indexObjets :

                print ("Nom du bloc = ",item)

                Command = mydb.cursor() 
                Command.execute("USE tobiasdb") 
                Command.execute(f"SELECT command FROM creator WHERE name='{item}'")

                for x in Command:
                    for lettre in x :                            
                        Commande.append(lettre)
                    
                result = Database("creator","command","name",f"{item}").getFromDatabase()
                
                #L'item n'a pas de commande , il sera donc executé comme un argument étrangé
                
                if result is None : 
                    Commande.append(str(item))
                    print("L'item : "+item+" A été rajouté en temps qu'argument")

                list_of_strings = [str(s) for s in Commande]
                joined_string = " ".join(list_of_strings)
                
                argsList = []
        
                #Récupérer le pattern
                newPattern = joined_string

                for caracters in newPattern : 
                    argsList.append(caracters)

                #Trouver la position des arguments
                List = []
                found = 0
                position = 0
                argument = [] #Put arguments inside
                for l in range(1,len(Commande)) : 
                    print(argument)
                    argument.append(l)

                for elements in range (0,len(argsList)):
                    if argsList[elements] == "$" : 
                        List.append(position)

                        found = found + 1
                        position = position + 1

                    else : 
                        position = position + 1

              
                for case in range (0,len(argsList)) : 
                    for i in range (0,len(List)):
                        argsList[List[i]]  = argument[i]
                        argsList[List[i]+1]  = "toremove"
                            
                        

            #Execution
            # print(Commande)

            # list_of_strings = [str(s) for s in Commande]
            
            # print(list_of_strings)

            # joined_string = " ".join(list_of_strings)
            
            # print(joined_string)

            # os.system(joined_string)

    def setupUi(self, creatorWindow):
        creatorWindow.setObjectName("creatorWindow")
        creatorWindow.resize(923, 762)
        self.centralwidget = QtWidgets.QWidget(creatorWindow)
        self.centralwidget.setObjectName("centralwidget")
      
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 110, 351, 231))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDragEnabled(True)

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(470, 30, 421, 591))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setAcceptDrops(True)
        self.listWidget_2.setDragEnabled(True)
        
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 390, 351, 131))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setDragEnabled(True)

        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(30, 570, 351, 131))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.setAcceptDrops(True)
        self.listWidget_4.setDragEnabled(True)
       
        #Insert

        for i in range(0,len(self.primaryContent)):
            self.listWidget.insertItem(i,self.primaryContent[i])
      
        for y in range(0,len(self.secondaryContent)):
            self.listWidget_3.insertItem(y,self.secondaryContent[y])

        for z in range(0,len(self.featureContent)):
            self.listWidget_4.insertItem(z,self.featureContent[z])
       
      
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 620, 211, 31))
        self.pushButton.setObjectName("pushButton")
       
        self.pushButton.clicked.connect(self.getItems)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 101, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindows)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 430, 51, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openQSW2)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 670, 101, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.save)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 620, 211, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.execute)
       
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 20, 131, 34))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openLfW)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 210, 51, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openQSW1)
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 101, 18))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 370, 111, 18))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 550, 101, 18))
        self.label_3.setObjectName("label_3")
      
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 10, 101, 18))
        self.label_4.setObjectName("label_4")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 670, 241, 32))
        self.lineEdit.setObjectName("lineEdit")
       
        creatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(creatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 30))
        self.menubar.setObjectName("menubar")
        creatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(creatorWindow)
        self.statusbar.setObjectName("statusbar")
        creatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(creatorWindow)
        QtCore.QMetaObject.connectSlotsByName(creatorWindow)

    def retranslateUi(self, creatorWindow):
        _translate = QtCore.QCoreApplication.translate
        creatorWindow.setWindowTitle(_translate("creatorWindow", "creatorWindow"))
        self.pushButton.setText(_translate("creatorWindow", "Exécuter"))
        self.pushButton_2.setText(_translate("creatorWindow", "Créer un bloc"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Ctrl+b"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("creatorWindow", "Sauvegarder"))
        self.pushButton_5.setText(_translate("creatorWindow", "Exécuter une fonctionnalité"))
        self.pushButton_6.setText(_translate("MainWindow", "Base de données"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("creatorWindow", "Bloc Primaire"))
        self.label_2.setText(_translate("creatorWindow", "Bloc Secondaire"))
        self.label_4.setText(_translate("creatorWindow", "Workspace"))
        self.label_3.setText(_translate("creatorWindow", "Fonctionnalités"))
        self.lineEdit.setPlaceholderText(_translate("creatorWindow", "Nom de la fonctionnalité à sauvegarder"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = creatorWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
