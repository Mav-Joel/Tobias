#!/usr/bin/env python3
#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import webbrowser
from time import sleep
import mechanicalsoup
import csv
import unidecode
import os
import itertools
import time
from threading import Thread
import threading
import random
# from PyPDF2 import PdfFileReader
Utilisateur=os.environ["USER"]

class Scrap :
    def __init__(self):
        self.url = "https://moodle.iut-kourou.fr/login/index.php"
        #self.url = "https://httpbin.org/post"
        self.website = requests.post(self.url)
        self.emploiDuTemps = "https://moodle.iut-kourou.fr/course/view.php?id=142"

    def isAccessible(self):
        print("Le site : {} est-il accessible ? : {}".format(self.url,self.website.ok))

    def getEmploiDuTemps(self):
        #Get Login Token
        session = requests.session()
        self.website = session.post(self.url)

        soup = BeautifulSoup(self.website.text, 'lxml')
        div = soup.find('input', {'name' : 'logintoken'})['value']
        auth = {'logintoken': div, 'username': 'guest', 'password': 'guest'}

        self.website = session.post(self.url, data=auth)
        emploiDuTemps = session.get(self.emploiDuTemps)

        #Emploi du temps
        soup = BeautifulSoup(emploiDuTemps.text,'lxml')
        links = []
        i=0
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        
        a = links[22] #Emploi du temps n°1
        b = links[23] #Emploi du temps n°2
        
        print(a)
        print(b)

        #Enregister
        getTimeTable1 = session.get(a)
        getTimeTable2 = session.get(b)

        with open(f"/home/{Utilisateur}/Bureau/"+soup.title.text+"A.pdf","wb") as variable :
            variable.write(getTimeTable1.content)
            variable.close()

        with open(f"/home/{Utilisateur}/Bureau/"+soup.title.text+"B.pdf","wb") as variable :
            variable.write(getTimeTable2.content)
            variable.close()

    def getMyPublicIp(self):
        self.url = "https://www.monippublique.com/"
    
        session = requests.session()
        self.website = session.post(self.url)

        soup = BeautifulSoup(self.website.text, 'lxml')
        div = soup.find('span', {'class' : 'big-green'})
        print(div.text)

class SecureScraping():
    def __init__(self):
        self.pool = [
        "35.185.16.35:80",
        "85.175.227.3:7014",
        "178.128.245.251:8080",
        "47.254.151.148:8080",
        "35.185.16.35:80",
        "181.129.183.19:53281",
        "140.227.11.26:3128",
        "1.20.101.149:44778"
        ]

        self.session = requests.session()
        self.proxyList = random.randint(0, len(self.pool) - 1)
    
        self.session.proxies = {
            'http':f'http://{self.pool[self.proxyList]}',
            'https':f'https://{self.pool[self.proxyList]}'
        }
        print(self.session.proxies)
    
    def getIp(self):
        try : 
            Connexion = self.session.get('http://httpbin.org/ip',timeout=10)
            print(Connexion.text)
        
        except : 
            print("Timeout")
            self.proxyList = random.randint(0, len(self.pool) - 1)
            self.session.proxies = {
            'http':f'http://{self.pool[self.proxyList]}',
            'https':f'https://{self.pool[self.proxyList]}'
        }
            Connexion = self.session.get('http://httpbin.org/ip',timeout=10)
            print(Connexion.text)
       
class CompteRendu():
    def __init__(self, *args):
        self.url = "https://moodle.iut-kourou.fr/login/index.php"
        self.website = requests.post(self.url)
        self.tp = args[0]


    def getTp(self,min,max):
    #Récupérer le TP
        session = requests.session()
        self.website = session.post(self.url)
       
        soup = BeautifulSoup(self.website.text, 'lxml')
        div = soup.find('input', {'name' : 'logintoken'})['value']
        auth = {'logintoken': div, 'username': 'toulaj', 'password': '20020113'}

        self.website = session.post(self.url, data=auth)
        tpLocation = session.get(self.tp)
        soup = BeautifulSoup(tpLocation.text,'lxml')
        links = []
        i=0
        for link in soup.find_all('a'):
            links.append(link.get('href'))
            print(str(link.get("href"))+" "+str(i))
            i=int(i)
            i=i+1

        parse = 0
        listeDeTP = []
        for parse in range(min,max):
            listeDeTP.append(links[parse])
            print(links[parse])        
        
        print("{} travaux pratiques ont été trouvé \n".format(len(listeDeTP)))
        numTP = input("Quel TP voulez vous télécharger ? \nInput : ") 
        print(listeDeTP[int(numTP)-1])
        
        tpFile = session.get(listeDeTP[int(numTP)])
        print(tpFile.content)
        
        with open(f"/home/{Utilisateur}/Archetype/Tobi/TP"+numTP+".pdf","wb") as variable :
            variable.write(tpFile.content)
            variable.close()


    def getPdfText(self):
    #Récupérer les questions et autres
        path = f"/home/{Utilisateur}/Archetype/Tobi/TP2.pdf"
        pdf = PdfFileReader(path)
        outputFile = f"/home/{Utilisateur}/Archetype/Tobi/TP2CR.txt"
        with open(outputFile,"w") as variable :
            for page in pdf.pages:
                text = page.extractText()
                variable.write(text)

    def parsePDF(self):
        with open(f"/home/{Utilisateur}/Archetype/Tobi/TP2CR.txt","r") as variable :
            for line in variable.readlines():
                if 'Etape 1' in line :
                    print("hey")   
                             
    def createPdf(self):
    #Créer mon PDF
        pass
    def getAnswers(self):       
    #Remplir mes réponses venant d'un fichier txt
        pass
    
    def sendToMoodle(self):
    #Envoyer sur Moodle
        pass


class findMacProvider():
    def perm(self,occ):
        premute = []
        token = "czoyNjoiOWZ0MjFiMjRydmQyMWw4MDRlNzVjMTczdzef"
        a = itertools.permutations(token,len(token))

        for i in a : 
            permutations = "".join(i)
            permutations = permutations+"=="
            premute.append(permutations)
        return premute[occ]

    def getMacProvider(self):
        token = "czoyNjoiw4MDRlNzVjMTczdzef=="
        cheminFichier = f"/home/{Utilisateur}/Bureau/userlist.csv"

        classe = []
        nom = []
        prenom = []
        mail = []

        with open(cheminFichier,"r") as csvFile :
            csvContent = csv.reader(csvFile)

            next(csvContent)

            for lines in csvContent :
            
                classe.append(lines[0])
                nom.append(lines[1])
                prenom.append(lines[2])
                mail.append(unidecode.unidecode(lines[2]).lower()+"."+unidecode.unidecode(lines[1]).lower()+"@etu.iut-kourou.fr")
        
        for i in range(0,len(nom)) :
            with open(f"/home/{Utilisateur}/Archetype/WorkBench/perm.txt","r") as variable :
                link = "https://www.sondageonline.fr/s/5c3cf80"
                token = variable.readlines(i)
                browser = mechanicalsoup.StatefulBrowser()
                browser.session.cookies.clear() 
                browser.open(link)
                browser.select_form('form[id="weiter"]')
                browser["zutritt"] = ""
                browser["tan"] = ""
                browser["history"] = "YjowOw=="
                browser["sid"] = "aToxMDAxMTA5NDs"
                browser["s"] = "{}".format(token)
                browser["element-35-21747019-15506716-1"] = "{}".format(prenom[i])
                browser["element-35-21747019-15506717-1"] = "{}".format(nom[i])
                browser["element-35-21747019-15506718-1"] = "{}".format(classe[i])
                browser["element-35-21747019-15506719-1"] = "{}".format(mail[i])
                browser["element-21-21746994"] = "49930805"
                response = browser.submit_selected()
                print(prenom[i])
                print(nom[i])
                print(classe[i])
                print(mail[i])
                print(response.text)
                browser.session.cookies.clear() 



        # session = requests.session()
        # self.website = session.post(self.url)
        
        # soup = BeautifulSoup(self.website.text, 'lxml')
        # print(soup)


        # # 2
        # form = login_html.select("form")[0]
        # form.select("input")[0]["value"] = "zeus"
        # form.select("input")[1]["value"] = "ThunderDude"

        # # 3

class Crawler():
    pass
if __name__ == "__main__":
    # Scrap().getMyPublicIp()
    # SecureScraping().getIp()
    Scrap().getEmploiDuTemps()
    # findMacProvider().getMacProvider()