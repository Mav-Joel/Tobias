#!/bin/bash

#Register my current IP
currentIp=$(ip a | egrep " inet " | egrep brd | awk '{print $2}' | sed -re "s/\/..//g" | awk '{print $1}' | head -n 1)
currentPc=$(hostname)
me=$(whoami)

mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO reseau (id,Network,Programme,Nature,Information) VALUES (NULL , '$currentIp' , 'network.bash', 'currentIp','$currentIp'); "
mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO reseau (id,Network,Programme,Nature,Information) VALUES (NULL , '$currentIp' , 'network.bash', 'previousIp','$currentIp'); "

mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO $currentPc(id,name,field,data) VALUES (NULL , 'USB' ,'Hardware','0'); "

main=$(ls /home/$me | wc -l)
core=$(ls / | wc -l)

mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO $currentPc (id,name,field,data) VALUES (NULL , 'nFichierR' , 'Riot', '$core'); "
mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO $currentPc (id,name,field,data) VALUES (NULL , 'nFichierHd' ,  'Riot', '$main'); "

mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO rapportExecution (id,Programme,Information) VALUES (NULL , 'firstStart' , 'Online'); "

mysql -uroot -P 8889 -D tobiasdb -e "INSERT INTO reseau (id,Network,Programme,Nature,Information) VALUES (NULL , '$currentIp' , 'network.bash', 'Liaison SSH Etablie' , '0'); "



