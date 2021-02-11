from random import randint
from time import sleep
from operator import itemgetter

print('=-=-= SORTEANDO VALORES =-=-=')

# Sorteando os valores do dado para cada jogador
jogadores = dict()
for i in range(0, 4):
    jogadores[f'jogador {i+1}'] = randint(1, 7)
    sleep(1)
    print(f'O jogador {i+1} tirou {jogadores[f"jogador {i+1}"]}')

# Lista auxiliar para tratar o rank dos jogadores
aux = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Criando o rank dos jogadores
rank = dict()
for i in aux:
    rank[i[0]] = i[1]
# Descartando a lista auxiliar, pois não será mais necessaria
del aux

# Exibindo o rank
print('\n=-=-= RANK =-=-=')
for k, v in rank.items():
    sleep(1)
    print(f'{k}: {v}')
