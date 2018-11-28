# -*- coding: utf-8 -*-
codigo, quant = input().split()
codigo = int(codigo)
quant = int(quant)
if codigo == 1:
    total = (quant*4.0)
    print('Total: R$ %.2f' %total)
if codigo == 2:
    total = (quant*4.5)
    print('Total: R$ %.2f' %total)
if codigo == 3:
    total = (quant*5.0)
    print('Total: R$ %.2f' %total)
if codigo == 4:
    total = (quant*2.0)
    print('Total: R$ %.2f' %total)
if codigo == 5:
    total = (quant*1.5)
    print('Total: R$ %.2f' %total)
