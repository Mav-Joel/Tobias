# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HostGI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 321, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label1_2 = QtWidgets.QLabel(self.frame)
        self.label1_2.setGeometry(QtCore.QRect(120, 10, 61, 31))
        self.label1_2.setObjectName("label1_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 240, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 90, 151, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 50, 181, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label1_3 = QtWidgets.QLabel(self.frame)
        self.label1_3.setGeometry(QtCore.QRect(240, 80, 61, 31))
        self.label1_3.setObjectName("label1_3")
        self.label1_4 = QtWidgets.QLabel(self.frame)
        self.label1_4.setGeometry(QtCore.QRect(120, 200, 61, 31))
        self.label1_4.setObjectName("label1_4")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(120, 130, 111, 31))
        self.label1.setObjectName("label1")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 280, 191, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(370, 10, 591, 361))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBackBone = QtWidgets.QAction(MainWindow)
        self.actionBackBone.setObjectName("actionBackBone")
        self.actionVue_Compl_te = QtWidgets.QAction(MainWindow)
        self.actionVue_Compl_te.setObjectName("actionVue_Compl_te")
        self.actionADD = QtWidgets.QAction(MainWindow)
        self.actionADD.setObjectName("actionADD")
        self.actionNetwork_csv = QtWidgets.QAction(MainWindow)
        self.actionNetwork_csv.setObjectName("actionNetwork_csv")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Host/Client Project"))
        self.label1_2.setText(_translate("MainWindow", "Sockets"))
        self.pushButton.setText(_translate("MainWindow", "Se connecter"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Adresse du Serveur"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Port 5566 par défaut"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Hôte Localhost par défaut"))
        self.pushButton_2.setText(_translate("MainWindow", "Héberger"))
        self.label1_3.setText(_translate("MainWindow", "Serveur"))
        self.label1_4.setText(_translate("MainWindow", "Client"))
        self.label1.setText(_translate("MainWindow", "Etat serveur : Off"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "Port"))
        self.actionBackBone.setText(_translate("MainWindow", "BackBone"))
        self.actionVue_Compl_te.setText(_translate("MainWindow", "Vue Complète"))
        self.actionADD.setText(_translate("MainWindow", "ADD"))
        self.actionNetwork_csv.setText(_translate("MainWindow", "Network.csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
