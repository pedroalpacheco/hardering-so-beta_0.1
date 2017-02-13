# -*- coding: utf-8 -*-
#Check user status
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 31/01/2017

import report

def informacoesuser():

    import pwd, grp
    import commands

    #Search one, by user
    report.relatorio('###########INFORMACOES DO USUSARIO##########')
    for p in pwd.getpwall():
        usu = p[0]
        verifica = commands.getoutput('chage -l '+usu)
        report.relatorio('Informação por usuario: ' + usu)
        report.relatorio('---------------------')
        report.relatorio(verifica)
        report.relatorio('---------------------')
