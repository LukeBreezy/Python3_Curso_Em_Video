from emoji import emojize
from random import randint
from time import sleep
print(emojize('Pedra :fist: Papel :raised_hand: Tesoura :v:', use_aliases=True))

jokenpo = [emojize(':fist:', use_aliases=True),         #Pedra
           emojize(':raised_hand:', use_aliases=True),  #Papel
           emojize(':v:', use_aliases=True)]            #Tesoura

IA = randint(0, 2)
jogador = int(input(emojize('''
A máquina fez uma jogada, faça a sua!
1 - Pedra :fist:
2 - Papel :raised_hand:
3 - Tesoura :v:
\n''', use_aliases=True)))-1

sleep(.7)
print('JO')
sleep(.7)
print('KEN')
sleep(.7)
print('PO!\n')

print('Jogador {} x {} IA'.format(jokenpo[jogador], jokenpo[IA]))
if (jogador == 2 and IA == 1) or (jogador == 1 and IA == 0) or (jogador == 0 and IA == 2):
    print('Parabéns, você venceu!!!')
elif (IA == 2 and jogador == 1) or (IA == 1 and jogador == 0) or (IA == 0 and jogador == 2):
    print('Se fudeu, a máquina venceu!!!')
elif jogador == IA:
    print('Empate')



