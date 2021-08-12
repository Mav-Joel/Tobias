#!/usr/bin/env python3
#-*-coding:utf-8-*-
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import mysql
import os
import functools
import time
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")

#---------------CUSTOM MODULES--------------------------
from Library.TBook import Tools #ADDS ALL THE METHODS STORED IN CLASS `Tools`
from Library.RawNetwork import internetProtocol #ADDS ALL THE METHODS STORED IN CLASS `internetProtol`
#---------------END CUSTOM MODULES--------------------------



class addPcWindow(object):
    """This window allows the user to give a name to the unknown ip addresses on his network"""

    def __init__(self):
        #---------------DECL--------------------------
        self.Content = []
        self.MagicWord = Tools().getModuleData("localDbPassword","Tobias")
        #---------------END DECL--------------------------


        #---------------MYSQL DATABASE--------------------------
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )
        #---------------END MYSQL DATABASE--------------------------


        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(address) FROM unknownIps")

        for x in Command:
            for lettre in x :
                self.Content.append(lettre) #Adds all the addresses into the Content List
        
    def refresh(self):
        #---------------TOBIAS PROMPT MESSAGE--------------------------
        Tools().MsgSystem("Refreshing","...")
        #---------------END TOBIAS PROMPT MESSAGE--------------------------

        #---------------DECL--------------------------
        self.Content = []
        Command = self.mydb.cursor() 
        #---------------END DECL--------------------------

        #---------------METHOD CALL--------------------------
        internetProtocol().Main()
        #---------------END METHOD CALL--------------------------

        Command.execute("USE tobiasdb") 
        Command.execute("SELECT DISTINCT(address) FROM unknownIps")

        for x in Command:
            for lettre in x :
                self.Content.append(lettre) #Manually adds all the addresses into the Content List
        
        for i in range(0,len(self.Content)):
            self.listWidget.insertItem(i,self.Content[i]) #Refreshes the widget 

        #---------------TOBIAS PROMPT MESSAGE--------------------------
        Tools().MsgSystem("Refreshed","Done")
        #---------------END TOBIAS PROMPT MESSAGE--------------------------

 
    def save(self):
        
        Command = self.mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"INSERT INTO knownIps(id , hostname , address) VALUES (NULL , '{self.lineEdit.text()}' , '{self.listWidget.currentItem().text()}')")
        Command.execute(f"DELETE FROM unknownIps WHERE address='{self.listWidget.currentItem().text()}'")
        self.mydb.commit()


    def changeLabel(self):
        self.label.setText(self.listWidget.currentItem().text())
        self.label.adjustSize()
        

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")  
        MainWindow.resize(800, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 371, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.changeLabel)

        for i in range(0,len(self.Content)):
            self.listWidget.insertItem(i,self.Content[i])
    
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 130, 291, 32))
        self.lineEdit.setObjectName("lineEdit")
      
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 171, 41))
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
       
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 240, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 240, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.refresh)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listWidget.setFont(font)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register New Pcs"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Name"))
        self.pushButton.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = addPcWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
