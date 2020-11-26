#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import os
import mysql.connector
from Bibliotheque.DBook import Database
from Bibliotheque.TBook import Tools
from Bibliotheque.NBook import Network

MagicWord=Tools().getModuleData("local dbpassword","Tobias")


class bbWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")
        
    def getAddresses(self):

        a = Database("backbone","ipAddress","statut","Allowed").getFromDatabase()

        list_of_strings = [str(s) for s in a]   
        joined_string = " ".join(list_of_strings)
        return joined_string
        

    def saveAddresses(self): 
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        if self.getAddresses() == " " : 
            Command=mydb.cursor()
            Command.execute("USE tobiasdb")
            Ins="INSERT INTO backbone (id,statut,ipAddress) VALUES (NULL,'Allowed','{}')".format(self.lineEdit.text())
            Command.execute(Ins)
            mydb.commit()

        elif self.getAddresses() != " ": 
            Database("backbone","ipAddress",self.lineEdit.text(),"statut","Allowed").updateValue()
      
        else : 
            Command=mydb.cursor()
            Command.execute("USE tobiasdb")
            Ins="INSERT INTO backbone (id,statut,ipAddress) VALUES (NULL,'Allowed',{})".format(self.lineEdit.text())
            Command.execute(Ins)
            mydb.commit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 691, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuSauvegarder = QtWidgets.QMenu(self.menubar)
        self.menuSauvegarder.setObjectName("menuSauvegarder")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuSauvegarder.addAction(self.actionSave)
        self.menubar.addAction(self.menuSauvegarder.menuAction())
        self.actionSave.triggered.connect(self.saveAddresses)

        a = self.getAddresses()

        if str(a) is None : 
            print("no known adresses")
        else : 
            self.lineEdit.setText(str(a))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BackBone Allowed Addresses"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Adresses autorisées à se connecter en SSH"))
        self.menuSauvegarder.setTitle(_translate("MainWindow", "Sauvegarder"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = bbWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
