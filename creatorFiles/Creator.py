#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

import mysql
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout,
                             QListWidget, QListWidgetItem, QWidget)
from Lookfor import LookforWindow

sys.path.insert(1,"/home/joel/Archetype/Tobi")

from Library.DBook import Database
from Library.TBook import Tools


class creatorWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")
        self.previous = 0
        self.after = 0
    def createBloc(self):

        Database("creator","id","name","type","command","category","pattern","NULL",f"{self.lineEdit.text()}","Bloc",f"{self.lineEdit_6.text()}",f"{self.comboBox.currentText()}",f"{self.spinBox.value()}").insertInDatabase()
        Tools().Notification("Block Successfully Created")
       
        self.lineEdit_6.clear()
        self.lineEdit.clear()
        self.spinBox.setValue(0)
       
        self.fill()
        
    def filepicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.lineEdit_6.setText(fileName[0])

    def modify(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        name = self.lineEdit_2.text()
        name = name.split()
        name = name[2]
        
        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"UPDATE creator SET name='{name}' WHERE name='{name}'")
        self.mydb.commit()

        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"UPDATE creator SET category='{self.lineEdit_3.text()}' WHERE name='{name}'")
        self.mydb.commit()

        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"UPDATE creator SET command='{self.lineEdit_4.text()}' WHERE name='{name}'")
        self.mydb.commit()

        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"UPDATE creator SET pattern={self.lineEdit_5.text()} WHERE name='{name}'")
        self.mydb.commit()
        self.updateEdits()

    def takeOut(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def updateEdits(self):
        blocInfos = []
        
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"SELECT name,type,command,category,pattern FROM creator WHERE name='{self.listWidget.currentItem().text()}'")

        for x in Command:
            for lettre in x :
                blocInfos.append(lettre)

        self.lineEdit_2.setText("Nom : "+blocInfos[0]+" [Type : "+blocInfos[1].upper()+"]")
        self.lineEdit_3.setText(blocInfos[3])
        self.lineEdit_5.setText(str(blocInfos[4]))
        self.lineEdit_4.setText(blocInfos[2])

    def fill(self):
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.listWidget_5.clear()

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        self.primaryContent=[]
        self.secondaryContent=[]
        self.featureContent=[]
        self.globalContent=[]
        self.globalPrimaryItems=[]
        self.Weird = []
        self.scriptContent = []
       
       
        Command = self.mydb.cursor() 
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
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Script' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.scriptContent.append(lettre)

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
        
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.listWidget_5.clear()

        for i in range(0,len(self.primaryContent)):
            self.listWidget_2.insertItem(i,self.primaryContent[i])
      
        for y in range(0,len(self.secondaryContent)):
            self.listWidget_3.insertItem(y,self.secondaryContent[y])

        for y in range(0,len(self.scriptContent)):
            self.listWidget_4.insertItem(y,self.scriptContent[y])

        for z in range(0,len(self.featureContent)):
            self.listWidget_5.insertItem(z,self.featureContent[z])

    def openLfW(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = LookforWindow()
        self.ui.setupUi(self.window)
        self.window.show()  
    
    def save(self):
        indexObjets = []
        nObjets = self.listWidget.count()

        #Récupérer les éléments
        for i in range(0,nObjets):
            items = self.listWidget.item(i).text()
            indexObjets.append(items)

        if nObjets > 0:
            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb") 
            
            Command.execute(f"INSERT INTO creator (id , name , type , command , category,pattern) VALUES (NULL , '{self.lineEdit_7.text()}' , 'Feature' , \"{indexObjets}\", 'Primaire',0)")
            self.mydb.commit()
            Tools().Notification("Feature Successfully Added")
            self.fill()

    def execute(self):

        pattern = []

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )
        #Déterminer les éléments de type Fonctionnalité
        for i in range(0,self.listWidget.count()):
            item = self.listWidget.item(i).text()

            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='{}' AND category !='Script'".format(item)) 

            for x in Command:
                for lettre in x :
                    pass

            lettre = str(lettre)
            lettre = lettre.strip("[]")
            lettre = lettre.replace("',","")
            lettre = lettre.replace("'","")
            firstStageCommands = lettre.split()
                    
        #Déterminer les commandes de ces éléments
        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='"+firstStageCommands[i]+"' AND type='Bloc' AND category!='Script'") 
            for x in Command:   
                for lettre in x :
                    firstStageCommands[i] = lettre

        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='"+firstStageCommands[i]+"' AND type='Bloc' AND category='Script'") 
            for x in Command:   
                for lettre in x :
                    a = subprocess.getoutput(lettre)
                    firstStageCommands[i] = a
                    pattern.append(a)
                    
                    Command = self.mydb.cursor() 
                    Command.execute("USE tobiasdb")
                    Command.execute("SELECT pattern FROM creator WHERE command='"+lettre+"' AND type='Bloc' AND category='Script'") 
                    for x in Command:   
                        for lettre in x:
                            pattern.append(lettre)

        #Check for Pattern
        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor() 
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command,pattern FROM creator WHERE command='"+firstStageCommands[i]+"' AND type='Bloc' AND category='Secondaire'") 
            for x in Command:   
                for lettre in x :
                    pattern.append(lettre)
        

        list_of_strings = [str(s) for s in firstStageCommands]
        joined_string = " ".join(list_of_strings)
        string = joined_string.split()
        need = string[:len(pattern)+1]

        for i in range(len(string)):
            for y in range(0,len(pattern)):
                if string[i] == f"${pattern[y]}":
                    string[i] = pattern[y-1]
        
        good = []
        for i in string:
            if i not in good:
                good.append(i)
        
        string = good   

        #FETCH
        caracters = 0
        letters = []
        nums = []
        for i in range(0,len(string)):
            num = string[i].count("$")
        if num == 0 :
            toDO = " ".join(string)
            print(toDO)
            os.system(toDO)
        else : 
            for a in string[i]:
                letters.append(a)
            for a in string[i]:
                if "$" == a:
                    nums.append(caracters)
                    caracters = caracters+1 
                else : 
                    caracters = caracters+1 
            val = 0
            for h in range(0,len(nums)):
                letters.pop(nums[h]-val)
                val = val+1

            val_b = 0
            for m in range(0,len(nums)):
                nums[m] = nums[m]-val_b
                val_b= val_b+1

            for i in range(0,len(nums)):
                b = letters[nums[i]]
                for y in range(0,len(pattern)):
                    if int(b) == pattern[y]:
                        letters[nums[i]] = pattern[y-1]

            joined_string = "".join(letters)
            string[i] = joined_string

            result = len(string) - len(need)
            toDO = string[:-result]
            toDO = " ".join(toDO)
            print(toDO)
            os.system(toDO)
    
    



        # thing = []
        # for i in range(0,len(string)):
        #     for y in range(0,len(pattern)):
        #         if string[i] == str(pattern[y]):
        #             thing.append(string[i])

        # print(good)
        # print(thing)
        
        # yey = []
        # for i in string:
        #     if i not in good:        
        #         yey.append(i)

        # print(yey)
        # yey = " ".join(yey)
        # os.system(yey)


    def getItems(self):
        Commande=[]
        indexObjets = []
        
        nObjets = self.listWidget.count()
       
        if nObjets > 0:

            for i in range(0,nObjets):
                items = self.listWidget.item(i).text()
                indexObjets.append(items)

            for item in indexObjets :

                Command = self.mydb.cursor() 
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
              

            # Execution

            # list_of_strings = [str(s) for s in Commande]

            # joined_string = " ".join(list_of_strings)
            # print(joined_string)
            # os.system(joined_string)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1381, 662)
        MainWindow.setMaximumSize(QtCore.QSize(1381, 707))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 0, 481, 651))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(80, 300, 71, 18))
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(90, 20, 58, 18))
        self.label.setObjectName("label")
        
        self.listWidget_3 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 330, 181, 231))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setDragEnabled(True)
        
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 50, 181, 231))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setAcceptDrops(True)
        
        self.listWidget_4 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_4.setGeometry(QtCore.QRect(260, 50, 181, 231))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.setDragEnabled(True)
        self.listWidget_4.setAcceptDrops(True)

        self.listWidget_5 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_5.setGeometry(QtCore.QRect(260, 330, 181, 231))
        self.listWidget_5.setObjectName("listWidget_5")
        self.listWidget_5.setDragEnabled(True)
        self.listWidget_5.setAcceptDrops(True)

        
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(320, 300, 61, 18))
        self.label_3.setObjectName("label_3")
        
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(320, 20, 51, 18))
        self.label_7.setObjectName("label_7")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 580, 88, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fill)

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(490, 0, 881, 651))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(350, 290, 441, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 18))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 81, 18))
        self.label_5.setObjectName("label_5")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 20, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 81, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 160, 301, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(190, 100, 151, 18))
        self.label_6.setObjectName("label_6")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 100, 41, 21))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 200, 88, 34))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.modify)

        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 291, 541))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.itemClicked.connect(self.updateEdits)
        self.listWidget.itemDoubleClicked.connect(self.takeOut) 

        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(330, 30, 511, 191))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 321, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 91, 18))
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 121, 18))
        self.label_18.setObjectName("label_18")

        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setGeometry(QtCore.QRect(130, 50, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 100, 71, 18))
        self.label_19.setObjectName("label_19")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 90, 361, 32))
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 90, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.filepicker)

        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(400, 140, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createBloc)

        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(10, 140, 101, 18))
        self.label_21.setObjectName("label_21")

        self.spinBox = QtWidgets.QSpinBox(self.frame_5)
        self.spinBox.setGeometry(QtCore.QRect(120, 130, 52, 32))
        self.spinBox.setObjectName("spinBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 140, 121, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openLfW)

        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(510, 260, 131, 18))
        self.label_20.setObjectName("label_20")

        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(130, 10, 71, 18))
        self.label_22.setObjectName("label_22")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(400, 580, 251, 32))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 580, 88, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.save)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 580, 141, 34))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.getItems)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 580, 141, 34))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.execute)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Secondary"))
        self.label.setText(_translate("MainWindow", "Primary"))
        self.label_3.setText(_translate("MainWindow", "Features"))
        self.label_7.setText(_translate("MainWindow", "Scripts"))
        self.pushButton_3.setText(_translate("MainWindow", "Rafraîchir"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Ctrl+r"))
        self.label_4.setText(_translate("MainWindow", "Categorie :"))
        self.label_5.setText(_translate("MainWindow", "Commande : "))
        self.label_6.setText(_translate("MainWindow", "Position dans le pattern :"))
        self.pushButton_8.setText(_translate("MainWindow", "Modifier"))
        self.label_17.setText(_translate("MainWindow", "Nom du bloc :"))
        self.label_18.setText(_translate("MainWindow", "Catégorie de bloc :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Primaire"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Secondaire"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Script"))
        self.label_19.setText(_translate("MainWindow", "Commande"))
        self.pushButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Create Block"))
        self.label_21.setText(_translate("MainWindow", "Pattern position"))
        self.pushButton_2.setText(_translate("MainWindow", "Base de données"))
        self.label_20.setText(_translate("MainWindow", "Information du bloc"))
        self.label_22.setText(_translate("MainWindow", "Workspace"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Nom de la fonctionnalité à sauvegarder :"))
        self.pushButton_5.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_6.setText(_translate("MainWindow", "Execute"))
        self.pushButton_7.setText(_translate("MainWindow", "Execute Feature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = creatorWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
