# -*- coding: utf-8 -*-
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 13/02/2017
import os.path
import os

def see_file():
    "Verify if report file exist"

    relat_file = os.path.isfile('Report-Hardering.txt')

    if relat_file == True:
        os.remove('Report-Hardering.txt')
    else:
        pass
        
