#!/usr/bin/env python3
#-*-coding:utf-8-*-
import hashlib
from os import name
import sys

def HASH(toHash=None):
    show = True
    if toHash != None : 
        arg = toHash
        show = False

    else : 
        arg=sys.argv[1]
        
    firstSalt="yU3#;SMn2Z9DEjyJGF`q)ZVuf7H)R[2>Hg3{E,q=Utm=vU_],ZgVv?k+?`/-"
    lastSalt=":]hW:ma~ZDL!,\YxtF(J5*[[D9N8fga38mNE$8p]B-%L8:*}D]];NG-qQb:("

    Mot_de_passe_Entré=(firstSalt+arg+lastSalt)
    Mot_de_passe_Entré=Mot_de_passe_Entré.encode()
    Mot_de_passe_chiffré = hashlib.sha1(Mot_de_passe_Entré).hexdigest()
    Mot_de_passe_chiffré=str(Mot_de_passe_chiffré)
    if show == False : 
        return Mot_de_passe_chiffré
    else : 
        print(Mot_de_passe_chiffré)

