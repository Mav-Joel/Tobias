#!/usr/bin/env python3
#-*-coding:utf-8-*-
import smtplib, ssl
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
senderEmail = "joel.toula@gmail.com"

for i in range(0,sys.argv):
    receiverEmail = i
    message = MIMEMultipart("alternative")
    message["Subject"] = "ModeCreateur"
    message["From"] = senderEmail
    message["To"] = receiverEmail

    text = sys.argv[2]
    html = text


    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    port = 465  # For SSL
    password = "GrpAmPMaverick1"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail, receiverEmail, message.as_string())