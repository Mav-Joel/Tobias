#!/usr/bin/env python3
#-*-coding:utf-8-*-
#Propriété de Toula Joël

import RPi.GPIO as GPIO #RASPBERRY
import time

#Initialisation des ports : 

GPIO.setmode(GPIO.BCM) #Initialise les broches du raspberry en GPIO
GPIO.setup(14,GPIO.IN) #Port 14 utilisé en entrée
GPIO.setup(7,GPIO.OUT) #Port 7 utilisé en sortie

#Programmme :

while True:
    if GPIO.input(14):
        GPIO.output(7,1) # 1 correspond à la puissance de sortie
        time.sleep(3) #Ne pas oublier d'importer la Bibliotheque.NBook 
        GPIO.output(7,0) # Arrêt après 2 secondes
