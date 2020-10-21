#!/bin/bash

if [[ $(lsusb | wc -l) > 4 ]];
then
  /home/joel/Archétype/Tobito/Page_Usb.py
  mysql -u Python -p$MDP -D Ressources -e "USE Ressources; "
  mysql -u Python -p$MDP -D Ressources -e "UPDATE Systeme SET Information='1' WHERE Programme='USB';"
else 
  mysql -u Python -p$MDP -D Ressources -e "USE Ressources; "
  mysql -u Python -p$MDP -D Ressources -e "UPDATE Systeme SET Information='0' WHERE Programme='USB';"
fi