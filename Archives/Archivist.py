#!/usr/bin/env python3
#-*-coding:utf-8-*-

#---------------IMPORT GRAPHICAL INTERFACE--------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
#---------------END IMPORT GRAPHICAL INTERFACE--------------------------

#---------------BUILT-IN IMPORTS--------------------------
import os
import subprocess
import sys
from zipfile import ZipFile 
import zipfile
#---------------END BUILT-IN IMPORTS--------------------------

#---------------ADD TO PATH--------------------------
Utilisateur=os.environ["USER"]
sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi")
sys.path.insert(1,f"/Users/{Utilisateur}/Archetype/Tobi/Library")
#---------------END ADD TO PATH--------------------------

#---------------CUSTOM MODULES--------------------------
from Library.DBook import Database
from Library.TBook import Tools
#---------------END CUSTOM MODULES--------------------------

class Archivisty(object):
    def __init__(self):
    #CONSTRUCTOR

        #---------------DECL--------------------------
        self.i = 0
        self.fileList = []
        #---------------END DECL--------------------------

    def doubleCLickToErase(self):
        #When double clicked on an item get the current row then take out that row to remove the item
        
        self.listWidget.takeItem(self.listWidget.currentRow()) 

    def insert(self):
        
        self.listWidget.insertItem(self.i,self.lineEdit.text())
        self.i =+1
        self.lineEdit.clear()
        self.fileList = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
    
    def filepicker(self):
        fileName = QFileDialog.getOpenFileName()
        self.listWidget.insertItem(1,fileName[0])

    def store(self):
        try : 
            self.fileList = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
         
            path = f"{Database().getPaths('path','Archives')}/{self.lineEdit_2.text()}"
            os.mkdir(path)

            for i in range(0,len(self.fileList)):
                os.system(f"cp {self.fileList[i]} {path}")
            
            for file_name in self.fileList: 
                Database("rapportExecution","id","Programme","Information","NULL","Tobias",f"{file_name}").insertInDatabase()
                with open(f"/Users/{Utilisateur}/Archetype/Tobi/Archives/Rapport.txt","a") as variable:
                    variable.write(file_name+"\n")

                with ZipFile(f'{path}.zip','w',compression=zipfile.ZIP_DEFLATED) as zip: 
                    for i in range(len(self.fileList)):
                        os.system(f"cd {path}")
                        subprocess.getoutput("ls ./")
                        item = self.fileList[i].split("/")
                        zip.write(f"./{item[-1]}") 
            
            Tools().Notification("Archives Created Successfully")
            
        except :
            pass       

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 20, 41, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filepicker)
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 411, 281))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setDragEnabled(True)
        self.listWidget.itemDoubleClicked.connect(self.doubleCLickToErase)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 211, 32))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 20, 51, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.insert)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 350, 91, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.store)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 350, 311, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(340, 30, 151, 22))
        self.radioButton.setObjectName("radioButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 30))
        self.menubar.setObjectName("menubar")
        self.menuUSB = QtWidgets.QMenu(self.menubar)
        self.menuUSB.setObjectName("menuUSB")
        self.menuServer = QtWidgets.QMenu(self.menubar)
        self.menuServer.setObjectName("menuServer")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSend_Archives_to_a_known_server = QtWidgets.QAction(MainWindow)
        self.actionSend_Archives_to_a_known_server.setObjectName("actionSend_Archives_to_a_known_server")
        
        self.actionCopy_Archives_into_a_USB_STICK = QtWidgets.QAction(MainWindow)
        self.actionCopy_Archives_into_a_USB_STICK.setObjectName("actionCopy_Archives_into_a_USB_STICK")
        
        self.menuUSB.addAction(self.actionCopy_Archives_into_a_USB_STICK)
        self.menuServer.addAction(self.actionSend_Archives_to_a_known_server)
        
        self.menubar.addAction(self.menuUSB.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archivisty"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "File or Directory Path"))
        self.pushButton_2.setText(_translate("MainWindow", "ADD"))
        self.pushButton_3.setText(_translate("MainWindow", "Store"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Archive\'s Name (Default : Last Directory\'s Name)"))
        self.radioButton.setText(_translate("MainWindow", "Secure via Password"))
        self.menuUSB.setTitle(_translate("MainWindow", "USB"))
        self.menuServer.setTitle(_translate("MainWindow", "Server"))
        self.actionSend_Archives_to_a_known_server.setText(_translate("MainWindow", "Send Archives to a Server"))
        self.actionCopy_Archives_into_a_USB_STICK.setText(_translate("MainWindow", "Copy Archives into a USB STICK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Archivisty()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


