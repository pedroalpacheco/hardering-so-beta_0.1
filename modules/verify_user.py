# -*- coding: utf-8 -*-
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 13/02/2017
import os
import sys

def see_root():

    user = os.getegid()
    if user == 0:
        pass
    else:
        print('Não é usuario root, goodby...')
        sys.exit(0)
