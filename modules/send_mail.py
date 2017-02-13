# -*- coding: utf-8 -*-
#Send mail with report
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 02/01/2017
import platform
import os
from ConfigParser import SafeConfigParser

ver_hostname = platform.node()

# reads file the configuration ====================
parser = SafeConfigParser()
parser.read('config.ini')

enviaemail = parser.get("informacoes", "destiny")
remetente = parser.get('informacoes', 'sender')
senha = parser.get('informacoes', 'pass')
smtp = parser.get('informacoes', 'srvsmtp')
porta = parser.get('informacoes', 'port')
ptp = int(porta)

def mail():

    import smtplib

    to = enviaemail
    gmail_user = remetente
    gmail_pwd = senha
    smtpserver = smtplib.SMTP(smtp,ptp)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Relatorio Hardering OS - Hostname: ' + ver_hostname
    read_file = open('Report-Hardering.txt', 'rb')
    msg = (header + read_file.read())
    read_file.close()
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
    os.remove('Report-Hardering.txt')
