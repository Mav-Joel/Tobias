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
from Library.NBook import Network

MagicWord=Tools().getModuleData("localDbPassword","Tobias")


class bbWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("localDbPassword","Tobias")
        
    def getAddresses(self):

        a = Database("backbone","ipAddress","statut","Allowed").getFromDatabase()
        list_of_strings = [str(s) for s in a]   
        joined_string = " ".join(list_of_strings)
        joined_string = joined_string.split()
        return joined_string
        

    def saveAddresses(self): 
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        a = self.lineEdit.text()

        if self.getAddresses() == " " : 
            Command=mydb.cursor()
            Command.execute("USE tobiasdb")
            print(a)
            Ins="INSERT INTO backbone (id,statut,ipAddress) VALUES (NULL,'Allowed','{}')".format(a)
            Command.execute(Ins)
            mydb.commit()

        elif self.getAddresses() != " ": 
            Database("backbone","ipAddress",a,"statut","Allowed").updateValue()
      
        else : 
            Command=mydb.cursor()
            Command.execute("USE tobiasdb")
            Ins="INSERT INTO backbone (id,statut,ipAddress) VALUES (NULL,'Allowed',{})".format(a)
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

        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)

        a = self.getAddresses()
        liste = []
        for i in range(len(a)):
            if a[i] != None : 
                liste.append(a[i])
        
        list_of_strings = [str(s) for s in liste]
        joined_string = " ".join(list_of_strings)
       
        self.lineEdit.setText(joined_string)

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
