#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import mysql.connector
import os
from Bibliotheque.DBook import Database
from Bibliotheque.TBook import Tools

MagicWord=Tools().getModuleData("local dbpassword","Tobias")


transcripts = []
mydb = mysql.connector.connect(
host="localhost",
user="Python",
passwd=MagicWord,
)

Command=mydb.cursor()
Command.execute("USE tobiasdb")
Selec="SELECT Information FROM rapportExecution WHERE Programme='print'"

Command.execute(Selec)
for x in Command :
    for lettre in x : 
        transcripts.append(lettre)

class rapportWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 401, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 30, 361, 371))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragEnabled(True)
        
        for i in range(0,len(transcripts)):
          self.listWidget.insertItem(i,transcripts[i])
      
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rapport d\'éxecutions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = rapportWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
