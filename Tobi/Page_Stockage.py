#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
from getpass import getpass
import hashlib
import os
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import mysql
import mysql.connector
import ast
from Bibliotheque.DBook import Database
from Bibliotheque.TBook import Tools

def MyConverter(mydata):
    def cvt(data):
            try : 
                return ast.litteral_eval(data)
            except Exception:
                return str(data)
    return tuple(map(cvt,mydata))

class pageStockageMainWindow(object):
    def __init__(self):
        self.magicWords=Tools().getModuleData("local dbpassword","Tobias")

    def LoadData(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.magicWords,
        )

        Command = mydb.cursor()
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT * FROM coffreFort")
        data = Command.fetchall()

        for row in data : 
                self.addTable(MyConverter(row))

        Command.close()
    
    
    def addTable(self,columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
                self.tableWidget.setItem(rowPosition, i , QtWidgets.QTableWidgetItem(str(column)))


    def stocker(self): 
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.magicWords,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        a = self.lineEdit.text()
        a = a.split()

        Ins="INSERT INTO coffreFort (id,name,Information) VALUES (NULL , '{}' , '{}')".format(a[0],a[1])      
        Command.execute(Ins)
        mydb.commit()

    def toHash(self): #Hasher et Stocker la valeur dans une base de données
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.magicWords,
        )

        #Entrer un Mot de Passe
        Mot_de_passe_Entré=(self.lineEdit.text())
        #Hasher le mot de passe
        Mot_de_passe_Entré=Mot_de_passe_Entré.encode()
        Mot_de_passe_chiffré = hashlib.sha1(Mot_de_passe_Entré).hexdigest()
        Mot_de_passe_chiffré=str(Mot_de_passe_chiffré)

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        Ins="INSERT INTO coffreFort (id,name,Information) VALUES (NULL,'tobiasStockage','{}')".format(Mot_de_passe_chiffré)
        Command.execute(Ins)
        mydb.commit()
        print(Command.rowcount,"Commandes prise en compte")


    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 340, 111, 41))
        self.pushButton.clicked.connect(self.store)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 691, 211))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 40, 151, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def store(self):
        if self.comboBox.currentText()  == "Is NOT a Password" : 
            self.LoadData()
            self.stocker()
            self.LoadData()

        else : 
            self.LoadData()
            self.toHash()
            self.LoadData()

        

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Vault"))
        self.pushButton.setText(_translate("MainWindow", "Stocker"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Information à Stocker"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Is NOT a Password"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Is a Password"))

def pageStockageWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pageStockageMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
