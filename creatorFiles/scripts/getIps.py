#!/usr/bin/env python3
#-*-coding:utf-8-*-
import nmap
import sys

sys.path.insert(1,"/Users/joel/Archetype/Tobi")
from Library.NBook import Network


nm = nmap.PortScanner()
nm.scan(hosts=Network().myIp("mask"), arguments='-n -sP -PE -PA21,23,80,3389') #Nouveau arguments
hosts_list = nm.all_hosts()
a = ["192.168.1.31"]
print(a) 

