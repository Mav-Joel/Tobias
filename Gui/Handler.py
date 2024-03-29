#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class handlerWindow(object):

    def __init__(self):
        self.Utilisateur=os.environ["USER"]

    def apache(self):
        os.system(f"sudo /Users/{self.Utilisateur}/Archetype/Tobi/sysCommands/apacheHandler.bash {self.comboBox.currentText()}")

    def tor(self):
        os.system(f"sudo /Users/{self.Utilisateur}/Archetype/Tobi/sysCommands/torHandler.bash {self.comboBox_2.currentText()}")

    def ipTables(self):
        os.system(f"sudo /Users/{self.Utilisateur}/Archetype/Tobi/sysCommands/iptableHandler.bash {self.comboBox_3.currentText()}")

    def sshService(self):
        os.system(f"sudo /Users/{self.Utilisateur}/Archetype/Tobi/sysCommands/sshHandler.bash {self.comboBox_4.currentText()}")
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 30, 111, 32))
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
        self.comboBox_2.setGeometry(QtCore.QRect(90, 110, 101, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 180, 87, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 41, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tor)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 30, 41, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.apache)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 180, 41, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.ipTables)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 260, 41, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.sshService)

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 260, 91, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 310, 321, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.comboBox.setItemText(7, _translate("MainWindow", "Status"))
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
