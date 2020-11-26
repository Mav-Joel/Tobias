#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import mysql.connector
import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database


class Quickset1Window(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")

    def createBloc(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")
        a = self.lineEdit.text()
        a = a.split()

        Ins="INSERT INTO creator (id , name , type , command , category) VALUES (NULL , '{}' , 'Bloc' , '{}' , 'Primaire')".format(a[0],a[1])

        Command.execute(Ins)
        mydb.commit()
        msg = QMessageBox()
        msg.setWindowTitle("Tobias")
        msg.setText("Bloc créer avec succès")
        x = msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 401, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 88, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createBloc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 30))
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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Contenu du Bloc Primaire"))
        self.pushButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Quickset1Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
