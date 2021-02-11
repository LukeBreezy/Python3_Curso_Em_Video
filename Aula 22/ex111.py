from uteisCeV.dados import resumo

from random import randint

v = float(input('Digite um valor: R$ '))

aum = randint(1, 100)
dim = randint(1, 100)

resumo(v, aum, dim)
