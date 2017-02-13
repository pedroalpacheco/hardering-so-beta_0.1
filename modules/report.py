# -*- coding: utf-8 -*-
#Class report
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 06/02/2017
def relatorio(dados):
    arquivo = open('Report-Hardering.txt', 'a+')
    #arquivo.write('\n_____________________________________')
    arquivo.write('\n')
    arquivo.write(dados)
    #arquivo.write('\n_____________________________________')
    #arquivo.write('\n------ Fim -----')
    arquivo.write('\n')
    arquivo.close()
