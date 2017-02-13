# -*- coding: utf-8 -*-
#Check if user uid root
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 31/01/2017
import report

def useruid():

    import commands

    ver_uid = commands.getoutput('awk -F: \'($3 == "0") {print}\' /etc/passwd')
    report.relatorio('=== Usuario com uid root: ===')
    report.relatorio(ver_uid)
    report.relatorio('==============================')
