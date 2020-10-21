#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import mysql
import os
from Bibliotheque.TBook import Tools
from RawNetwork import internetProtocol  

MagicWord = Tools().getModuleData("local dbpassword","Tobias")

Content = []

mydb = mysql.connector.connect(
host="localhost",
user="Python",
passwd=MagicWord,
)

Command = mydb.cursor() 
Command.execute("USE tobiasdb") 
Command.execute("SELECT address FROM unknownIps")

for x in Command:
    for lettre in x :
        Content.append(lettre)

class addPcWindow(object):

    def refresh(self):
        internetProtocol().Main()
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=MagicWord,
        )

        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT address FROM unknownIps")

        for x in Command:
            for lettre in x :
                Content.append(lettre)

    def save(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=MagicWord,
        )
        
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Command.execute(f"INSERT INTO knownIps(id , hostname , address) VALUES (NULL , '{self.lineEdit.text()}' , '{self.listWidget.currentItem().text()}')")
        Command.execute(f"DELETE FROM unknownIps WHERE address='{self.listWidget.currentItem().text()}'")
        mydb.commit()

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

        #Code
        for i in range(0,len(Content)):
            self.listWidget.insertItem(i,Content[i])
    
    
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 130, 291, 32))
        self.lineEdit.setObjectName("lineEdit")
      
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 171, 41))
        
        font = QtGui.QFont()
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
