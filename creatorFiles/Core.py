# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os 
import subprocess
import csv

blockDbPath ='../DATABASE/BLOCKS.csv'
featureDbPath ='../DATABASE/FEATURES.csv'

global storage 
global blocOrder 
global feature 
global commands 
global args 

storage = []
blocOrder = {} #Where we store the order by which blocs were created
blockNumber = 0
feature = {} #Where we store the features
commands = []
args = {}

class Creator(): #Main

    def __init__(self) -> None:
        print("Running...")
    
    
        # Bloc("yo","Primaire","echo $1","0","Famille")#RUNTIME
        # Bloc("lo","Primaire","echo $2","P","Famille")#RUNTIME                                                                                                                                                                                                                                                  
        
        # Storage().storeArgs(1,"hey")#RUNTIME
        # Storage().storeArgs(2,"hello")#RUNTIME

        # Storage().databaseBlockStorage("yo")#RUNTIME
        # Storage().databaseBlockStorage("lo")#RUNTIME

        # Features().addBloc("MyFunction","yo")#RUNTIME
        # Features().addBloc("MyFunction","lo")#RUNTIME
        
        # Storage().databaseFeatureStorage("MyFunction") #STORED

        # Features().incorporate("MyFunction") #RUNTIME
        
        # Storage().storeFeatureCommands() #RUNTIME

        # Execute().pattern()
    
# %%
#Class that will interact with Storage
class Storage():
    def __init__(self) -> None:
        pass
    
    def reset(self):

        global storage 
        global blocOrder 
        global feature 
        global blockNumber 
        global commands 
        global args 

        storage = []
        blocOrder = {} #Where we store the order by which blocs were created
        blockNumber = 0
        feature = {} #Where we store the features
        commands = []
        args = {}

    def Store(self,name):
        storage.append(name)
        global blockNumber 
        blockNumber +=1

    def accessStorage(self,dict,field):
        for value in blocOrder :
            if blocOrder[value] == dict :
                return storage[value][dict][field]

    def modifyStorage(self,dict,field,newData):
        for value in blocOrder :
            if blocOrder[value] == dict :
                storage[value][dict][field] = newData
    
    def accessBloc(self,bloc):
        for value in blocOrder :
            if blocOrder[value] == bloc :
               return storage[value]

    def accessFeature(self,blocs):
        for value in feature :
            if value == blocs :
                return feature[value]
    
    def storeFeatureCommands(self):
        print(feature)
        for value in feature :
            for blocks in feature[value] :
                commands.append(feature[value][blocks]["command"])
                commands.append(" ")
    
    def storeArgs(self,number,arg):
        args[number] = arg
            
    def databaseBlockStorage(self,bloc):
        
        for value in blocOrder :
            if blocOrder[value] == bloc :
                 with open(blockDbPath, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter='.')

                    filewriter.writerow(
                        [
                            bloc, 
                            storage[value][bloc]["type"], 
                            storage[value][bloc]["command"],
                            storage[value][bloc]["category"],
                            storage[value][bloc]["pattern"],
                            storage[value][bloc]["family"],
                        ]
                    
                    )

    def getBlockFromDB(self,name):
        with open(blockDbPath, 'r') as f:
            reader = csv.reader(f,delimiter='.')

            for row in reader:
                if row[0] == name:
                    return row                    

    def databaseFeatureStorage(self,element):
        arguments = []
        for i in range(1,len(args)+1):
            arguments.append(args[i])

        set = []
        for value in feature :
            if value == element :
                for blocks in feature[value] :
                    set.append(blocks)
        
        with open(featureDbPath, 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter='.',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    
                filewriter.writerow(
                            [
                                value, 
                                "&".join(set),
                                arguments

                            ]
                        )        
                    
    def getFeatureFromDB(self,name):
        with open(featureDbPath, 'r') as f:
            reader = csv.reader(f,delimiter='.')

            for row in reader:
                if row[0] == name:
                    return row                 

# %%
class Execute():
    def __init__(self) -> None:
        pass

    def execBloc(self,toExecute):
        print(subprocess.getoutput(toExecute))

    def pattern(self):
        pool = []
        index = 0
        found = 0
        argNumber = 0

        for i in range (len(commands)):
            for y in range(len(commands[i])):
                char = commands[i][y] #Commandes dans le bon ordre avant pattern
                pool.append(char)

        if pool.count("$") > 0 :
            for elements in range(len(pool)):
                
                if pool[elements] == "$":
                    try : 
                        pool[elements] = args[int(pool[elements+1])]
                    except : 
                        print("Argument non trouvé")
                        break

                    pool[elements+1] = "X"
                    print(pool)
                    argNumber +=1
                    

            for elements in range(len(pool)):
                if found == argNumber:
                    break
                else : 
                    if pool[elements] == "X":
                        print(index)
                        pool.pop(index+found)
                        found +=1
                    else : 
                        index +=1

            self.execFeatureCommand(pool)

        else : 
            self.execFeatureCommand(commands)

       
    def execFeatureCommand(self,set):
             
        list_of_strings = [str(s) for s in set]
        joined_string = "".join(list_of_strings)
        
        print(commands)
        print(set)
        # print(joined_string)
        os.system(joined_string) 
        # print(feature)

# %%
#Create and Store Blocs
class Bloc():

    def __init__(self,name,type,command,pattern,family) -> dict:

        print("Creating bloc")
        self.name = name
        self.type = type
        self.command = command
        self.pattern = pattern
        self.family = family

        self.parameters = {
            self.name :{
            "type" : self.type,
            "command" : self.command,
            "category" : "Bloc",
            "pattern" : self.pattern,
            "family" : self.family
            }
        }
        blocOrder[blockNumber] = self.name
        print(self.parameters)
        Storage().Store(self.parameters)
        print(blockNumber)
        print(blocOrder)
        print(storage)

# %%
class Features():
    def __init__(self) -> None:
        print("Creating a Feature")
        
    def addBloc(self,featureName,bloc):
        if feature : 
            feature[featureName].update(Storage().accessBloc(bloc))
        else : 
            feature[featureName] = Storage().accessBloc(bloc)
   
    def incorporate(self,featureName):
        element = Storage().getFeatureFromDB(featureName)
        content = element[1]
        content = content.split("&")
        argument = element[2]
        argument = argument.strip("[]")
        argument = argument.replace("',","")
        argument = argument.replace("'","")
        argument = argument.split()
        for y in range(len(argument)):
            Storage().storeArgs(y+1,argument[y])

        feature[featureName] = {}

        for i in range(len(content)):   
            fields = Storage().getBlockFromDB(content[i])
            Bloc(fields[0],fields[1],fields[2],fields[4],fields[5])
            feature[featureName].update(Storage().accessBloc(fields[0]))
