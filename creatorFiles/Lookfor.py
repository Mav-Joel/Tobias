#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import os
import mysql.connector
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.DBook import Database
from Library.TBook import Tools
display = []

class LookforWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("localDbPassword","Tobias")

    
    def search(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",                         
        )

        Command = mydb.cursor() 

        if self.lineEdit.text().count("SELECT") == 1:

            Command.execute("USE tobiasdb") 
            Command.execute(self.lineEdit.text())

            for x in Command:
                for lettre in x :
                    display.append(str(lettre))
            
            for i in range(0,len(display)):
                self.listWidget.insertItem(i,display[i])
        
        else : 

        
            Command.execute("USE tobiasdb") 
            Command.execute("SELECT Information FROM coffreFort WHERE name='{}'".format(self.lineEdit.text()))

            for x in Command:
                for lettre in x :
                    display.append(lettre)
            
            for i in range(0,len(display)):
                self.listWidget.insertItem(i,display[i])
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 801, 301))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragEnabled(True)
      
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 491, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 30, 88, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Rechercher"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "SQL Query"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LookforWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
