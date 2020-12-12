#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import mysql
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
self.MagicWord=os.environ["MDP"]

class importExportWindow(object):

    def process(self):
        try :
            os.system("scp {} {}".format(self.lineEdit.text(),self.lineEdit_2.text()))
            self.instertPresets()
        except :
            os.system("scp -r {} {}".format(self.lineEdit.text(),self.lineEdit_2.text()))
            self.instertPresets()

    def filepicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.lineEdit.setText(fileName[0])

    def secondFilePicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.lineEdit_2.setText(fileName[0])


    def reverse(self):
        contenuBox1=[]
        contenuBox2=[]
        contenuBox1.append(self.lineEdit.text())
        contenuBox2.append(self.lineEdit_2.text())
        
        self.lineEdit.setText(contenuBox2[0])
        self.lineEdit_2.setText(contenuBox1[0])

    def instertPresets(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        Ins="INSERT INTO presets (id , Programme , Destination , Source ) VALUES (NULL , 'ImportExport' , '{}' , '{}')".format(self.lineEdit_2.text(),self.lineEdit.text())

        Command.execute(Ins)
        mydb.commit()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 231, 32))
        self.lineEdit.setObjectName("lineEdit")
      
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.reverse)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 190, 231, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
       
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 50, 41, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.filepicker)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 190, 41, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.secondFilePicker)
       
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 240, 88, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.process)
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 30))
        self.menubar.setObjectName("menubar")
        
        self.menuPr_r_glages = QtWidgets.QMenu(self.menubar)
        self.menuPr_r_glages.setObjectName("menuPr_r_glages")
        MainWindow.setMenuBar(self.menubar)
       
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
        self.actionP1 = QtWidgets.QAction(MainWindow)
        self.actionP1.setObjectName("actionP1")
      
        self.actionP2 = QtWidgets.QAction(MainWindow)
        self.actionP2.setObjectName("actionP2")
      
        self.actionP3 = QtWidgets.QAction(MainWindow)
        self.actionP3.setObjectName("actionP3")
     
        self.actionP4 = QtWidgets.QAction(MainWindow)
        self.actionP4.setObjectName("actionP4")
     
        self.actionP5 = QtWidgets.QAction(MainWindow)
        self.actionP5.setObjectName("actionP5")
     
        self.menuPr_r_glages.addAction(self.actionP1)
        self.menuPr_r_glages.addAction(self.actionP2)
        self.menuPr_r_glages.addAction(self.actionP3)
        self.menuPr_r_glages.addAction(self.actionP4)
        self.menuPr_r_glages.addAction(self.actionP5)
        self.menubar.addAction(self.menuPr_r_glages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Import Export Page"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Chemin Source"))
        self.pushButton.setText(_translate("MainWindow", "Inverser"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Chemin de Destination"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "Process"))
        self.menuPr_r_glages.setTitle(_translate("MainWindow", "Préréglages"))
        self.actionP1.setText(_translate("MainWindow", "P1"))
        self.actionP2.setText(_translate("MainWindow", "P2"))
        self.actionP3.setText(_translate("MainWindow", "P3"))
        self.actionP4.setText(_translate("MainWindow", "P4"))
        self.actionP5.setText(_translate("MainWindow", "P5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = importExportWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
