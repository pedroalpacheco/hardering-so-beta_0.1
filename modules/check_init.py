# -*- coding: utf-8 -*-
#Verify the startup of the OS
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 24/01/2017
import report
import platform

def inicializacao():

    import commands

    ver_version = ver_version = platform.platform(aliased=0, terse=0)
    deb = 'debian'
    see_result = deb in ver_version

    if see_result == True:
        ler_ini_deb = commands.getoutput('service --status-all')
        report.relatorio('######## INICIALIZACAO DO SO ########')
        report.relatorio(ler_ini_deb)
        report.relatorio('---------------------')
    else:
        ler_ini_redh = commands.getoutput('systemctl list-unit-files --type=service')
        report.relatorio('######## INICIALIZACAO DO SO ########')
        report.relatorio(ler_ini_redh)
        report.relatorio('---------------------')
