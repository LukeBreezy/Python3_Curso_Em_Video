from random import randint
from time import sleep

jogos = []
qtde = int(input('Quantos palítes você quer gerar? '))

for i in range(qtde):
    jogos.append([])
    for j in range(6):
        aux = randint(1, 60)
        while aux in jogos[i]:
            aux = randint(1, 60)
        jogos[i].append(aux)

print('\n'+'=-='*3, f'Sorteando {qtde} jogos', '=-='*3)
sleep(1)
for i in range(qtde):
    sleep(.4)
    print(f'Jogo {i+1}: {jogos[i]}')
