#!/usr/bin/env python3
#-*-coding:utf-8-*-
import mysql
import mysql.connector
import hashlib
import os
import json

Utilisateur=os.environ["USER"]

class Database():
    """Class that allows other programs to use all of the methods below relative to Databases"""

    def __init__(self,*args):
        self.arguments = args
        self.numberOfArguments = len(self.arguments)
        self.MagicWord = self.getModuleData("local dbpassword","Tobias")

    def getModuleData(self,searchingFor,fieldName='user'):
        self.confs = self.getPaths('path','ConfigurationJson')
        with open(self.confs,"r") as config :
            content = json.load(config)

        for parameters in content['Configurations'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values
    
    def getPaths(self,searchingFor,fieldName='Archives'):
        with open(f"/home/{Utilisateur}/Archetype/Tobi/Settings/Paths/filesPaths.json","r") as variable:
            content = json.load(variable)
        
        for parameters in content['Paths'] :
            for keys,values in parameters[fieldName].items() : 
                if searchingFor == keys :
                    return values

    def insertInDatabase(self):

        #Déterminer le nombre de colonne et de champs
        total = self.numberOfArguments - 1
        half = total//2
        otherHalf = total /2

        #Si le résultat n'est pas un chiffre rond RAISE EXECEPTION
        if half != otherHalf :
            raise Exception("BAD INPUT \nSyntax :  List[0] : Database's Name; List[1 -> n] are the columns name ; List [n -> end] the values \nNOTE : Same input as in a normal SQL Query Insert")
        else :
            columnsN = [] #Nom des colonnes
            for i in range(1,self.numberOfArguments-half):
                columnsN.append(self.arguments[i])

            columnsV = [] #Valeur des colonnes
            for i in range(self.numberOfArguments-half,self.numberOfArguments):
                if self.arguments[i] != "NULL" : #Enlever les guillements à NULL
                    columnsV.append("'"+self.arguments[i]+"'")
                else :
                    columnsV.append(self.arguments[i])


        """Insert in Database"""

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Command=mydb.cursor()
        Command.execute("USE tobiasdb")

        FirstListOfStrings = [str(s) for s in columnsV]
        NewStrings = ",".join(FirstListOfStrings)

        SecondListOfStrings = [str(s) for s in columnsN]
        NewStrings_2 = ",".join(SecondListOfStrings)


        Ins = f"INSERT INTO {self.arguments[0]} ({NewStrings_2}) VALUES ({NewStrings})"

        Command.execute(Ins)
        mydb.commit()
        mydb.close()

    def getFromDatabase(self):
        Result = []

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",
        passwd=self.MagicWord,
        )

        Dictionnary = {
            "getValue":self.arguments[1],
            "databaseName":self.arguments[0],
            "firstWhereArgument":self.arguments[2],
            "secondWhereArgument":self.arguments[3]
        }

        Command = mydb.cursor()
        Command.execute("USE tobiasdb")
        Command.execute(f"SELECT {Dictionnary['getValue']} \
                        FROM {Dictionnary['databaseName']} \
                        WHERE {Dictionnary['firstWhereArgument']}='{Dictionnary['secondWhereArgument']}'")
        
        for x in Command:
            for lettre in x :
                Result.append(lettre)
            
        return Result
        
    def updateValue(self): #Mettre à Jour une Information

        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",  
        passwd=self.MagicWord,
        )

        Dictionnary = {
            "valueColumn":self.arguments[1],
            "databaseName":self.arguments[0],
            "value":self.arguments[2],
            "firstWhereArgument":self.arguments[3],
            "secondWhereArgument":self.arguments[4]
        }
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 
        Ins=f"UPDATE {Dictionnary['databaseName']} \
            SET {Dictionnary['valueColumn']}='{Dictionnary['value']}' \
            WHERE {Dictionnary['firstWhereArgument']}='{Dictionnary['secondWhereArgument']}'"
        
        Command.execute(Ins)
        mydb.commit()

    def checkIfExists(self,lookingFor,databaseName,whereCondition,equalsTo):
        mydb = mysql.connector.connect(
        host="localhost",
        user="Python",  
        passwd=self.MagicWord,
        )
       
        Command = mydb.cursor() 
        Command.execute("USE tobiasdb") 

        Command.execute(f"SELECT {lookingFor} FROM {databaseName} WHERE {whereCondition} = '{equalsTo}'")
        
        for x in Command:
            for lettre in x :
                if lettre is None : 
                    return None 
                else : 
                    return True

#TEST BENCH
# if __name__ == "__main__":
    # a = Database().getPaths("path","Archives")
    # print(Database().checkIfExists("data","Blade","name","openPorts"))
