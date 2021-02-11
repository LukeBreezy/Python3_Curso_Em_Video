from random import randint
from moeda import *


v = float(input('Digite o valor: R$ '))

print(f'A metade de R${v:.2f} é R${metade(v):.2f}.')

print(f'O dobro de R${v:.2f} é R${dobro(v):.2f}.')

aum = randint(1, 100)
print(f'Aumentando {aum}%, temos R${aumentar(v, aum):.2f}.')

dim = randint(1, 100)
print(f'Diminuindo {dim}% temos R${diminuir(v, dim):.2f}.')
