#!/bin/bash
#Propriété de Toula Joël

#Informations Basiques
echo "Contenu : "
a=$(cat $1 | wc -l); 

	i=0
until (( i == $a )); do

	cat $1 | head -n$(($i+1)) |tail -n +$(($i+1)) | sed "s/^/$(($i+1)) /g"
	i=$(($i+1))

done

echo "Taille : $(cat $1 |du -h $1)"
echo "Nombre de lignes : $a"
#Informations Droits
echo "Droits : $(ls -l $1)";

#Codage
b=$(cat $1 | egrep "python")
c=$(cat $1 | egrep "bash")
d=$(cat $1 | egrep "python3")

if [[ $b == "#!/usr/bin/env python" ]] ; then 
	echo "Ce fichier est un script python"
fi

if [[ $c == "#!/bin/bash" ]] ; then 
        echo "Ce fichier est un script Bash"
fi

if [[ $b == "#!/usr/bin/env python3" ]] ; then 
        echo "Ce fichier est un script python3"
fi


