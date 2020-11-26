#!/usr/bin/env python3
#-*-coding:utf-8-*-

import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database


class blockWindow(object):
    def __init__(self):
        self.MagicWord=Tools().getModuleData("local dbpassword","Tobias")

    def createBloc(self):

        Database("creator","id","name","type","command","category","NULL",f"{self.lineEdit.text()}","Bloc",f"{self.lineEdit_2.text()}",f"{self.comboBox.currentText()}").insertInDatabase()
        Tools().Notification("Block Successfully Created")
        self.MainWindow.close()

    def filepicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.lineEdit_2.setText(fileName[0])


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 327)
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 321, 32))
        self.lineEdit.setObjectName("lineEdit")
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 18))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 141, 18))
        self.label_2.setObjectName("label_2")
      
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 150, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
       
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 240, 321, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
       
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 291, 18))
        self.label_3.setObjectName("label_3")
      
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 240, 161, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filepicker)
      
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 190, 161, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.createBloc)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(490, 30, 271, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
      
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 111, 18))
        self.label_5.setObjectName("label_5")
      
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 121, 18))
        self.label_6.setObjectName("label_6")
     
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 151, 18))
        self.label_7.setObjectName("label_7")
      
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 0, 111, 18))
        self.label_4.setObjectName("label_4")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 30))
        self.menubar.setObjectName("menubar")
       
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Bloc\'s Creation Page"))
        self.label.setText(_translate("MainWindow", "Nom du bloc"))
        self.label_2.setText(_translate("MainWindow", "Catégorie de bloc"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Primaire"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Secondaire"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Script"))
        self.label_3.setText(_translate("MainWindow", "Commande à exécuter OU Path d\'un fichier"))
        self.pushButton.setText(_translate("MainWindow", "Sélectionner  un fichier"))
        self.pushButton_2.setText(_translate("MainWindow", "Créer le bloc"))
        self.label_5.setText(_translate("MainWindow", "Nom du bloc :"))
        self.label_6.setText(_translate("MainWindow", "Catégorie du  bloc : "))
        self.label_7.setText(_translate("MainWindow", "Commande à exécuter :"))
        self.label_4.setText(_translate("MainWindow", "Récapitulatif"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = blockWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())