#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
import notify2
from twilio.rest import Client
from gtts import gTTS
import speech_recognition as sr
import os
import re
import subprocess
import webbrowser
import smtplib
import requests
import smtplib
import json
from email.mime.text import MIMEText
import time
import mysql 
import mysql.connector
from time import strftime
from datetime import datetime
import functools

"""Variables d'environnement"""

user=os.environ["USER"]
Utilisateur=os.environ["USER"]


class Tools():
    def __init__(self):
        self.MagicWord = self.getModuleData("local dbpassword","Tobias")

    def getModuleData(self,searchingFor,fieldName='user'):
        with open(f"/home/{user}/Archetype/Tobi/Admin/Configurations.json","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def Insert_Into_Bashrc(self,write): #Écrire dans le Bashrc
        with open("/home/"+user+"/.bashrc","a") as Variable :
            Variable.write(str(write))
            Variable.close()

    def Notification(self,Message): #Notifie le Message

        notify2.init("Tobias")
        n = notify2.Notification("Tobias Information",message=Message)
        n.show()

    def Saut_de_Lignes(self,Variable) :
        Variable.write("\n")

    def Archiver(self,Nom_Archive,Nom_Fichier):

        with zipfile.ZipFile(Nom_Archive,"w") as variable:
            variable.write(Nom_Fichier)

    def Extraire(self):
        zipfile.ZipFile.extract(f"/home/{Utilisateur}/base","Archive.zip ")

    def SMS(self,Num,Message) :
        account_sid = "AC3feaac267028a50163d4ea3e26c443db"
        auth_token = "276b5f23c702804031e19e33f3c39575"

        client=Client(account_sid,auth_token)
        client.messages.create(
            to = "+594"+Num,
            from_="+12028838988",
            body=Message

        )

    def Tell_me(self,Message):
        account_sid = "AC3feaac267028a50163d4ea3e26c443db"
        auth_token = "276b5f23c702804031e19e33f3c39575"

        client=Client(account_sid,auth_token)
        client.messages.create(
            to = "+5940694232624",
            from_="+12028838988",
            body=Message
        )

    def talktoMe(self,audio):
        currentIp = subprocess.getoutput("ip a | egrep \" inet \" | egrep \"brd\" | awk '{print $2}' | sed -re \"s/\/..//g\" | head -n1")
        
        #Sauvegarder le text
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        Ins="INSERT INTO rapportExecution (id , Programme , Information) VALUES (NULL , 'print' , '{}')".format(str(audio+" "+str(datetime.now())))
        Command.execute(Ins)
        mydb.commit()

        if currentIp != "":

            print(audio)
            tts=gTTS(text=audio,lang="en")
            tts.save('audio.mp3')
            os.system("mpg123 audio.mp3")

        else : 
            print(audio)
            #raise Exception("Non connecté à un internet")

    def sendMail(self,objet,contenu):
        time.sleep(10)
        message = MIMEText(str(contenu))
        message['Subject'] = str(objet)

        message['From'] = 'joel.toula@gmail.com'  
        message['To'] = 'joel.toula@gmail.com'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('joel.toula@gmail.com','')
        server.send_message(message)
        server.quit()

    def myCommand(self):
        "listens for commands"

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Ready...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            command = myCommand()

        return command

    def MsgSystem(self,thing,way):
        print(" [{}] Tobias : {}".format(way,thing))

    """DEBUG"""
