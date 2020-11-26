#!/usr/bin/env python3
#-*-coding:utf-8-*-
from scapy.all import *
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
class Forge:

    def myIp(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a=s.getsockname()[0]
        
        return a

        s.close()
        

    def __init__(self,*args):
        self.argumentLenght = len(args)
        
        if self.argumentLenght == 2 : 
            self.message = args[1]
            self.destination = args[0]

        elif self.argumentLenght == 1 :
            
            self.message = "Packet sended from {}".format(self.myIp("ip"))
            self.destination = args[0]
            print("Votre paquet sera envoyé avec un message par défaut ")

        else : 
            raise Exception("Aucun paramètre n'a été reçu")
    


class packetWindow(object):
    
    def wakeOnLan(self):
        magic=self.lineEdit_4.text()
        thing=str(magic*int(self.spinBox.text()))
        self.packet = Ether(dst="ff:ff:ff:ff:ff:ff ")/UDP(dport=7)/thing
        send(self.packet)
   
    def customPacket(self):
        if self.comboBox.currentText() == "IP" :
            
            if self.comboBox_2.currentText() == "ICMP" :
                self.packet = IP(dst=self.lineEdit_4.text())/ICMP()/self.lineEdit_3.text()
                self.packet.show()
                send(self.packet)
                
        elif self.comboBox_2.currentText() == "Ethernet" :
          
            if self.comboBox_2.currentText() == "UDP" :
                self.packet = Ether(dst=str(self.lineEdit_4.text()))/UDP(dport=self.lineEdit_5.text())/self.lineEdit_3.text()*int(self.spinBox.text())
                self.packet.show()
                send(self.packet)

            elif self.comboBox_2.currentText() == "TCP": 
                self.packet = Ether(dst=self.lineEdit_4.text())/TCP(dport=self.lineEdit_5.text())/self.lineEdit_3.text()*int(self.spinBox.text())
                self.packet.show()
                send(self.packet)
            
        else : 
            pass

    def getMacAddress(self):
        arping(self.lineEdit_4.text())


        
    def update(self):
        self.label_4.adjustSize()

    def preview(self):
        self.label_4.setText(self.comboBox.currentText()+"/"+self.lineEdit_4.text()+"/"+self.comboBox_2.currentText()+"/"+self.lineEdit_3.text()+"/"+self.lineEdit_5.text())
        self.update()

    def wireshark(self):
        os.system("sudo wireshark")
    
    def cells(self):
        print(ls(self.comboBox.currentText()))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(390, 60, 391, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 58, 18))
        self.label_4.setObjectName("label_4")
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 30, 161, 18))
        self.label.setObjectName("label")
      
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 170, 211, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
       
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 70, 211, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
   
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 180, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.preview)
     
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 220, 211, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
      
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 180, 191, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cells)
     
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 180, 88, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.customPacket)
      
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 180, 71, 18))
        self.label_2.setObjectName("label_2")
      
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(270, 170, 41, 32))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
    
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 211, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
  
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 120, 211, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
     
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 30))
        self.menubar.setObjectName("menubar")
      
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
     
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
     
        self.actionWakeOnLan = QtWidgets.QAction(MainWindow)
        self.actionWakeOnLan.setObjectName("actionWakeOnLan")
        self.actionWakeOnLan.triggered.connect(self.wakeOnLan)
   
        self.actionWireShark = QtWidgets.QAction(MainWindow)
        self.actionWireShark.setObjectName("actionWireShark")
        self.actionWireShark.triggered.connect(self.wireshark)
        self.actionARP = QtWidgets.QAction(MainWindow)
        self.actionARP.setObjectName("actionARP")
        self.actionARP.triggered.connect(self.getMacAddress)

        self.menuMore.addAction(self.actionWireShark)
        self.menuMore.addAction(self.actionARP)
        self.menuMore.addAction(self.actionWakeOnLan)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Packet Forger"))
        self.label_4.setText(_translate("MainWindow", "Paquet"))
        self.label.setText(_translate("MainWindow", "Prévisualisation"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Contenu"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Destination"))
        self.pushButton.setText(_translate("MainWindow", "Preview"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Numéro de port"))
        self.pushButton_2.setText(_translate("MainWindow", "Voir les champs du protocol"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.comboBox.setItemText(0, _translate("MainWindow", "IP"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ethernet"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ICMP"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "UDP"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "TCP"))
        self.menuMore.setTitle(_translate("MainWindow", "More"))
        self.actionWakeOnLan.setText(_translate("MainWindow", "WakeOnLan"))
        self.actionWireShark.setText(_translate("MainWindow", "WireShark"))
        self.actionARP.setText(_translate("MainWindow", "ARP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = packetWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#Forge("192.168.1.0/24").getMacAddress()
#Forge("d0 17 c2 d4 8b fb").wakeOnLan()