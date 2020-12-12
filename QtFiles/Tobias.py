# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tobias.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 10, 261, 111))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 551, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuOutils = QtWidgets.QMenu(self.menuBar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuR_seau = QtWidgets.QMenu(self.menuBar)
        self.menuR_seau.setObjectName("menuR_seau")
        self.menuInternet = QtWidgets.QMenu(self.menuBar)
        self.menuInternet.setObjectName("menuInternet")
        self.menuStockage = QtWidgets.QMenu(self.menuBar)
        self.menuStockage.setObjectName("menuStockage")
        self.menuServeur = QtWidgets.QMenu(self.menuBar)
        self.menuServeur.setObjectName("menuServeur")
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuCreator = QtWidgets.QMenu(self.menuBar)
        self.menuCreator.setObjectName("menuCreator")
        MainWindow.setMenuBar(self.menuBar)
        self.actionBloc_Note = QtWidgets.QAction(MainWindow)
        self.actionBloc_Note.setObjectName("actionBloc_Note")
        self.actionImport_Export = QtWidgets.QAction(MainWindow)
        self.actionImport_Export.setObjectName("actionImport_Export")
        self.actionArchiver = QtWidgets.QAction(MainWindow)
        self.actionArchiver.setObjectName("actionArchiver")
        self.actionMail = QtWidgets.QAction(MainWindow)
        self.actionMail.setObjectName("actionMail")
        self.actionRecherche = QtWidgets.QAction(MainWindow)
        self.actionRecherche.setObjectName("actionRecherche")
        self.actionCoffre_Fort = QtWidgets.QAction(MainWindow)
        self.actionCoffre_Fort.setObjectName("actionCoffre_Fort")
        self.actionArchiver_2 = QtWidgets.QAction(MainWindow)
        self.actionArchiver_2.setObjectName("actionArchiver_2")
        self.actionLobby = QtWidgets.QAction(MainWindow)
        self.actionLobby.setObjectName("actionLobby")
        self.actionLobby_2 = QtWidgets.QAction(MainWindow)
        self.actionLobby_2.setObjectName("actionLobby_2")
        self.actionScan_R_seau = QtWidgets.QAction(MainWindow)
        self.actionScan_R_seau.setObjectName("actionScan_R_seau")
        self.actionPaquets = QtWidgets.QAction(MainWindow)
        self.actionPaquets.setObjectName("actionPaquets")
        self.actionHandler = QtWidgets.QAction(MainWindow)
        self.actionHandler.setObjectName("actionHandler")
        self.actionVeraCrypt = QtWidgets.QAction(MainWindow)
        self.actionVeraCrypt.setObjectName("actionVeraCrypt")
        self.actionH_berger = QtWidgets.QAction(MainWindow)
        self.actionH_berger.setObjectName("actionH_berger")
        self.actionModifier_le_fichier_de_configuration = QtWidgets.QAction(MainWindow)
        self.actionModifier_le_fichier_de_configuration.setObjectName("actionModifier_le_fichier_de_configuration")
        self.actionPage_Createur = QtWidgets.QAction(MainWindow)
        self.actionPage_Createur.setObjectName("actionPage_Createur")
        self.actionPage_Internet = QtWidgets.QAction(MainWindow)
        self.actionPage_Internet.setObjectName("actionPage_Internet")
        self.actionVoice_Feedback = QtWidgets.QAction(MainWindow)
        self.actionVoice_Feedback.setObjectName("actionVoice_Feedback")
        self.actionModifier_une_base_de_donn_e = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_base_de_donn_e.setObjectName("actionModifier_une_base_de_donn_e")
        self.menuOutils.addAction(self.actionBloc_Note)
        self.menuOutils.addAction(self.actionImport_Export)
        self.menuOutils.addAction(self.actionHandler)
        self.menuR_seau.addAction(self.actionLobby_2)
        self.menuR_seau.addAction(self.actionScan_R_seau)
        self.menuR_seau.addAction(self.actionPaquets)
        self.menuInternet.addAction(self.actionMail)
        self.menuInternet.addAction(self.actionRecherche)
        self.menuInternet.addAction(self.actionPage_Internet)
        self.menuStockage.addAction(self.actionCoffre_Fort)
        self.menuStockage.addAction(self.actionArchiver_2)
        self.menuStockage.addAction(self.actionVeraCrypt)
        self.menuServeur.addAction(self.actionLobby)
        self.menuServeur.addAction(self.actionH_berger)
        self.menuConfiguration.addAction(self.actionModifier_le_fichier_de_configuration)
        self.menuConfiguration.addAction(self.actionVoice_Feedback)
        self.menuConfiguration.addAction(self.actionModifier_une_base_de_donn_e)
        self.menuCreator.addAction(self.actionPage_Createur)
        self.menuBar.addAction(self.menuOutils.menuAction())
        self.menuBar.addAction(self.menuR_seau.menuAction())
        self.menuBar.addAction(self.menuInternet.menuAction())
        self.menuBar.addAction(self.menuStockage.menuAction())
        self.menuBar.addAction(self.menuServeur.menuAction())
        self.menuBar.addAction(self.menuConfiguration.menuAction())
        self.menuBar.addAction(self.menuCreator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias"))
        self.label.setText(_translate("MainWindow", "Bonjour {}".format(Utilisateur)))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuR_seau.setTitle(_translate("MainWindow", "Réseau"))
        self.menuInternet.setTitle(_translate("MainWindow", "Internet"))
        self.menuStockage.setTitle(_translate("MainWindow", "Stockage"))
        self.menuServeur.setTitle(_translate("MainWindow", "Serveur"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuCreator.setTitle(_translate("MainWindow", "Createur"))
        self.actionBloc_Note.setText(_translate("MainWindow", "Bloc Note"))
        self.actionImport_Export.setText(_translate("MainWindow", "Import/Export"))
        self.actionArchiver.setText(_translate("MainWindow", "Archiver"))
        self.actionMail.setText(_translate("MainWindow", "Mail"))
        self.actionRecherche.setText(_translate("MainWindow", "Recherche"))
        self.actionCoffre_Fort.setText(_translate("MainWindow", "Coffre Fort"))
        self.actionArchiver_2.setText(_translate("MainWindow", "Archiver"))
        self.actionLobby.setText(_translate("MainWindow", "Page Server"))
        self.actionLobby_2.setText(_translate("MainWindow", "Page Réseau"))
        self.actionScan_R_seau.setText(_translate("MainWindow", "Scan Réseau"))
        self.actionPaquets.setText(_translate("MainWindow", "Paquets"))
        self.actionHandler.setText(_translate("MainWindow", "Handler"))
        self.actionVeraCrypt.setText(_translate("MainWindow", "VeraCrypt"))
        self.actionH_berger.setText(_translate("MainWindow", "Héberger"))
        self.actionModifier_le_fichier_de_configuration.setText(_translate("MainWindow", "Modifier le fichier de configuration"))
        self.actionPage_Createur.setText(_translate("MainWindow", "Page Createur"))
        self.actionPage_Internet.setText(_translate("MainWindow", "Page Internet"))
        self.actionVoice_Feedback.setText(_translate("MainWindow", "Voice Feedback"))
        self.actionModifier_une_base_de_donn_e.setText(_translate("MainWindow", "Modifier une base de donnée"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
