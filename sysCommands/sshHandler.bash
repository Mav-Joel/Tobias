#!/bin/bash
echo """Script de contrôle de serveur Ssh""" 

getLinuxVersion=$(lsb_release -a | egrep "Manjaro")
me=$(whoami)

if [[ -z "$1" ]] ; #Vérification arguments
then    

    echo "Aucun argument"
    echo "Listes des arguments acceptés : [\" Run ; Stop ; Disable ; Enable ; Restart ; Reload ; Test \"]"

elif [[ -z "$getLinuxVersion" ]]; #Si la version de linux installée ne dispose pas du même kernel que Manjaro
then


    if [[ $1 == "Run" ]] ; #Lancer
    then

        sudo systemctl start ssh && echo " [+] Ssh Server Status : Started "

    elif [[ $1 == "Stop" ]] ; #Arrêter
    then

        sudo systemctl stop ssh && echo " [+] Ssh Server Status : Stopped"

    elif [[ $1 == "Status" ]] ; #Empécher le démarrage automatique
    then

        sudo systemctl status ssh && echo " [+] Ssh Server Auto Start Disabled "

    elif [[ $1 == "Restart" ]]; #Relancer le serveur Apache
    then

        sudo systemctl restart ssh && echo " [+] Ssh Server Status : Restarted"


    elif [[ $1 == "Test" ]]; #Tester l'ensemble de la configuration Apache et hôtes virtuels
    then

        ssh $me@127.0.0.1 && echo " [+] Ssh Server Tests : Done"
  
    fi 
    
else   

    if [ $1 == "Run" ] ; #Lancer
    then

        sudo systemctl start sshd.service && echo " [+] Ssh Server Status : Started "

    elif [ $1 == "Stop" ] ; #Arrêter
    then

        sudo systemctl stop sshd.service && echo " [+] Ssh Server Status : Stopped"

    elif [ $1 == "Disable" ] ; #Empécher le démarrage automatique
    then

        sudo systemctl disable sshd.service && echo " [+] Ssh Server Auto Start Disabled "

    elif [ $1 == "Enable" ] ; # Activer le démarrage automatique
    then 

        sudo systemctl enable sshd.service && echo " [+] Ssh Server Auto Start Enabled"
        

    elif [ $1 == "Restart" ]; #Relancer le serveur Apache
    then

        sudo systemctl restart sshd.service && echo " [+] Ssh Server Status : Restarted"


    elif [ $1 == "Test" ]; #Tester l'ensemble de la configuration Apache et hôtes virtuels
    then

        ssh $me@127.0.0.1 && echo " [+] Ssh Server Tests : Done"

    elif [ $1 == "Status" ];
    then

        sudo systemctl status sshd.service && echo " [+] Ssh Server Status"

    fi

fi