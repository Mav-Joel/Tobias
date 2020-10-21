#!/bin/bash

#Register my current IP
currentIp=$(ip a | egrep " inet " | egrep brd | awk '{print $2}' | sed -re "s/\/..//g" | awk '{print $1}' | head -n 1)

mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO reseau (id,Network,Information) VALUES (NULL , 'currentIp' , '$currentIp'); "
mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO reseau (id,Network,Information) VALUES (NULL , 'previousIp' , '$currentIp'); "

mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO systeme (id,Programme,Information) VALUES (NULL , 'USB' , '0'); "

main=$(ls /home/$USER | wc -l)
core=$(ls / | wc -l)

mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO systeme (id,Programme,Information) VALUES (NULL , 'nFichierR' , '$core'); "
mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO systeme (id,Programme,Information) VALUES (NULL , 'nFichierHd' , '$main'); "

mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO rapportExecution (id,Programme,Information) VALUES (NULL , 'firstStart' , 'Online'); "

mysql -u Python -p$MDP -D tobiasdb -e "INSERT INTO reseau (id,Network,Information) VALUES (NULL , 'Liaison SSH Etablie' , '0'); "

if ! [[ -f ~/otherPcTask ]] ;
then
mkdir ~/otherPcTask
fi

if ! [[ -f ~/otherPcTask/Rapport ]] ;
then
mkdir ~/otherPcTask/Rapport
fi

