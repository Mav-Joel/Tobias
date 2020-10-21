#!/bin/bash

#Script d'upload du fichier "Machinima" du Blade vers Machinima

if [[ -z "$1" ]];
then 

    scp -r /home/joel/Archétype/Machinima/* serv001@92.142.47.33:/var/www/html/ && echo "[+] Done" #Emplacement par défaut

else 

    scp -r $1 serv001@92.142.47.33:/var/www/html && echo "Done" # Si argument , emplacement changeable 

fi
