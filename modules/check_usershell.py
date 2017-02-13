# -*- coding: utf-8 -*-
#Check acces to user to shell-bash
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 01/02/2017

import report

def shelluser():

    import pwd, grp
    import commands

    var_bash = 'bash'

    report.relatorio('###### Usuarios com shell ativo ######')

    for p in pwd.getpwall():
        ver_bash = (p[0] + p[0-1])
        user_bash = var_bash in ver_bash
        if user_bash == True:
            report.relatorio('---------------------')
            report.relatorio('Usuário')
            report.relatorio(p[0] + ' [Shell ativo!] ' + p[0-1])
            report.relatorio('---------------------')
        else:
            pass
