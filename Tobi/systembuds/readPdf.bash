#!/bin/bash

me=$(whoami)
echo $(cat ~/Archetype/Tobi/TP2CR.txt | egrep "[0-9]:") >> /home/$me/Archetype/Tobi/TP2Questions.txt 