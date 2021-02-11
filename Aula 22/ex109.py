from random import randint
from moeda import *


v = float(input('Digite o valor: R$ '))

print(f'A metade de {moeda(v)} é {metade(v, False)}.')

print(f'O dobro de {moeda(v)} é {dobro(v)}.')

aum = randint(1, 100)
print(f'Aumentando {aum}%, temos {aumentar(v, aum, True)}.')

dim = randint(1, 100)
print(f'Diminuindo {dim}% temos {diminuir(v, dim, False)}.')
