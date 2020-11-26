#!/usr/bin/env python3
#-*-coding:utf-8-*-


import notify2
notify2.init("test")
n = notify2.Notification("heyo",message="hey ")
n.show()
# from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql
# import mysql.connector
# import os
# import functools
# import time
# import hashlib
# import sys
# import subprocess
# import json
# import pandas 
# from Bibliotheque.DBook import Database

# def timer(func):
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         tic = time.perf_counter()
#         value = func(*args, **kwargs)
#         tac = time.perf_counter()
#         elapsed_time = tac - tic
#         print(f"Elapsed time: {elapsed_time:0.10f} seconds for : {func}")
#         return value
#     return wrapper_timer

# def sheets():
#     data = {
#             'Nom': ['Orange', 'Sfr', 'Free', 'Bouygues', 'Maxis', 'BT',
#             'Vodafone','Comcast','T ou Deutsche Telekom','At&t','Level3',
#             'Verizon','TATA Com','TeliaSonera'],
#             'Siege': ['France', 'France', 'France', 'France',
#                     'Malaisie', 'Royaume-Uni', 'Angleterre','USA',
#                     'Allemagne','USA','USA','USA','N/A','Suède'],
#         'Chiffre d_Affaire': ['42,2 milliard' , '8,5 milliard', '2,9 milliard',
#         '5.5 milliard', 'N/A', '23 459 millions', '45 066 millions','108 942 millions',
#         '75 656 millions','163,8 milliards','3,378 milliards','130 863 millions',
#         'N/A','83 559 millions'],
#     }
#     row_labels = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14]
#     df = pandas.DataFrame(data=data, index=row_labels)
#     print(df)
