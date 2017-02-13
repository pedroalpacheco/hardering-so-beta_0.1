# -*- coding: utf-8 -*-
#Check OS packages
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 24/01/2017
import commands
import report
import platform

def  pacotes():

    ver_version = ver_version = platform.platform(aliased=0, terse=0)
    deb = 'debian'
    see_result = deb in ver_version

    if see_result == True:
        ler_pacotes_apt = commands.getoutput('dpkg -l')
        report.relatorio('----------PACOTES INSTALADOS-----------')
        report.relatorio(ler_pacotes_apt)
        report.relatorio('---------------------')
    else:
        ler_pacotes_rpm = commands.getoutput('rpm -qa')
        report.relatorio('----------PACOTES INSTALADOS-----------')
        report.relatorio(ler_pacotes_rpm)
        report.relatorio('---------------------')
