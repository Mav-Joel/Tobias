#!/bin/bash

#Script d'upload du fichier du Blade vers Machinima

me=$(whoami)
scp $1 serv001@92.142.47.33:/home/$me/ || echo "Machinima Inaccessible"


