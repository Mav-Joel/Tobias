#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import mysql.connector
import ast
import os
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.TBook import Tools
magicWords = Tools().getModuleData("localDbPassword","Tobias")

Utilisateur=os.environ["USER"]
def MyConverter(mydata):
    def cvt(data):
            try : 
                return ast.litteral_eval(data)
            except Exception:
                return str(data)
    return tuple(map(cvt,mydata))

class updateWindow(object):

    def LoadData(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=magicWords,
        )

        Command = mydb.cursor()
        Command.execute("USE tobiasdb") 
        Command.execute("SELECT * FROM knownIps")
        data = Command.fetchall()

        for row in data : 
            self.addTable(MyConverter(row))

        Command.close()
    
    def addTable(self,columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
                self.tableWidget.setItem(rowPosition, i , QtWidgets.QTableWidgetItem(str(column)))

    def stocker(self): 
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=magicWords,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        Ins="INSERT INTO knownIps (id,hostname,address) VALUES (NULL , '{}' , '{}')".format(self.lineEdit_2.text(),self.lineEdit.text()) 
        
        Command.execute(Ins)
        mydb.commit()

    def init(self):
        self.LoadData()
        self.stocker()
        self.LoadData()
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 10, 691, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 280, 251, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 280, 251, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 280, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.init)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tobias\'s Update Hosts Page"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Adresse ip à rajouter"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Nom "))
        self.pushButton.setText(_translate("MainWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = updateWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
