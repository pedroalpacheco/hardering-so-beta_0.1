# -*- coding: utf-8 -*-
#Check user history
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 24/01/2017

import report

def historicouser():
    import commands
    lista_home = commands.getoutput('grep -e "$pattern" /home/*/.bash_history')
    report.relatorio('---------------------')
    report.relatorio('Historico de comando de usuarios')
    report.relatorio('---------------------')
    report.relatorio(lista_home)
    report.relatorio('---------->FIM<-----------')
