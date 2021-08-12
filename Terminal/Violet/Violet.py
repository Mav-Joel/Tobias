#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket    
from bs4 import BeautifulSoup
import requests
import json
import os
import subprocess
from datetime import datetime
import smtplib, ssl
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import time

class Servs:
    def __init__(self):
        """SETUP THE SERVER"""
        self.machine = subprocess.getoutput("hostname")
        try : 
            open(f"./Report.txt")
            self.user = subprocess.getoutput("cat ./Report.txt | head -n3 | tail -n1 | awk '{print $4}'")
        
        except IOError:  
            if self.machine == "raspberrypi":

                checkName = input("[?] Violet :  L'appareil actuel semble être une raspberry pi, veuillez renseigner le nom d'utilisateur [no/name] \n> ")
                if checkName == "no":
                    self.user = subprocess.getoutput("whoami")
                else : 
                    self.user = checkName
                
                self.setup()
                self.install()

            else : 
                self.user = subprocess.getoutput("whoami")
                self.setup()
                self.install()

    def getMyPublicIp(self):
        try : 
            url = "https://www.monippublique.com/"

            session = requests.session()
            website = session.post(url)

            soup = BeautifulSoup(website.text, 'lxml')
            div = soup.find('span', {'class' : 'big-green'})
            return div.text
        except : 
            return 0
   
    def casualSweep(self):
        pass

    def sendMail(self):

        senderEmail = self.getModuleData("Email","Serv")
        receiverEmail = senderEmail

        message = MIMEMultipart("alternative")
        message["Subject"] = f"{self.machine}"
        message["From"] = senderEmail
        message["To"] = receiverEmail

        with open(f"./Report.txt","r") as content :
            text = content.read()
        
        text =  f'Online since {datetime.now()}\n \
        Server Name : {self.machine}\n \
        User Name : {self.user}\n \
        Network address : {self.getNetworkIp()}\n\
        Public address : {self.getMyPublicIp()}\n'

        html = f"""\
        <html>
        <body>
            <h1>Welcome Joël</h1>
                <ul>
                    <li>Online since {datetime.now()}</li>
                    <li>Server's Name : {self.machine}</li>
                    <li>User's Name : {self.user}</li>
                    <li>Network address : {self.getNetworkIp()}</li>
                    <li>Public address : {self.getMyPublicIp()}</li>
                <ul>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        port = 465  # For SSL
        password = self.getModuleData("appPassword","Serv")

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receiverEmail, message.as_string())

    def getNetworkIp(self):
        try : 
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            myIp=s.getsockname()[0]
            s.close()
            return myIp
        except :
            return 0

    def hote(self):

        knownRequests = [
            "close"
        ]

        host,port = ('',5566)
        prise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        prise.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
        prise.bind((host,port)) #Associer à Adresse IP
        print("Le serveur est initialisé")

        prise.listen(1) #Lier à port défini dans le tuple plus haut
        connexion, address = prise.accept()

        data = connexion.recv(1024) #Recevoir une donnée
        data = data.decode("utf8")
        print(data)
        print(connexion)
        for i in range(len(knownRequests)):
            if data == knownRequests[i]:
                print(data)
            else : 
                self.sendNotice(f"L'adresse IP : {connexion} a établie un contact en envoyant : {data}")

        connexion.close()
        prise.close()

    def sendNotice(self,msg):

        senderEmail = self.getModuleData("Email","Serv")
        receiverEmail = senderEmail

        message = MIMEMultipart("alternative")
        message["Subject"] = f"{self.machine}"
        message["From"] = senderEmail
        message["To"] = receiverEmail

        part1 = MIMEText(msg, "plain")

        message.attach(part1)

        port = 465  # For SSL
        password = self.getModuleData("appPassword","Serv")

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receiverEmail, message.as_string())

    def getModuleData(self,searchingFor,fieldName='user'):

        with open(f"/Users/{self.user}/Terminal/.Violet/Settings/Confs/Configuration.json","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values
   
    def getPaths(self,searchingFor,fieldName='Archives'):
        with open(f"/Users/{self.user}/Terminal/.Violet/Settings/Paths/filesPaths.json","r") as variable:
            content = json.load(variable)
        
        for parameters in content['Paths'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def actualize(self):
        newConfig = {
            "Configurations": [
            {
                "Serv": {
                "name": f"{self.machine}",
                "localDbPassword": f"{self.getModuleData('localDbPassword','Serv')}",
                "Address": f"{self.getMyPublicIp()}",
                "Email": f"{self.getModuleData('Email','Serv')}",
                "appPassword": f"{self.getModuleData('appPassword','Serv')}",
                }
            }
            ]
        }
        with open(f"/Users/{self.user}/Terminal/.Violet/Settings/Confs/Configuration.json","w") as config :
            json.dump(newConfig,config,indent=2)
    def checkIp(self):
        storedAddress = self.getModuleData("Address","Serv")
        if storedAddress != self.getMyPublicIp():
            if self.getMyPublicIp() != 0:
                self.sendMail()
                self.actualize()
            else : 
                self.actualize()
    def setup(self):

        newConfig = {
            "Configurations": [
            {
                "Serv": {
                "name": f"{self.machine}",
                "localDbPassword": f"{self.getModuleData('localDbPassword','Serv')}",
                "Address": f"{self.getMyPublicIp()}",
                "Email": f"{self.getModuleData('Email','Serv')}",
                "appPassword": f"{self.getModuleData('appPassword','Serv')}",
                }
            }
            ]
        }
        with open(f"/Users/{self.user}/Terminal/.Violet/Settings/Confs/Configuration.json","w") as config :
            json.dump(newConfig,config,indent=2)
        
        pathConf = {
                "Paths": [
                {
                    "Configs": {
                    "path": f"/Users/{self.user}/Terminal/.Violet/Settings/Confs/Configuration.json"
                    }
                }
                ]
            }
        with open(f"/Users/{self.user}/Terminal/.Violet/Settings/Paths/filesPaths.json","w") as config :
            json.dump(pathConf,config,indent=2)

        with open(f"./Report.txt","w") as Report :
            Report.write(f"Online since {datetime.now()}\n")
            Report.write(f"Server's Name : {self.machine}\n")
            Report.write(f"User's Name : {self.user}\n")
            Report.write(f"Network address : {self.getNetworkIp()}\n")
            Report.write(f"Public address : {self.getMyPublicIp()}\n")
        
        self.sendMail()
             
    def install(self):
        os.system(f"chmod u+x /Users/{self.user}/Terminal/.Violet/setup.sh && /Users/{self.user}/Terminal/.Violet/setup.sh")
        os.system(f"crontab -l >> ~/Cron && echo '* * * * * cd /Users/{self.user}/Terminal/.Violet && ./Violet.py' >> ~/Cron && crontab ~/Cron && rm ~/Cron")
#EXECUTE
if __name__ == "__main__":
    Server = Servs()
    Server.checkIp()
    # Server.hote()
    