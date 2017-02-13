# -*- coding: utf-8 -*-
#Check ssh parameters
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 25/01/2017
import commands
import re
import report

def infossh():

    par_um = 'PermitRootLogin no'
    par_port = '0.0.0.0:22'

    ler_ssh = commands.getoutput('cat /etc/ssh/sshd_config')
    #report.relatorio(ler_ssh)


    ler_portssh = commands.getoutput('netstat -tulpn')

    reum = par_um in ler_ssh
    ressh = par_port in ler_portssh
    #report.relatorio(reum)

    if reum == False :
        report.relatorio('----------- Verifica SSH PermitRootLogin ----------')
        report.relatorio('Não existe >>PermitRootLogin no<<')
        report.relatorio('---------------------')
    else:
        report.relatorio('----------- Verifica SSH PermitRootLogin ----------')
        report.relatorio('>>PermitRootLogin no EXISTE!<< necessário verificar se está habilitado!')
        report.relatorio('---------------------')

    if ressh == False:
        report.relatorio('----------- Verifica porta SSH ----------')
        report.relatorio('SSH nao esta na porta padrao!')
        report.relatorio('---------------------')
    else:
        report.relatorio('----------- Verifica porta SSH ----------')
        report.relatorio('Problema, ssh esta na porta 22!')
        report.relatorio('---------------------')
