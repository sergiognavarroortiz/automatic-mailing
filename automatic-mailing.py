# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:47:04 2019

@author: Sergio Navarro
"""

# Establecemos conexion con el servidor smtp de gmail
import smtplib 
from email.mime.text import MIMEText

mailServer = smtplib.SMTP('smtp.gmail.com',587)   # substitute smtp.gmail.com for smtp.live.com in case of being an outlook email
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login("Username@gmail.com","password")
CC=['sender1@correo.com','sender2@correo.com','sender3@correo.com','sender4@correo.com']
 
 # Construimos el mensaje simple
mensaje = MIMEText("""Mail body""")
mensaje['From']="Username@gmail.com"
mensaje['To']=', '.join(CC)
mensaje['Subject']="mail subject"

# Envio del mensaje
mailServer.send_message(mensaje)
