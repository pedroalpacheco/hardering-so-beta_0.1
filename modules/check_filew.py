# -*- coding: utf-8 -*-
#Check files from write stick bits
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 31/01/2017

import report

def arquivosescrita():
    import commands

    varredura = commands.getoutput('find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \)')
    #No files
    if varredura == '':
        report.relatorio('---------------------')
        report.relatorio ('Não ha arquivos com escrita:')
        report.relatorio(varredura)
        report.relatorio('---------------------')
    else:
        #Has files
        report.relatorio('---------------------')
        report.relatorio('Arquivos com escrita:')
        report.relatorio('---------------------')
        report.relatorio(varredura)
        report.relatorio('---------------------')


#verifica_var = if not varredura;




#report.relatorio(varredura)
