#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
Utilisateur=os.environ["USER"]
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.DBook import Database
#Récupérer informations utilisateur

class confWIndow(object):

    def __init__(self):
        self.right = " True"
        self.wrong = " False"
        self.confs = Database().getPaths('path','ConfigurationJson')

    def allIn(self):
        newConfig = {
        "Configurations": [
            {
            "Backbone": {
                "ipScan": "True",
                "networkSpace": "True",
                "allow/Deny access": "True"
            },
            "Riot": {
                "authorized_keys": "True",
                "crontabCheck": "True",
                "connexions": "True",
                "processus": "True"
            },
            "General": {
                "AllyComputer": "True",
                "Internet Protocol": "True",
                "Langue": "FR"
            },
            "user": {
                "name": "Toula",
                "prenom": "Joel",
                "phone number": "0694232624",
                "adresse mail": "joel.toula@gmail.com"
            },
            "Tobias": {
                "name": "MainTobias",
                "localDbPassword": "GrpAmPMaverick&",
                "MainServer": self.lineEdit.text()
            }
            }
        ]
        }
        with open(f"{self.confs}","w") as config :
            json.dump(newConfig,config,indent=2)
    


    def allOut(self):
        newConfig = {
        "Configurations": [
            {
            "Backbone": {
                "ipScan": "False",
                "networkSpace": "False",
                "allow/Deny access": "False"
            },
            "Riot": {
                "authorized_keys": "False",
                "crontabCheck": "False",
                "connexions": "False",
                "processus": "False"
            },
            "General": {
                "AllyComputer": "False",
                "Internet Protocol": "False",
                "Langue": "FR"
            },
            "user": {
                "name": "Toula",
                "prenom": "Joel",
                "phone number": "0694232624",
                "adresse mail": "joel.toula@gmail.com"
            },
            "Tobias": {
                "name": "MainTobias",
                "localDbPassword": "GrpAmPMaverick&",
                "MainServer": self.lineEdit.text()
            }
            }
        ]
        }
        with open(f"{self.confs}","w") as config :
            json.dump(newConfig,config,indent=2)
        

    def getModuleData(self,searchingFor,fieldName='user'):
        with open(f"{self.confs}","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def getAddress(self):
        vals = []
        with open(f"{self.confs}","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for values in parameters['Tobias'].values() :
                vals.append(values) 
        
        return vals[1]     
      

    def getValues(self):

        newConfig = {
    
            "Configurations": [
                {
                    "Backbone": {
                    
                        "ipScan" : self.comboBox.currentText().strip(),
                        "networkSpace" : self.comboBox_2.currentText().strip() , 
                        "allow/Deny access" : self.comboBox_3.currentText().strip()
                
                    },

                    "Riot": {

                        "authorized_keys" : self.comboBox_4.currentText().strip(),
                        "crontabCheck" : self.comboBox_5.currentText().strip(), 
                        "connexions" : self.comboBox_6.currentText().strip(), 
                        "processus" : self.comboBox_7.currentText().strip() 

                    },

                    "General" : {

                        "AllyComputer" : self.comboBox_8.currentText().strip() ,
                        "Internet Protocol" : self.comboBox_9.currentText().strip() ,
                        "Langue" : self.comboBox_10.currentText().strip()

                    },

                    "user": {
                        "name": "Toula",
                        "prenom": "Joel",
                        "phone number" : "13/01/2002",
                        "adresse mail" : "joel.toula@gmail.com"
                    },
                    
                    "Tobias" : {
                        "name": "MainTobias",
                        "localDbPassword": "GrpAmPMaverick&",
                        "MainServer": self.lineEdit.text(),
                        "admin" : self.comboBox_11.currentText().strip() 
                    } 
                }
            ]
        }
        with open(f"{self.confs}","w") as config :
            json.dump(newConfig,config,indent=2)
        

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 581, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 261, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 451, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 391, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 371, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 251, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 321, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 210, 241, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 240, 341, 18))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 270, 341, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(50, 300, 51, 18))
        self.label_10.setObjectName("label_10")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(50, 330, 81, 18))
        self.label_21.setObjectName("label_21")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(480, 380, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getValues)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(260, 30, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 60, 81, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(440, 90, 81, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(420, 120, 81, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(300, 150, 81, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(370, 180, 81, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(290, 210, 81, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(400, 240, 81, 21))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame)
        self.comboBox_9.setGeometry(QtCore.QRect(390, 270, 81, 21))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.frame)
        self.comboBox_10.setGeometry(QtCore.QRect(100, 300, 81, 21))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(self.frame)
        self.comboBox_11.setGeometry(QtCore.QRect(140, 330, 81, 21))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(50, 380, 141, 18))
        self.label_22.setObjectName("label_22")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(210, 370, 113, 32))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 30))
        self.menubar.setObjectName("menubar")
        self.menuModes = QtWidgets.QMenu(self.menubar)
        self.menuModes.setObjectName("menuModes")
        self.menuPr_r_glages = QtWidgets.QMenu(self.menubar)
        self.menuPr_r_glages.setObjectName("menuPr_r_glages")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEconomie_d_nergie = QtWidgets.QAction(MainWindow)
        self.actionEconomie_d_nergie.setObjectName("actionEconomie_d_nergie")
        self.actionEconomie_d_nergie.triggered.connect(self.allOut)
        self.actionIdgaf = QtWidgets.QAction(MainWindow)
        self.actionIdgaf.setObjectName("actionIdgaf")
        self.actionIdgaf.triggered.connect(self.allIn)
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
        self.menuModes.addAction(self.actionEconomie_d_nergie)
        self.menuModes.addAction(self.actionIdgaf)
        self.menuPr_r_glages.addAction(self.actionP1)
        self.menuPr_r_glages.addAction(self.actionP2)
        self.menuPr_r_glages.addAction(self.actionP3)
        self.menuPr_r_glages.addAction(self.actionP4)
        self.menuPr_r_glages.addAction(self.actionP5)
        self.menubar.addAction(self.menuModes.menuAction())
        self.menubar.addAction(self.menuPr_r_glages.menuAction())
        font = QtGui.QFont()
        font.setFamily("Inconsolata SemiBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_4.setFont(font)
        self.label_10.setFont(font)
        self.label_2.setFont(font)
        self.label_21.setFont(font)
        self.label_22.setFont(font)
        self.label_3.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_8.setFont(font)
        self.label_7.setFont(font)
        self.label_9.setFont(font)
        self.label_10.setFont(font)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Configuration Page"))
        self.label.setText(_translate("MainWindow", "Scan IP du réseau"))
        self.label_2.setText(_translate("MainWindow", "Détection du changement d\'adresse de l\'utilisateur "))
        self.label_3.setText(_translate("MainWindow", "Système d\'authentification SSH par liste blanche "))
        self.label_4.setText(_translate("MainWindow", "Vérification des clées publiques enregistrées  "))
        self.label_5.setText(_translate("MainWindow", "Vérification de la Crontab "))
        self.label_6.setText(_translate("MainWindow", "Vérification des liaisons SSH établies "))
        self.label_7.setText(_translate("MainWindow", "Gestion des processus "))
        self.label_8.setText(_translate("MainWindow", "Informations sur les ordinateurs connus "))
        self.label_9.setText(_translate("MainWindow", "Vérification des activitées sur le réseau "))
        self.label_10.setText(_translate("MainWindow", "Langue "))
        self.label_21.setText(_translate("MainWindow", "Mode Admin"))
        self.pushButton.setText(_translate("MainWindow", "Save"))

        if self.getModuleData("ipScan","Backbone") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("networkSpace","Backbone") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"


        self.comboBox_2.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("allow/Deny access","Backbone") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox_3.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("authorized_keys","Riot") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox_4.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("crontabCheck","Riot") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox_5.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("connexions","Riot") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"
            
        self.comboBox_6.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("processus","Riot") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox_7.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("AllyComputer","General") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"


        self.comboBox_8.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
        
        if self.getModuleData("Internet Protocol","General") == "True" :
            self.right = "True"
            self.wrong = "False"
        else : 
            self.right = "False"
            self.wrong = "True"

        self.comboBox_9.setItemText(0, _translate("MainWindow", "{}").format(self.right))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "{}").format(self.wrong))
       
        if self.getModuleData("Langue","General") == "Fr" :
            self.rightL = "Fr"
            self.wrongL = "En"
        else : 
            self.rightL = "En"
            self.wrongL = "Fr"

        self.comboBox_10.setItemText(0, _translate("MainWindow", "  {}".format(self.rightL)))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "  {}".format(self.wrongL)))
        
        self.comboBox_11.setItemText(0, _translate("MainWindow", "  True"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "  False"))
       
        
        self.label_22.setText(_translate("MainWindow", "Adresse du Webserver"))
        # self.lineEdit.setText(_translate("MainWindow", "{}".format(self.getAddress())))
        self.menuModes.setTitle(_translate("MainWindow", "Modes"))
        self.menuPr_r_glages.setTitle(_translate("MainWindow", "Préréglages"))
        self.actionEconomie_d_nergie.setText(_translate("MainWindow", "Economie d\'énergie"))
        self.actionIdgaf.setText(_translate("MainWindow", "Rock\'n Roll"))
        self.actionP1.setText(_translate("MainWindow", "P1"))
        self.actionP2.setText(_translate("MainWindow", "P2"))
        self.actionP3.setText(_translate("MainWindow", "P3"))
        self.actionP4.setText(_translate("MainWindow", "P4"))
        self.actionP5.setText(_translate("MainWindow", "P5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = confWIndow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
