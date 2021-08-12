#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
Utilisateur=os.environ["USER"]
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.DBook import Database

class notesWindow(object):
    def __init__(self):
        self.notesPath = Database().getPaths('noteFile','Notes')

    def save(self):
        text = self.plainTextEdit.toPlainText()
        with open(f"{self.notesPath}","w") as variable : 
            variable.write(text)
            variable.close()

    def open(self):
        with open(f"{self.notesPath}","r") as variable :
            self.plainTextEdit.appendPlainText(variable.read())
            variable.close()


    def clear(self):
        self.plainTextEdit.setPlainText("")
        

    def setupUi(self, notesWindow):
        notesWindow.setObjectName("notesWindow")    
        notesWindow.resize(431, 543)
        self.centralwidget = QtWidgets.QWidget(notesWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 0, 411, 491))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        notesWindow.setCentralWidget(self.centralwidget)
       
        self.statusbar = QtWidgets.QStatusBar(notesWindow)
        self.statusbar.setObjectName("statusbar")
       
        notesWindow.setStatusBar(self.statusbar)
        
        self.menuBar = QtWidgets.QMenuBar(notesWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 431, 30))
        self.menuBar.setObjectName("menuBar")
       
        self.menuParam_tres = QtWidgets.QMenu(self.menuBar)
        self.menuParam_tres.setObjectName("menuParam_tres")
       
        self.menuSauvegarder = QtWidgets.QMenu(self.menuBar)
        self.menuSauvegarder.setObjectName("menuSauvegarder")
       
        notesWindow.setMenuBar(self.menuBar)
       
        self.actionOuvrir = QtWidgets.QAction(notesWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
       
        self.actionSauvegarder = QtWidgets.QAction(notesWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
       
        self.actionNouvelles_Notes = QtWidgets.QAction(notesWindow)
        self.actionNouvelles_Notes.setObjectName("actionNouvelles_Notes")
        self.actionNouvelles_Notes.triggered.connect(self.clear)

        self.actionOpen = QtWidgets.QAction(notesWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open)
        
        self.actionSave = QtWidgets.QAction(notesWindow) 
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)
        
        self.menuParam_tres.addAction(self.actionNouvelles_Notes)
        self.menuParam_tres.addAction(self.actionOpen)
        
        self.menuSauvegarder.addAction(self.actionSave)
       
        self.menuBar.addAction(self.menuParam_tres.menuAction())
        self.menuBar.addAction(self.menuSauvegarder.menuAction())

        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)

        self.retranslateUi(notesWindow)
        QtCore.QMetaObject.connectSlotsByName(notesWindow)

    def retranslateUi(self, notesWindow):
        _translate = QtCore.QCoreApplication.translate
        notesWindow.setWindowTitle(_translate("notesWindow", "Tobias\'s Bloc Note"))
        self.menuParam_tres.setTitle(_translate("notesWindow", "Ouvrir"))
        self.menuSauvegarder.setTitle(_translate("notesWindow", "Sauvegarder"))
        self.actionOuvrir.setText(_translate("notesWindow", "Ouvrir"))
        self.actionSauvegarder.setText(_translate("notesWindow", "Sauvegarder"))
       
        self.actionNouvelles_Notes.setText(_translate("notesWindow", "New"))
        self.actionNouvelles_Notes.setShortcut(_translate("MainWindow", "Ctrl+c"))
        
        self.actionOpen.setText(_translate("notesWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+o"))
        
        self.actionSave.setText(_translate("notesWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+s"))


