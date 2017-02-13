# -*- coding: utf-8 -*-
#Check type OS
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 24/01/2017
#07/02/2016 - Create function
import commands
import report

def verifport():
    ver_ports = commands.getoutput('netstat -tulpn')
    report.relatorio(' >>> Verifica portas <<< ')
    report.relatorio('\n' + ver_ports)
