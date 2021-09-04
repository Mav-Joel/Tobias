#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import getpass
import sys
import csv
import time
from Core import Storage
from Core import Features
from Core import Bloc
from Core import Execute

class GraphicalUserInterface():

    def __init__(self) -> None:
        
        self.blockList = []
        self.goodWords = []
        self.blockDisplayed = []
        self.blockDbPath ='../DATABASE/BLOCKS.csv'
        self.featureDbPath ='../DATABASE/FEATURES.csv'

        self.login()
    
        os.system("clear")
        print(f"----------------- Bonjour Joel -----------------\n")
        print(f"[?] Computer Status --------\n")
        # if self.myIp('ip') != None :
        #     print(f"Network Access : YES ")
        # else :
        #     print(f"Network Access : NO ")

        # print(f"IP Address: {self.myIp('ip')}")

        # try :
        #     open(f"/Users/{self.user}/Archetype/Tobi/Terminal/.Violet/Report.txt")
        #     print(f"Is Violet deployed : YES\n")
        #     print("Violet Report File Content: \n")
        #     with open(f"/Users/{self.user}/Archetype/Tobi/Terminal/.Violet/Report.txt","r") as variable:
        #         print(variable.read()+"\n")

        # except IOError:

        #         print(f"Is Violet deployed : NO \n")

        # print("|(1) Outils  # (2) Réseau  # (3) Internet  |\n|(4) Stockage  # (5) Serveur  # (6) Configuration  | \n|(7) Créateur  # (8) LoopSequence  # (9) Deploy Violet |\n")
        # self.chooseAction()

    def login(self):
        os.system("clear")
        print("--------------- Tobias Login Page : ---------------\n")
        username = input("               Nom d'utilisateur : ")
        password = getpass.getpass("               Mot de passe : ")
        if username != "Joel" or password != "Joel":
                print("WRONG")
                sys.exit(0)

    def showBlocksFromDB(self):
        with open(self.blockDbPath, 'r') as f:
            reader = csv.reader(f,delimiter='.')

            for row in reader:
                if row != None : 
                    print("|"+row[0]+" : "+row[2]+"|")

    def getFeaturesFromDB(self):
        with open(self.featureDbPath, 'r') as f:
            reader = csv.reader(f,delimiter='.')

            for row in reader:
                print("|"+row[0]+"|")

    def choiceList(self):
        os.system("clear")
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
        
        for element in range(eachChoices.__len__()): #Fetch choices
            
            print(f"({element+1}) {eachChoices[element]}",end = " \n") #Display the menu
        
        print("\n")
        print("[!] Available Blocks -------\n")
        self.showBlocksFromDB()

        print("\n")
        print("[!] Available Features -------\n")
        self.getFeaturesFromDB()
        
        print("\n")

        answer = input("----> Votre choix : ")

        options = 0
        for keys,values in execute.items() : # If the answer is correct, check what the answer does
            if answer is keys :
                exec(values)
            else : 
                options +=1 
                if options == len(execute):
                    self.feature(answer)

    def createBloc(self):

        os.system("clear")

        self.nom = input("Nom du bloc : ")
        self.category = input("Catégorie du bloc [ Primaire | Secondaire | Script | multipleInput ]: ")
        self.command = input("Commande à Éxecuter: \n > ")
        
        if self.category != "Primaire":
            self.pattern = input("Emplacement dans le pattern: \n > ")
        else :
            self.pattern = 0

        with open(self.blockDbPath, 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='.')
            filewriter.writerow(
                [
                    self.nom, 
                    self.category, 
                    self.command,
                    "Bloc",
                    self.pattern,
                    "Famille"
                ]
            
            )

        print("Bloc créer avec succès")
        time.sleep(1)
        self.choiceList()

    def getBlocksFromDB(self):
        with open(self.blockDbPath, 'r') as f:
            reader = csv.reader(f,delimiter='.')

            for row in reader:
                if row != None : 
                    self.blockDisplayed.append(row[0])

    def createFeature(self):
        os.system("clear")
        self.blockDisplayed = []
        self.showBlocksFromDB()
        self.getBlocksFromDB()
        print(f"Vos blocs sélectionnés : {self.blockList}")
        print("_______________________________________________________________")
        nextAction = input("\n(1) Créer une fonctionnalité avec les blocs actuelles   \n(2) Supprimer un bloc de la pioche  \n(3) Retour \n----> Votre choix : ")
        
        if nextAction == "1":
            if len(self.blockList) != 0:
                os.system("clear")
                foncName = input("Nom de la fonctionnalité ? \n : ")
                item = 0
                for elements in self.blockList:
                    fields = Storage().getBlockFromDB(elements)
                    if fields[1] == "Secondaire":
                        Bloc(fields[0],fields[1],fields[2],fields[4],fields[5])
                        Storage().storeArgs(item,fields[2])
                    else : 
                        Bloc(fields[0],fields[1],fields[2],fields[4],fields[5])
                        Features().addBloc(foncName,elements)
                    item +=1

                Storage().databaseFeatureStorage(foncName) #STORED
                os.system("clear")
                self.choiceList()

            else :
                print("[!] Votre pioche est vide...")
                time.sleep(0.5)
                self.createFeature()
        
        elif nextAction == "2":
            if len(self.blockList) != 0:
                if len(self.blockList) == 1 : 
                    self.blockList.remove(self.blockList[0])
                    self.createFeature()
                
                name = input("Nom du bloc à retirer \n : ")
                
                if len(self.blockList) >1 : 
                    self.blockList.remove(name)
                    self.createFeature()
            else :
                print("[!] Votre pioche est vide...")
                time.sleep(0.5)
                self.createFeature()

        elif nextAction == "3":
            self.choiceList()
        
        else : 
            for i in range(len(self.blockDisplayed)):
                if nextAction == self.blockDisplayed[i]:
                    self.blockList.append(nextAction)
                    self.createFeature()
                else :
                    if self.blockDisplayed[i].count(nextAction) > 0:
                        self.goodWords.append(self.blockDisplayed[i])

            if len(self.goodWords) == 0:
                print("Votre bloc n'existe pas")
                time.sleep(0.5)
                self.createFeature()
            else: 

                for i in range(len(self.goodWords)):
                    print(f"Bloc correspondant à la description {self.goodWords[i]}\n ------")
                
                answer = input("Lequel est ce ? [nom/NO] \n ----> Votre choix : ")
                self.blockList.append(answer)
                self.goodWords = []
                self.createFeature()

    def feature(self,name="placeholder"):
        os.system("clear")
        print("[!] Available Features -------\n")
        if name is None :
            self.getFeaturesFromDB()
            name = input("Nom de la fonctionnalité à lancer\n ----> Votre choix : ")
            
        Features().incorporate(name) #RUNTIME
        
        Storage().storeFeatureCommands() #RUNTIME

        Execute().pattern()
        action = input("Appuyer sur une touche pour continuer")
        Storage().reset()

        self.choiceList()
    
if __name__ == "__main__":
    GraphicalUserInterface().choiceList()