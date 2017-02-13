# -*- coding: utf-8 -*-
#Check if ipv6 is active
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 31/01/2017
import report

def veripv6():

    import commands

    ler_ipv = commands.getoutput('ifconfig | grep inet6')
    protocolo = 'inet6'

    result_ipv = protocolo in ler_ipv

    if result_ipv == True:
        report.relatorio('##### Verifica IPV6 #####')
        report.relatorio('---------------------')
        report.relatorio('Ipv6 Habilitado!')
        report.relatorio('---------------------')
    else:
        report.relatorio('##### Verifica IPV6 #####')
        report.relatorio('---------------------')
        report.relatorio('Ipv6 Desabilitado!')
        report.relatorio('---------------------')
