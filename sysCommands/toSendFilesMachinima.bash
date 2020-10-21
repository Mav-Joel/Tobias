#!/bin/bash

#Script d'upload du fichier du Blade vers Machinima


scp $1 serv001@92.142.47.33:/home/joel/ || echo "Machinima Inaccessible"


