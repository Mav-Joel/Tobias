#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import paramiko
import mysql
import mysql.connector
import os
# self.MagicWord=os.environ["MDP"]
#Créer un utilisateur
# mydb = mysql.connector.connect(
# host="localhost",
# user="Python",
# passwd=self.MagicWord,
# )

# Command=mydb.cursor()
# Command.execute("USE tobiasdb")

# Ins="CREATE USER 'tobias'@'10.96.26.197' IDENTIFIED BY 'BladeDBfromTobias'"
# then = "GRANT ALL ON `tobiasdb`.* TO'tobias'@'10.96.26.197'"
# well = "FLUSH PRIVILEGES"
# Command.execute(Ins,then,well)
# mydb.commit()

# os.system("scp -r /home/Utilisateur/Archetype/Tobi/HUB pi@192.168.1.31:~/")


# #Ouvrir la base de donnée à distance
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect("192.168.1.31",port=22 ,username="pi",password="Razerberry")
# stdin,stdout,stderr=ssh.exec_command("cd /home/pi/HUB/HUB && virtualenv DjangoEnv && source /home/pi/HUB/HUB/DjangoEnv/bin/activate && pip3 install django && pip3 install django-debug-toolbar && pip3 install mysql && ./manage.py runserver 0.0.0.0:8000")
