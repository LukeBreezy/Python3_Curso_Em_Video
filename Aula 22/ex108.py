from random import randint
from moeda import *


v = float(input('Digite o valor: R$ '))

print(f'A metade de {moeda(v)} é {moeda(metade(v))}.')

print(f'O dobro de {moeda(v)} é {moeda(dobro(v))}.')

aum = randint(1, 100)
print(f'Aumentando {aum}%, temos {moeda(aumentar(v, aum))}.')

dim = randint(1, 100)
print(f'Diminuindo {dim}% temos {moeda(diminuir(v, dim))}.')
