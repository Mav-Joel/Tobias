#!/usr/bin/env python3
#-*-coding:utf-8-*-
import webbrowser
import smtplib
from time import sleep
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import getpass
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

class sendMailWindow(object):
    def sendMail(self):
        try : 

            senderEmail = self.lineEdit.text()
            receiverEmail = self.lineEdit_2.text()
            message = MIMEMultipart("alternative")
            message["Subject"] = self.lineEdit_3.text()
            message["From"] = senderEmail
            message["To"] = receiverEmail

            text = self.plainTextEdit.toPlainText()
            html = text


            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            message.attach(part1)
            message.attach(part2)

            port = 465  # For SSL
            password = self.lineEdit_4.text()

            # Create a secure SSL context
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(senderEmail, password)
                server.sendmail(senderEmail, receiverEmail, message.as_string())
        except : 

            raise Exception("Mot de passe incorrect")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 261, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 261, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 170, 261, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(390, 10, 351, 411))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 341, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendMail)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 220, 361, 161))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 70, 261, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
      
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 120, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 30))
        self.menubar.setObjectName("menubar")
        self.menuParam_tres = QtWidgets.QMenu(self.menubar)
        self.menuParam_tres.setObjectName("menuParam_tres")
        self.menuPr_r_glages = QtWidgets.QMenu(self.menubar)
        self.menuPr_r_glages.setObjectName("menuPr_r_glages")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.actionVider_la_liste_de_contact = QtWidgets.QAction(MainWindow)
        self.actionVider_la_liste_de_contact.setObjectName("actionVider_la_liste_de_contact")
        self.menuParam_tres.addAction(self.actionVider_la_liste_de_contact)
        self.menuPr_r_glages.addAction(self.actionP1)
        self.menuPr_r_glages.addAction(self.actionP2)
        self.menuPr_r_glages.addAction(self.actionP3)
        self.menuPr_r_glages.addAction(self.actionP4)
        self.menuPr_r_glages.addAction(self.actionP5)
        self.menubar.addAction(self.menuParam_tres.menuAction())
        self.menubar.addAction(self.menuPr_r_glages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Mail Page"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "From"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "To"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Object"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Content"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Contact List"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Email\'s Password"))
        self.comboBox.setItemText(0, _translate("MainWindow", "All Contacts"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Top Half"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bottom Half"))
        self.menuParam_tres.setTitle(_translate("MainWindow", "Paramètres"))
        self.menuPr_r_glages.setTitle(_translate("MainWindow", "Préréglages"))
        self.actionP1.setText(_translate("MainWindow", "P1"))
        self.actionP2.setText(_translate("MainWindow", "P2"))
        self.actionP3.setText(_translate("MainWindow", "P3"))
        self.actionP4.setText(_translate("MainWindow", "P4"))
        self.actionP5.setText(_translate("MainWindow", "P5"))
        self.actionVider_la_liste_de_contact.setText(_translate("MainWindow", "Vider la liste de contact"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = sendMailWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





# source = sys.argv[1]
# Mdp = sys.argv[2]
# destinataire = sys.argv[3]
# objet = sys.argv[4]
# contenu = sys.argv[5]

# port_number =1234
# msg = MIMEMultipart()
# msg['From'] = 'sender@protonmail.com'
# msg['To'] = 'receiver@protonmail.com'
# msg['Subject'] = 'My Test Mail '
# message = 'This is the body of the mail'
# msg.attach(MIMEText(message))
# mailserver = smtplib.SMTP('localhost',port_number)
# mailserver.login("sender@protonmail.com", "mypassword")
# mailserver.sendmail('sender@protonmail.com','receiver@protonmail.com',msg.as_string())
# mailserver.quit()