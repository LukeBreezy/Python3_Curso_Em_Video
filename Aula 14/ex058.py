from random import randint

maq = randint(1, 10)    # Definindo o número escolhido pela máquina
num = jogadas = 0       # Declarando as variáveis que receberam o número digitado e a quantidade de jogadas

print('''\033[1;33mA máquina escolheu um número entre 1 e 10.
Tente adivinhar!!!\033[0m\n''')

while num != maq:       # Enquanto o aux não adivinhar o número qua a máquina escolheu, o jogo não acaba
    num = int(input('Digite um número: '))
    jogadas += 1        # Adicionando 1 na quantidade de jogadas
    if num != maq:
        print('Errou, tente'
              ' novamente!\n')
    else:
        print('\033[1;34mParabens, você acertou!!!\n\033[0m'
              'Foram necessárias {} jogadas para você acertar.'.format(jogadas))
