from random import randint
from dados import resumo

v = float(input('Digite um valor: R$ '))

aum = randint(1, 100)
dim = randint(1, 100)

resumo(v, aum, dim)
