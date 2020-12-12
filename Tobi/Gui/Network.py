#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(1,"/home/joel/Archetype/Tobi")
from Library.DBook import Database
Utilisateur=os.environ["USER"]

class NetworkconfWindow(object):
    def __init__(self):
        self.nCsv = Database().getPaths('path','NetworkCSV')

    def open(self):
        with open(f"{self.nCsv}","r") as variable :
            self.plainTextEdit.appendPlainText(variable.read())
            variable.close()
            
    def save(self):
        text = self.plainTextEdit.toPlainText()
        with open(f"{self.nCsv}","w") as variable : 
            variable.write(text)
            variable.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 0, 411, 391))
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 446, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuSauvegarder = QtWidgets.QMenu(self.menuBar)
        self.menuSauvegarder.setObjectName("menuSauvegarder")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionSauvegarder = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionNouvelles_Notes = QtWidgets.QAction(MainWindow)
        self.actionNouvelles_Notes.setObjectName("actionNouvelles_Notes")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.triggered.connect(self.save)
        self.actionSave.setObjectName("actionSave")
        self.menuSauvegarder.addAction(self.actionSave)
        self.menuBar.addAction(self.menuSauvegarder.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        with open(f"{self.nCsv}","r") as variable :
            if variable != "" : 
                self.open()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Rules"))
        self.menuSauvegarder.setTitle(_translate("MainWindow", "Sauvegarder"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.actionNouvelles_Notes.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = NetworkconfWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
