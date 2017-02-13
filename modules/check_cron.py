# -*- coding: utf-8 -*-
#Check type OS
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 25/01/2017
#!/usr/bin/python

import report

def cronusuarios():

    import pwd, grp
    import commands

    #Search one, by user
    for p in pwd.getpwall():
        #report.relatorio p[0], grp.getgrgid(p[3])[0]
        #report.relatorio p[0]
        cat = p[0]
        busca = commands.getoutput('crontab -l -u '+cat)
        report.relatorio(' >>> Verificacao nos arquivos crontab <<< ')
        report.relatorio('Verificacao por usuario: ' + cat)
        report.relatorio(busca)
        #report.relatorio('')
        #report.relatorio('')

    #Search two, by filess
"""
    #Testado no debian
    report.relatorio('')
    report.relatorio('')
    report.relatorio('Verificacao nos arquivos crontab')
    report.relatorio('--------------------------------')
    report.relatorio('')
    busca_cron = commands.getoutput('grep -e "$pattern" /var/spool/cron/crontabs/*')
    report.relatorio(busca_cron)
"""
