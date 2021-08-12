#!/usr/bin/env python3
#-*-coding:utf-8-*-
import getpass
import json
import os
import socket
import subprocess
import sys
import threading
import time

import mysql
import mysql.connector

from Library.DBook import Database
from Library.TBook import Tools


class Creator():
    def __init__(self) :
        self.MagicWord=self.getModuleData("localDbPassword","Tobias") 

    def choiceList(self):
        """SETUP THE FIRST MENU"""
        
        eachChoices = [
                "Créer un bloc",
                "Créer une fonctionnalité",
                "Lancer une fonctionnalité",
        ] #Choices the user can choose to move on

        execute = {
            "1" : "self.createBloc()",
            "2" : "self.createFeature()",
            "3" : "self.feature()"
        } #Action launched when the user chooses a number

        os.system("clear")

        for element in range(eachChoices.__len__()): #Fetch choices
            
            print(f"({element+1}) {eachChoices[element]} |",end = " \n") #Display the menu

        answer = input("----> Votre choix : ")

        for keys,values in execute.items() : # If the answer is correct, check what the answer does
            if answer is keys :
                exec(values)
            else : #If not, do while the answer is not a key
                while answer != keys :
                    answer = input("----> Votre choix : ")
                    if answer is keys :
                        exec(values)

    def createBloc(self):

        os.system("clear")

        self.nom = input("Nom du bloc : ")
        self.category = input("Catégorie du bloc [ Primaire | Secondaire | Script | multipleInput ]: ")
        self.command = input("Commande à Éxecuter: \n > ")
        
        if self.category != "Primaire":
            self.pattern = input("Emplacement dans le pattern: \n > ")
        else :
            self.pattern = 0

        Database("creator","id","name","type",
        "command","category","pattern",
        "NULL",f"{self.nom}","Bloc",f"{self.command}",
        f"{self.category}",f"{self.pattern}").insertInDatabase()

        print("Bloc créer avec succès")
        time.sleep(1)
        self.choiceList()
        # Tools().Notification("Block Successfully Created")

    def fill(self):
        self.MagicWord=self.getModuleData("localDbPassword","Tobias")
        
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        self.primaryContent = []
        self.secondaryContent = []
        self.featureContent = []
        self.globalContent = []
        self.globalPrimaryItems = []
        self.Weird = []
        self.scriptContent = []
        self.multipleContent = []

        Command = self.mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Primaire' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.primaryContent.append(lettre)


        Command = self.mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Primaire' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.primaryContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Secondaire' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.secondaryContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Script' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                self.scriptContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator")

        for x in Command:
            for lettre in x :
                self.globalContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE type='Feature'")

        for x in Command:
            for lettre in x :
                self.featureContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='multipleInputs'")

        for x in Command:
            for lettre in x :
                self.multipleContent.append(lettre)

        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE category='Primaire'")

        for x in Command:
            for lettre in x :
                self.globalPrimaryItems.append(lettre)

        os.system("clear")
        blocDisplayed = []

        for i in range(0,len(self.multipleContent)):
            if len(self.multipleContent) == 0 :
                print("Aucun bloc prenant plusieur points d'entrées")
            else :
                print(self.multipleContent[i]+"\n")
                blocDisplayed.append(self.multipleContent[i])
                print(" "+"_"*len(self.multipleContent[i]))
                print("|"+self.multipleContent[i]+"|"+f" Bloc à MultiInput | Command : [{self.getCommand(self.multipleContent[i])}]")
                print(" "+"-"*len(self.multipleContent[i]))

        for i in range(0,len(self.primaryContent)):
            if len(self.primaryContent) == 0 :
                print("Aucun blocs Primaires")
            else :
                print(" "+"_"*len(self.primaryContent[i]))
                blocDisplayed.append(self.primaryContent[i])
                print("|"+self.primaryContent[i]+"|"+f" Bloc Primaire | Command : [{self.getCommand(self.primaryContent[i])}]")
                print(" "+"-"*len(self.primaryContent[i]))

        for i in range(0,len(self.secondaryContent)):
            if len(self.secondaryContent) == 0 :
                print("Aucun blocs Secondaires")
            else :
                print(" "+"_"*len(self.secondaryContent[i]))
                blocDisplayed.append(self.secondaryContent[i])
                print("|"+self.secondaryContent[i]+"|"+f" Bloc Secondaire | Command :  [{self.getCommand(self.secondaryContent[i])}]")
                print(" "+"-"*len(self.secondaryContent[i]))

        for i in range(0,len(self.scriptContent)):
            if len(self.scriptContent) == 0 :
                print("Aucun blocs Scripts")
            else :
                print(" "+"_"*len(self.scriptContent[i]))
                blocDisplayed.append(self.scriptContent[i])
                print("|"+self.scriptContent[i]+"|"+f" Bloc Scripts | Command : [{self.getCommand(self.scriptContent[i])}]")
                print(" "+"-"*len(self.scriptContent[i]))

        if len(self.blocList) != 0 :
            print(f"Vos blocs sélectionnés : {self.blocList}")
        print("_______________________________________________________________")
        nextAction = input("\n(1) Utiliser un bloc   \n(2) Chercher par lettres   \n(3) Créer une fonctionnalité avec les blocs actuelles   \n(4) Supprimer un bloc de la pioche  \n(5) Retour \n----> Votre choix : ")
        
        self.goodWords = []
        good = 1

        choices = ["1","2","3","4","5"]
        for y in range(len(choices)):
            if choices[y] == nextAction :
                good = 0

        if good != 0 :
            for i in range(len(blocDisplayed)):
                if nextAction == blocDisplayed[i]:
                    self.blocList.append(nextAction)
                    self.fill()
                else :
                    if blocDisplayed[i].count(nextAction) > 0:
                        self.goodWords.append(blocDisplayed[i])

            if len(self.goodWords) == 0:
                print("Votre bloc n'existe pas")
                time.sleep(0.5)
                self.fill()
            else: 

                for i in range(len(self.goodWords)):
                    print(f"Bloc correspondant à la description {self.goodWords[i]}\n ------")
                
                answer = input("Lequel est ce ? [nom/aucun] \n ----> Votre choix : ")
                if answer == "aucun ":
                    self.fill()
                else : 
                    self.blocList.append(answer)
                    self.fill()


        if nextAction == "1" :

            blocToSelect = input("Quel est son nom ou numéro ? \n : ")
            right = 0
            for i in range(len(blocDisplayed)):
                if blocToSelect != blocDisplayed[i] :
                    right += 1
                    if right == len(blocDisplayed) :
                        print("Votre bloc n'existe pas")
                        time.sleep(0.5)
                        self.fill()
                else :
                    self.blocList.append(blocToSelect)
                    self.fill()

        elif nextAction == "2" :
            count = 0 
            blocToSearchFor = input("Quel est son nom ? \n : ")
            for i in range(len(blocDisplayed)):
                if blocDisplayed[i].count(blocToSearchFor) > 0:
                    count +=1 
                    print(f"Bloc correspondant à la description {blocDisplayed[i]}\n ------")
                    answer = input("Lequel est ce ? [nom/aucun] \n ----> Votre choix : ")
                    if answer == "aucun ":
                        self.fill()
                    else : 
                        self.blocList.append(answer)
                        self.fill()
            
            if count == 0:
                print("Votre bloc n'existe pas")
                self.fill()

        elif nextAction == "3":
            if len(self.blocList) != 0:
                self.save()
                self.feature()
            else :
                print("[!] Votre pioche est vide...")
                time.sleep(0.5)
                self.fill()

        elif nextAction == "4":
            if len(self.blocList) != 0:
                if len(self.blocList) == 1 : 
                    self.blocList.remove(self.blocList[0])
                    self.fill()
                
                name = input("Nom du bloc à retirer \n : ")
                
                if len(self.blocList) >1 : 
                    self.blocList.remove(name)
                    self.fill()
            else :
                print("[!] Votre pioche est vide...")
                time.sleep(0.5)
                self.fill()

        elif nextAction == "5":
            os.system("clear")
            self.choiceList()

        else :
            self.fill()

    def save(self):
        os.system("clear")
        foncName = input("Nom de la fonctionnalité ? \n : ")
        indexObjets = []
        nObjets = len(self.blocList)

        #Récupérer les éléments
        indexObjets = self.blocList

        if nObjets > 0:
            Command = self.mydb.cursor()
            Command.execute("USE tobiasdb")

            Command.execute(f"INSERT INTO creator (id , name , type , command , category,pattern) VALUES (NULL , '{foncName}' , 'Feature' , \"{indexObjets}\", 'Primaire',0)")
            self.mydb.commit()
            # Tools().Notification("Feature Successfully Added")
            os.system("clear")
            self.choiceList()

    def createFeature(self):
        os.system("clear")
        self.fill()

    def feature(self):
        self.MagicWord=self.getModuleData("localDbPassword","Tobias")
        self.featureContent = []
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        Command = self.mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute("SELECT DISTINCT(name) FROM creator WHERE type='Feature'")

        for x in Command:
            for lettre in x :
                self.featureContent.append(lettre)

        os.system("clear")
        print(f"Liste des fonctionnalités : {self.featureContent}")
        featureToExecute = input("Que voulez vous éxecuter ? \n :  ")

        pattern = []

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=self.MagicWord, port="8889",
        )

        #Déterminer les éléments de type Fonctionnalité

        Command = self.mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute(f"SELECT command FROM creator WHERE name='{featureToExecute}' AND category !='Script'")

        for x in Command:
            for lettre in x :
                pass

        lettre = str(lettre)
        lettre = lettre.strip("[]")
        lettre = lettre.replace("',","")
        lettre = lettre.replace("'","")
        firstStageCommands = lettre.split()

        #Déterminer les commandes de ces éléments
        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor()
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE name='"+firstStageCommands[i]+"' AND type='Bloc' AND category!='Script'")
            for x in Command:
                for lettre in x :
                    firstStageCommands[i] = lettre

        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor()
            Command.execute("USE tobiasdb")
            Command.execute(f"SELECT command FROM creator WHERE name='{firstStageCommands[i]}' AND type='Bloc' AND category='Script'")
            for x in Command:
                for lettre in x :
                    a = subprocess.getoutput(lettre)
                    firstStageCommands[i] = a
                    pattern.append(a)

                    Command = self.mydb.cursor()
                    Command.execute("USE tobiasdb")
                    Command.execute("SELECT pattern FROM creator WHERE command='"+lettre+"' AND type='Bloc' AND category='Script'")
                    for x in Command:
                        for lettre in x:
                            pattern.append(lettre)

        #Check for Pattern
        for i in range(0,len(firstStageCommands)):
            Command = self.mydb.cursor()
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command,pattern FROM creator WHERE command='"+firstStageCommands[i]+"' AND type='Bloc' AND category='Secondaire'")
            for x in Command:
                for lettre in x :
                    pattern.append(lettre)

        list_of_strings = [str(s) for s in firstStageCommands]
        joined_string = " ".join(list_of_strings)
        string = joined_string.split()
        stringList = []
        for i in range(0,len(string)):
            stringList.append(string[i])
            stringList.append(" ")
        workingUnits = []
        byOne = []
        #Détermine les secteurs ayant besoin d'une modification
        pos = []
        var_pos = 0
        for sector in stringList:
            num = sector.count("$")
            if num > 0:
                workingUnits.append(sector)
                pos.append(var_pos)
                var_pos +=1
            else :
                var_pos +=1

        #Change le string en liste de caractères
        for elements in range(0,len(workingUnits)):
            elementString = workingUnits[elements]
            for caracter in range(0,len(elementString)):
                byOne.append(elementString[caracter])
            byOne.append(" ")

        byOne = byOne[:-1]
        val = 0
        #Change $n par la bonne valeur du pattern
        for cell in range(0,len(byOne)):
            if byOne[cell] == "$":
                if int(byOne[cell+1]) == 1:
                    val = -1
                elif int(byOne[cell+1]) == 2:
                    val = 0
                else :
                    val +=1

                byOne[cell+1] = pattern[int(byOne[cell+1])+val]

            final = ""
            for i in byOne:
                final = final+str(i)
            final = final.replace("$","")
            final = final.split()

            finalList = []
            for i in range(0,len(final)):
                finalList.append(final[i])

            for i in range(0,len(stringList)):
                for y in range(0,len(pattern)):
                    if stringList[i] == pattern[y]:
                        stringList[i] = " "

        for i in range(0,len(pos)):
            stringList[pos[i]] = finalList[i]

        full = stringList
        if stringList.count("X1") > 0:
            #TROUVER LA BOUCLE
            position = 0
            indexGet = []

            for i in range (0,len(stringList)):
                if stringList[i] == "for":
                    indexGet.append(position)
                    position +=1
                elif stringList[i] == "end" :
                    indexGet.append(position)
                    position +=1
                else :
                    position +=1

            #TROUVER LE COMMENCEMENT ET LA FIN
            doing = []
            i = 0
            while i != int(len(indexGet)):
                start = indexGet[i]
                end = indexGet[i+1]

                start = int(start)
                end = int(end)

                #LES RECUPERER
                condition = stringList[start:end]
                stage_1 = condition[0:9]
                stage_1[6] = stage_1[8]
                numberOT = stage_1[8]
                stage_1.pop(8)
                i = i+2
                condition = stringList[start:end]

                condition[6] =  stage_1[6]
                condition.pop(8)
                condition.pop(8)


                #GET THE THINGS THAT NEED TO BE DONE
                do = condition[7:end]
                do = "".join(do)
                doing.append(do)

            inputs=[]
            #Déterminer les commandes de ces éléments

            Command = self.mydb.cursor()
            Command.execute("USE tobiasdb")
            Command.execute("SELECT command FROM creator WHERE category='multipleInputs' AND type='Bloc'")
            for x in Command:
                for lettre in x :
                    for i in range(0,len(stringList)):
                        if lettre in stringList[i]:
                            inputs.append(lettre)
            if len(inputs) == 0:
                inputs.append(numberOT)

            numberOI = 0
            try :
                numberOT = int(numberOT)
                numberOI = numberOT
            except:
                numberOT = None
                numberOI = len(inputs)

            for i in range(0,numberOI):
                if numberOT is not None:
                    a = numberOT
                    a = str(a)
                else :
                    proc = subprocess.Popen(['python3', inputs[i]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    a = proc.communicate()[0]
                    a = a.decode("utf-8")
                    a = str(a)
                    a = a.strip("[")
                    a = a.strip("]")
                    a = a[:-2]

                    a = a.replace("',","")
                    a = a.replace("'","")
                a = a.split()
                i=0
                while i != len(doing):
                    word = doing[i]
                    word = word.split()
                    for k in range(0,len(word)):
                        print(word)
                        if word[k] == "X2":
                            for y in range(0,len(a)):
                                word[k] = a[y]
                                word = " ".join(word)
                                print(word)
                                os.system(word)
                                word = do.split()
                    i +=len(doing)


            #A REFAIRE
            for i in range(indexGet[0],indexGet[-1]+1):
                full[i] = "TODELETE"


            good = []
            for i in range(0,len(full)):
                if full[i] != "TODELETE":
                    good.append(full[i])

            commande = "".join(good)
            print(f"La commande à éxecuter est : {commande}")
            os.system(commande)
        else :
            commande = "".join(stringList)
            print(f"La commande à éxecuter est : {commande}")
            os.system(commande)

    def getCommand(self,blocName):
        Command = self.mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute(f"SELECT command FROM creator WHERE name='{blocName}' AND type='Bloc'")

        for x in Command:
            for lettre in x :
                return lettre

class Tobias(Creator):

    def __init__(self):
        self.blocList = []
        self.confs = self.getPaths('path','ConfigurationJson')
        self.networkB = self.getPaths('network','sysCommandsDirectory')
        self.user = os.environ["USER"] #User's name


        # try :
        #     open(f".started.txt")

        # except IOError:

        #     self.fromZeroToHero() #Working

        threadLogin = threading.Thread(target=self.login())
        threadLogin.start()

    def fromZeroToHero(self):

        """Install needed packages"""
        packages = [
            "python-nmap",
            "PyQt5",
            "notify2",
            "django",
            "django-debug-toolbar",
            "gtts",
            "pyshark",
            "nginx",
            "speechRecognition" ,
            "mysql",
            "mysql-connector",
            "paramiko",
            "install --pre scapy[basic]",
            "mechanicalsoup",
            "beautifulsoup4",
            "git",
            "pandas",
            "unidecode"
        ]

        for i in range (0,len(packages)):
            a = subprocess.getoutput(f"which {packages[i]}")
            if a != f"/usr/bin/{packages[i]}" :
                #print(f"{packages[i]} is not installed")
                os.system(f"pip3 install {packages[i]}")

        os.system("clear")

        with open(f"/Users/{self.user}/Terminal/.started.txt","w") as variable :
            variable.write("Started")

    def myIp(self,toSearch):
        """Give my Ip Address and Mask"""
        if toSearch == "ip":
            try :

                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                myIp=s.getsockname()[0]
                s.close()
                return myIp

            except OSError :

                myIp = subprocess.getoutput("ip a | egrep 'inet' | egrep 'brd' | awk '{print $2}' | sed -re 's/\\/..//g'|head -n1")

                return myIp

            finally :

                osBasedIp = subprocess.getoutput("ip a | egrep 'inet' | egrep 'brd' | awk '{print $2}' | sed -re 's/\\/..//g' | head -n1")

                if myIp != osBasedIp :
                    raise Exception("IP Non concordante")

        elif toSearch == "mask":

            mask = subprocess.getoutput("ip a | egrep \"inet\"  | head -n3 | tail -1 | awk '{print $2}'")
            return mask

        else :
            raise Exception("'ip' and 'mask' are the only parameters accepted")

    def retour(self):
        question = input("\nRevenir au menu principal ? [yes/no] \n > ")
        if question == "yes":
            self.start()

    def initializeViolet(self):
        os.system("cd ./.Violet && ./Violet.py")

    def start(self):

        os.system("clear")
        print(f"----------------- Bonjour {self.getModuleData('prenom')} -----------------\n")
        print(f"[?] Violet : Computer Status --------\n")
        if self.myIp('ip') != None :
            print(f"Network Access : YES ")
        else :
            print(f"Network Access : NO ")

        print(f"IP Address: {self.myIp('ip')}")

        try :
            open(f"/Users/{self.user}/Archetype/Tobi/Terminal/.Violet/Report.txt")
            print(f"Is Violet deployed : YES\n")
            print("Violet Report File Content: \n")
            with open(f"/Users/{self.user}/Archetype/Tobi/Terminal/.Violet/Report.txt","r") as variable:
                print(variable.read()+"\n")

        except IOError:

                print(f"Is Violet deployed : NO \n")

        print("|(1) Outils  # (2) Réseau  # (3) Internet  |\n|(4) Stockage  # (5) Serveur  # (6) Configuration  | \n|(7) Créateur  # (8) LoopSequence  # (9) Deploy Violet |\n")
        self.chooseAction()

    def login(self):
        from Library import toHash
        print("--------------- Tobias Login Page : ---------------\n")
        username = input("               Nom d'utilisateur : ")
        password = getpass.getpass("               Mot de passe : ")
        if username == self.getModuleData("prenom"):
            if toHash.HASH(password) == self.getModuleData("password"):
                self.start()
            else :
                print("WRONG PASSWORD")
                sys.exit(0)

    def creator(self):
        self.choiceList()

    def chooseAction(self):
        choice = input("----> Votre choix : ")
        if choice == "1":

            os.system("clear")
            print("[?] Tobias : Onglet Outil ----\n")
            print("----- Bloc Note (1) | Handler (2) | Raw (3) -----\n")

            answer = input("----> Votre choix : ")
            if answer == "1":
                self.blocNote()
                self.retour()

            if answer == "2":
                self.handler()
                self.retour()

            if answer == "3":
                self.raw()
                self.retour()


        if choice == "2":
            os.system("clear")
            print("[?] Tobias : Onglet Réseau ----\n")
            print("----- Page Reseau (1) | Paquet (2) \n")

            answer = input("----> Votre choix : ")
            if answer == "1":
                self.pageReseau()
                self.retour()

            if answer == "2":
                self.paquet()
                self.retour()


        if choice == "4":
            os.system("clear")
            print("[?] Tobias : Onglet Stockage ----\n")
            print("----- Coffre Fort (1) | GetFromDb (2) | Archiver\n")

            answer = input("----> Votre choix : ")
            if answer == "1":
                self.coffreFort()
                self.retour()

            if answer == "2":
                self.getFromDb()
                self.retour()

            if answer == "3":
                self.Archives()
                self.retour()


        if choice == "5":
            os.system("clear")
            print("[?] Tobias : Onglet Serveur ----\n")
            print("----- Page Serveur (1) | Transférer \n")

            answer = input("----> Votre choix : ")
            if answer == "1":
                self.pageServeur()
                self.retour()

            if answer == "2":
                self.transfert()
                self.retour()


        if choice == "7":
            os.system("clear")
            print("[?] Tobias : Onglet Créateur ----\n")
            self.creator()
            # self.start()


        elif choice == "8" :
            threadLoopSequence = threading.Thread(target=self.loopSequence())
            threadLoopSequence.start()
            self.retour()

        elif choice == "9" :
            threadViolet = threading.Thread(target=self.initializeViolet())
            threadViolet.start()
            self.retour()

    def pageServeur(self):
        pass

    def transfert(self):
        pass

    def coffreFort(self):
        pass

    def getFromDb(self):
        pass

    def Archives(self):
        pass

    def pageReseau(self):
        pass

    def paquet(self):
        pass

    def blocNote(self):
        self.notesPath = self.getPaths('noteFile','Notes')

        with open(f"{self.notesPath}","r") as variable :
            print(variable.read())

    def raw(self):
        pass

    def handler(self):
        pass

    def loopSequence(self):

        import time
        from multiprocessing import Process

        from Library.NBook import Network
        from Library.RawNetwork import Ally_Computers, internetProtocol
        from Security.Backbone import Backbone
        from Security.Riot import Security


        """ Execute every methods in order to make them properly available to the user """

        print("Launching loopSequence")


        #BackBone
        if self.getModuleData("ipScan","Backbone") == "True" :
            loopBackboneIpScan = threading.Thread(target=Backbone().innerPortScan())
            loopBackboneIpScan.start()


        if self.getModuleData("networkSpace","Backbone") == "True" :
            loopBackboneNetworkSpace = threading.Thread(target=Backbone().networkSpace())
            loopBackboneNetworkSpace.start()

        if self.getModuleData("allow/Deny access","Backbone") == "True" :
            loopBackbone = threading.Thread(target=Backbone().Etapes_de_Fonctionnement())
            loopBackbone.start()

        # Riot
        if self.getModuleData("authorized_keys","Riot") == "True" :
            loopRiot = threading.Thread(target=Security().autorized_keysCheck())
            loopRiot.start()

        # if self.getModuleData("crontabCheck","Riot") == "True" :
        #     print("starting")
        #     loopCrontab = threading.Thread(target=Security().crontabCheck())
        #     loopCrontab.start()

        if self.getModuleData("connexions","Riot") == "True" :
            loopRiot = threading.Thread(target=Security().connexion())
            loopRiot.start()

        if self.getModuleData("processus","Riot") == "True" :
            loopRiotProc = threading.Thread(target=Security().Processus())
            loopRiotProc.start()

        #RawNetwork
        #  if self.getModuleData("AllyComputer","General") == "True" :
        #     self.threads(Ally_Computers().Main())

        if self.getModuleData("Internet Protocol","General") == "True" :
            loopRaw = threading.Thread(target=internetProtocol().Main())
            loopRaw.start()

    def getModuleData(self,searchingFor,fieldName='user'):
        import json
        with open(f"{self.confs}","r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() :
                if searchingFor == keys :
                    return values

    def getPaths(self,searchingFor,fieldName='Archives'):

            with open(f"Settings/Paths/filesPaths.json","r") as variable:
                content = json.load(variable)

            for parameters in content['Paths'] :
                for keys,values in parameters[fieldName].items() :
                    if searchingFor == keys :
                        return values

#Tobias Main Task
if __name__ == "__main__":
    Tobias()
    # creatorDebug = Creator()




