#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël
import os
import subprocess
import nmap
import socket
from ipaddress import IPv4Interface

#CUSTOM IMPORTS
from Bibliotheque.TBook import Tools
from Bibliotheque.DBook import Database


"""Variables d'environnement"""

user = os.environ["USER"]
currentPc=subprocess.getoutput("hostname")


class Network():
   
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
                    print(myIp)
                    print(osBasedIp)
                    raise Exception("IP Non concordante")

        elif toSearch == "mask":
            
            mask = subprocess.getoutput("ip a | egrep \"inet\"  | head -n3 | tail -1 | awk '{print $2}'")
            return mask
    
        else : 
            raise Exception("'ip' and 'mask' are the only parameters accepted")

    def ipScan(self,ip):
       
        ifc = IPv4Interface(self.myIp("mask"))
        Tools().MsgSystem("IP Scan Ongoing","...")
        
        nm = nmap.PortScanner()
        nm.scan(ip, '1-1024')
        for host in nm.all_hosts(): #HÔTES SUR LE RESEAU
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","ipScan","---------------------").insertInDatabase()
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","ipScan",f"{host} : {nm[host].hostname()}").insertInDatabase()
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","ipScan",f"State : {nm[host].state()}").insertInDatabase()
            for proto in nm[host].all_protocols():
                Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","ipScan",f"Protocol : {proto}").insertInDatabase()

                lport = nm[host][proto].keys()
                for port in lport:
                    Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","ipScan",f"Port | State : {port} {nm[host][proto][port]['state']}").insertInDatabase()
                
        Tools().MsgSystem("IP Scan Done","+")

    def networkScan(self,ip):
        ifc = IPv4Interface(self.myIp("mask"))
        Tools().MsgSystem("Network IP Scan Ongoing","...")
      
        nm = nmap.PortScanner()
        nm.scan(hosts=ip+'/24', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan",f"{host} : {status}").insertInDatabase()
            nm.scan(host, '1-1024')
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan","-----------------------------").insertInDatabase()
            Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan",f"{host} : {nm[host].hostname()}").insertInDatabase()
            for proto in nm[host].all_protocols():
                Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan","-----------------------------").insertInDatabase()
                Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan",f"Port : {proto}").insertInDatabase()

                lport = nm[host][proto].keys()
                for port in lport:
                    Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","NetworkIpScan",f"Port | State {port} | {nm[host][proto][port]['state']}").insertInDatabase()

        Tools().MsgSystem("The Network IP Scan is Done","+")

    def currentNH(self,ip):
        ifc = IPv4Interface(self.myIp("mask"))
        Tools().MsgSystem("IP Scan Ongoing","...")

        nm = nmap.PortScanner()
        nm.scan(hosts=ip+'/24', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = nm.all_hosts()
        for lettre in hosts_list :
           
            if lettre == self.myIp("ip"):
                Database("knownIps","id","hostname","address","NULL",f"{currentPc}",f"{lettre}").insertInDatabase()
            else : 
           
                print("L'adresse ip : "+lettre+" a été identifié sur votre réseau actuel")
                answer=input("Connaissez vous cette adresse ip ? [yes/no] \n> ")
            
                if answer == "yes":
                    name=input("Nommez là \n> ")
                    Database("knownIps","id","hostname","address","NULL",f"{name}",f"{lettre}").insertInDatabase()
                    Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","Online",f"{lettre}").insertInDatabase()

                elif answer == "no" :
                    Database("unknownIps","id","address","NULL",f"{lettre}").insertInDatabase()
                    
                
                else :
                    print("Wrong answer")

        
        hosts_list = str(hosts_list)
        hosts_list = hosts_list.strip("[]")
        hosts_list = hosts_list.replace("',","")
        hosts_list = hosts_list.replace("'","")
        Database("reseau","id","Network","Programme","Nature","Information","NULL",f"Network : {ifc.network}","NBook","currentNetworkHosts",f"{hosts_list}").insertInDatabase()
        Tools().MsgSystem("Current host list recovered","+")


#TEST BENCH
# if __name__ == "__main__":
    # pass   
