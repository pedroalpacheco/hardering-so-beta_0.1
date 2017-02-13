# -*- coding: utf-8 -*-
#Check if files and directories not pas owner
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 01/02/2017
import report

def nouser():
    import commands

    varredura_no = commands.getoutput('find / -xdev \( -nouser -o -nogroup \)')

    #No files
    if varredura_no == '':
        report.relatorio('---------------------')
        report.relatorio ('Todos os arquivos possuem dono!')
        report.relatorio(varredura_no)
        report.relatorio('---------------------')
    else:
        #Has files
        report.relatorio('---------------------')
        report.relatorio('Arquivos e diretorios sem donos:')
        report.relatorio('---------------------')
        report.relatorio(varredura_no)
        report.relatorio('---------------------')
