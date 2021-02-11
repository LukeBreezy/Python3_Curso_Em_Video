# =-=-=-=  BIBLIOTECAS  =-=-=-=
from random import randint
from time import sleep


# =-=-=-= FUNÇÕES  =-=-=-=
# Sorteia 5 números e coloca em uma lista
def sorteio(lst):
    print('Sorteando os valores da lista: ', end='')
    for i in range(5):
        lst.append(randint(1, 10))
        print(lst[i], end=' ')
        sleep(.5)
    print('FIM.')


# Soma apenas os valores pares da lista sorteada
def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lst}, temos {soma}')


# =-=-=-=  MAIN  =-=-=-=
nums = []
sorteio(nums)
somaPar(nums)
