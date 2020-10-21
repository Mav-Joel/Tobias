#!/bin/bash

echo """Script de contrôle de serveur Apache""" 

getLinuxVersion=$(lsb_release -a | egrep "Manjaro")

if [[ -z "$1" ]] ; #Vérification arguments
then    

    echo "Aucun argument"
    echo "Listes des arguments acceptés : [\" Run ; Stop ; Disable ; Enable ; Restart ; Reload ; Test \"]"

elif [[ -z "$getLinuxVersion" ]]; #Si la version de linux installée ne dispose pas du même kernel que Manjaro
then


    if [[ $1 == "Run" ]] ; #Lancer
    then

        sudo systemctl start apache2 && echo " [+] Web Server Status : Started "

    elif [[ $1 == "Stop" ]] ; #Arrêter
    then

        sudo systemctl stop apache2 && echo " [+] Web Server Status : Stopped"


    elif [[ $1 == "Disable" ]] ; #Empécher le démarrage automatique
    then

        sudo systemctl disable apache2 && echo " [+] Web Server Auto Start Disabled "

    elif [[ $1 == "Enable" ]] ; # Activer le démarrage automatique
    then 

        sudo systemctl enable apache2 && echo " [+] Web Server Auto Start Enabled"
        

    elif [[ $1 == "Restart" ]]; #Relancer le serveur Apache
    then

        sudo systemctl restart apache2 && echo " [+] Web Server Status : Restarted"


    elif [[ $1 == "Reload" ]]; #Recharger les fichiers de configurations
    then

        sudo systemctl reload apache2 " [+] Web Server Status : Config files updated"


    elif [[ $1 == "Test" ]]; #Tester l'ensemble de la configuration Apache et hôtes virtuels
    then

        sudo apache2ctl -t && sudo apache2ctl -t -D DUMP_VHOSTS && echo " [+] Web Server Tests : Done"
  
    fi 
    
else   

    if [ $1 == "Run" ] ; #Lancer
    then

        sudo systemctl start httpd && echo " [+] Web Server Status : Started "

    elif [ $1 == "Stop" ] ; #Arrêter
    then

        sudo systemctl stop httpd && echo " [+] Web Server Status : Stopped"

    elif [ $1 == "Disable" ] ; #Empécher le démarrage automatique
    then

        sudo systemctl disable httpd && echo " [+] Web Server Auto Start Disabled "

    elif [ $1 == "Enable" ] ; # Activer le démarrage automatique
    then 

        sudo systemctl enable httpd && echo " [+] Web Server Auto Start Enabled"
        

    elif [ $1 == "Restart" ]; #Relancer le serveur Apache
    then

        sudo systemctl restart httpd && echo " [+] Web Server Status : Restarted"


    elif [ $1 == "Reload" ]; #Recharger les fichiers de configurations
    then

        sudo systemctl reload httpd && echo " [+] Web Server Status : Config files updated"


    elif [ $1 == "Test" ]; #Tester l'ensemble de la configuration Apache et hôtes virtuels
    then

        sudo httpd -t && sudo httpd -t -D DUMP_VHOSTS && echo " [+] Web Server Tests : Done"

    elif [ $1 == "Status" ];
    then

        sudo systemctl status httpd

    fi

fi