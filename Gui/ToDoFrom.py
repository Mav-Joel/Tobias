#!/usr/bin/env python3
#-*-coding:utf-8-*-
import paramiko
import os
import sys
import time
import subprocess
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.TBook import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

#Multi Task 

Utilisateur=os.environ["USER"]

class toDoFromWindow(object):
    
    def filepicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.lineEdit_5.setText(fileName[0])

    def Multi_Task_PCs(self):
        
        print("Multitasking ongoing")
        #Envoi du fichier de contrôle / Envoi du programme dans le fichier de contrôle
        os.system("scp -r /Users/{}/Archetype/Tobito/Multi_Task_Pcs {}:~/".format(Utilisateur,self.lineEdit_4.text())) 

        os.system("scp {} {}:{} ".format(self.lineEdit_5.text(),self.lineEdit.text()+"@"+self.lineEdit_3.text(),self.lineEdit_4.text()))

        # Executer le programme
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(Ip,port=22 ,username=self.lineEdit.text(),password=self.lineEdit_2.text())
        stdin,stdout,stderr=ssh.exec_command("chmod u+x {}/* | {}/* >> {}/Rapport/Result".format(self.lineEdit_4.text(),self.lineEdit_4.text,self.lineEdit_4.text()))
        output= stdout.readlines()
        print( "\n".join(output))

        os.system("scp {}:{}/Rapport/Result {} ".format(self.lineEdit.text()+"@"+self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_6.text()))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 171, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 171, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 130, 171, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 180, 351, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 230, 251, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 280, 301, 32))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 230, 51, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filepicker)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 40, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Multi_Task_PCs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 30))
        self.menubar.setObjectName("menubar")
        self.menuPr_r_glages = QtWidgets.QMenu(self.menubar)
        self.menuPr_r_glages.setObjectName("menuPr_r_glages")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionP = QtWidgets.QAction(MainWindow)
        self.actionP.setObjectName("actionP")
        self.actionP2 = QtWidgets.QAction(MainWindow)
        self.actionP2.setObjectName("actionP2")
        self.actionP3 = QtWidgets.QAction(MainWindow)
        self.actionP3.setObjectName("actionP3")
        self.actionP4 = QtWidgets.QAction(MainWindow)
        self.actionP4.setObjectName("actionP4")
        self.actionP5 = QtWidgets.QAction(MainWindow)
        self.actionP5.setObjectName("actionP5")
        self.menuPr_r_glages.addAction(self.actionP)
        self.menuPr_r_glages.addAction(self.actionP2)
        self.menuPr_r_glages.addAction(self.actionP3)
        self.menuPr_r_glages.addAction(self.actionP4)
        self.menuPr_r_glages.addAction(self.actionP5)
        self.menubar.addAction(self.menuPr_r_glages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Multi PC/Tasks Page"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nom d\'utilisateur"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Adresse ip"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Chemin Repertoire de travail sur l\'ordinateur cible "))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Chemin Programme à envoyer"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Chemin de Retour sur la machine actuelle"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
        self.menuPr_r_glages.setTitle(_translate("MainWindow", "Préréglages"))
        self.actionP.setText(_translate("MainWindow", "P1"))
        self.actionP2.setText(_translate("MainWindow", "P2"))
        self.actionP3.setText(_translate("MainWindow", "P3"))
        self.actionP4.setText(_translate("MainWindow", "P4"))
        self.actionP5.setText(_translate("MainWindow", "P5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = toDoFromWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
