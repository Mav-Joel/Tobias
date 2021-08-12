#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys
sys.path.insert(1,"/Users/joel/Archetype/Tobi/")
sys.path.insert(1,"/Users/joel/Archetype/Tobi/Library")
from Library.TBook import Tools
      
Tools().Notification("Transfer ongoing")
Utilisateur=os.environ["USER"]
Tools().getModuleData()
# #Envoi du fichier de contrôle / Envoi du programme dans le fichier de contrôle
os.system("scp -r /Users/{}/Archetype/Tobito/Multi_Task_Pcs {}:~/".format(Utilisateur,Pc)) 

# os.system("scp {} {}:/Users/{}/Multi_Task_Pcs ".format(Programme,Pc,Utilisateur))

# # Executer le programme
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect(Ip,port=22 ,username='joel',password="GrpAmPMaverick&")
# stdin,stdout,stderr=ssh.exec_command("chmod u+x ~/Multi_Task_Pcs/* | ~/Multi_Task_Pcs/* >> ~/Multi_Task_Pcs/Rapport/Result")
# output= stdout.readlines()
# print( "\n".join(output))

# os.system("scp {}:~/Multi_Task_Pcs/Rapport/Result /Users/{}/Archetype/Tobito/Multi_Task_Pcs/Rapport ".format(Pc,Utilisateur))
