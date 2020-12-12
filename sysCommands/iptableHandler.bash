#!/bin/bash

echo """Script de contrôle de iptables""" 

if [[ -z "$1" ]] ; #Vérification arguments
then    

    echo "Aucun argument n'a été trouvé"

    echo "Listes des arguments acceptés : [\" Numéro de port[*] ; Action [ACCEPT/DROP] ; Voie[INPUT/OUTPUT]\"]"

elif [[ $1 == "Save" ]]
then
    
    echo "Saving iptables"
    sudo iptables-save -f /etc/iptables/iptables.rules && echo "[+] iptables Saved "

elif [[ $1 == "Status" ]]
then 

    echo "Displaying iptables Status"
    sudo iptables -L


elif [[ $1 == "Del" ]]
then

    echo "Delete iptables lines module"

    sudo iptables -L --line-number
    
    echo "Numéro de la ligne à supprimer"
    read numLigne

    echo "OUTPUT or INPUT ?"
    read answer

    sudo iptables -D $answer $numLigne && sudo iptables -L

elif [[ $1 == "Backbone" ]]
then 

    sudo iptables -L
    echo "Bloquer le trafic en input ou output ?"
    read answer
    
    sudo iptables -A ${answer^^} -p tcp --destination-port $2 -j DROP && sudo iptables -L && echo "Updated"

else

    sudo iptables -A $3 -p tcp --destination-port $1 -j $2 && sudo iptables -L

fi

