# -*- coding: utf-8 -*-
#Check type OS
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 24/01/2017
#Melhorar verificação de sistema operacional
import commands
import report
import platform

def so():

    #ver_version = commands.getoutput('uname -a')
    #ver_version = platform.uname()
    ver_version = platform.platform(aliased=0, terse=0)
    ver_hostname = platform.node()
    deb = 'debian'
    see_result = deb in ver_version

    if see_result == True:
        version_debian = commands.getoutput('lsb_release -a')
        report.relatorio('----------INFO SO-----------')
        report.relatorio('Hostname: ' + ver_hostname)
        report.relatorio(version_debian)
        report.relatorio('---------------------')
    else:
        version_rhn = commands.getoutput('cat /etc/*-release')
        report.relatorio('----------INFO SO-----------')
        report.relatorio(version_rhn)
        report.relatorio('---------------------')
