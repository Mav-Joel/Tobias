#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys, inspect
sys.path.insert(1,"/home/joel/Archetype/Tobi")
sys.path.insert(1,"/home/joel/Archetype/Tobi/Security")
sys.path.insert(1,"/home/joel/Archetype/Tobi/Library")
sys.path.insert(1,"/home/joel/Archetype/Tobi/creatorFiles")
sys.path.insert(1,"/home/joel/Archetype/Tobi/System")
sys.path.insert(1,"/home/joel/Archetype/Tobi/Violet")
sys.path.insert(1,"/home/joel/Archetype/Tobi/Web")
from Tobias import Tobias,ByPass,Ui_MainWindow
from Riot import Security
from RawNetwork import internetProtocol,Ally_Computers
from Rapport import rapportWindow
from ToDoFrom import toDoFromWindow 
from UpdateHosts import updateWindow
from PageBackbone import bbWindow
from Page_Stockage import pageStockageMainWindow
from Page_Serveur import ServerWindow
from Page_Reseau import pageReseauUI 
from Page_Configuration import confWIndow
from packets import Forge,packetWindow
from Notes import notesWindow
from Network import NetworkconfWindow 
from Lookfor import LookforWindow 
from Handler import handlerWindow
from Creator import creatorWindow 
from Borrow import Scrap,SecureScraping,CompteRendu,findMacProvider
from Backbone import Backbone
from addPc import addPcWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class RawWindow(object):

    def __init__(self):
        self.toDo = ["className","methodName"]
        self.thing = 0

    def print_names(self):
        Names = [
            "Tobias", 
            "Riot",
            "RawNetwork", 
            "Rapport",
            "ToDoFrom",
            "UpdateHosts", 
            "PageBackbone", 
            "Page_Stockage", 
            "Page_Serveur", 
            "Page_Reseau", 
            "Page_Configuration", 
            "packets", 
            "Notes", 
            "Network", 
            "Lookfor", 
            "Handler", 
            "Creator", 
            "Borrow", 
            "Backbone", 
            "addPc", 
            "PyQt5" 
        ]
        return Names

    def print_methods(self):
        Names = [
        "Tobias",
        "ByPass",
        "Ui_MainWindow",
        "Security",
        "internetProtocol",
        "Ally_Computers",
        "rapportWindow",
        "toDoFromWindow", 
        "updateWindow",
        "bbWindow",
        "pageStockageMainWindow",
        "ServerWindow",
        "pageReseauUI",
        "confWIndow",
        "Forge",
        "packetWindow",
        "notesWindow",
        "NetworkconfWindow", 
        "LookforWindow",
        "handlerWindow",
        "creatorWindow",
        "Scrap",
        "SecureScraping",
        "CompteRendu",
        "findMacProvider",
        "Backbone",
        "addPcWindow",
        ]
        return sorted(Names)
  
    def execute(self):
        
        self.toDo[1]=(self.listWidget.currentItem().text())
        for i in range(0,len(self.print_methods())):
            if self.toDo[0] == self.print_methods()[i]:
                if self.lineEdit.text() == "" : 
                    toExec = f"{self.toDo[0]}().{self.toDo[1]}()"
                    exec(toExec)
                else : 
                    toExec = f"{self.toDo[0]}().{self.toDo[1]}('{self.lineEdit.text()}')"
                    exec(toExec)
            else : 
                pass
        
    def print_classes(self):
        if self.thing == 0:

            self.toDo[0]=(self.listWidget.currentItem().text())
            method_list = [method for method in dir(eval(self.listWidget.currentItem().text())) if method.startswith('__') is False]
            method_list = sorted(method_list)

            self.listWidget.clear() #Refreshes the widget 
            for i in range(0,len(method_list)):
                self.listWidget.insertItem(i,method_list[i]) #Refreshes the widget 
            self.thing = 1
            return method_list
        else : 
            pass
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 11, 461, 251))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 270, 371, 32))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget.itemClicked.connect(self.print_classes)
        self.listWidget.itemDoubleClicked.connect(self.execute)


        for i in range(0,len(self.print_methods())):
            self.listWidget.insertItem(i,self.print_methods()[i]) #Refreshes the widget 

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 270, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.execute)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 30))
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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Arguments"))
        self.pushButton.setText(_translate("MainWindow", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RawWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
