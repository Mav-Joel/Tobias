#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os
from PyQt5 import QtCore, QtGui, QtWidgets

Utilisateur=os.environ["USER"]

class handlerWindow(object):
    def apache(self):
        os.system("sudo /home/{}/Archetype/Tobi/sysCommands/apacheHandler.bash {}".format(Utilisateur,self.comboBox.currentText()))

    def tor(self):
        os.system("sudo /home/{}/Archetype/Tobi/sysCommands/torHandler.bash {}".format(Utilisateur,self.comboBox_2.currentText()))

    def ipTables(self):
        os.system("sudo /home/{}/Archetype/Tobi/sysCommands/iptableHandler.bash {}".format(Utilisateur,self.comboBox_3.currentText()))

    def sshService(self):
        os.system("sudo /home/{}/Archetype/Tobi/sysCommands/sshHandler.bash {}".format(Utilisateur,self.comboBox_4.currentText()))

    def all(self):

        self.apache()
        self.tor()
        self.ipTables()
        self.sshService()
        
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 111, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 120, 101, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 200, 87, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 120, 41, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tor)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 40, 41, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.apache)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 200, 41, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.ipTables)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 370, 91, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.all)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 280, 41, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.sshService)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 280, 91, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Handler"))
        self.label.setText(_translate("MainWindow", "Apache"))
        self.label_2.setText(_translate("MainWindow", "Tor"))
        self.label_3.setText(_translate("MainWindow", "IPtables"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Run"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Stop"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Disable"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Enable"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Restart"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Reload"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Test"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Status (Manjaro)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Run"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Stop"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Restart"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Fix"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Status"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Trafic"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Save"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Del"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.pushButton_4.setText(_translate("MainWindow", "All OK"))
        self.label_4.setText(_translate("MainWindow", "Service Ssh"))
        self.pushButton_5.setText(_translate("MainWindow", "OK"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Run"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Stop"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Disable"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Enable"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Restart"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Test"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Status "))

  
   
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = handlerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
