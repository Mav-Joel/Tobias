#!/usr/bin/env python3
#-*-coding:utf-8-*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'joel.toula@gmail.com'
msg['To'] = 'joel.toula@gmail.com@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('joel.toula@gmail.com', 'GrpAmPMaverick1')
mailserver.sendmail('joel.toula@gmail.com', 'joel.toula@gmail.com', msg.as_string())
mailserver.quit()





