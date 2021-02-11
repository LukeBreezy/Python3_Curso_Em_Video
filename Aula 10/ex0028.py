from random import randint
from time import sleep

randnum = int(randint(0, 5))

print('A máquina escolheu um número entre 0 e 5.\nTente adivinhar qual foi!')

usernum = int(input('Digite um número inteiro: '))
print('Processando...')
sleep(2.5)
if usernum == randnum:
    print('Parabens, voce acertou!!!')
else:
    print('Voce fracassou, a máquina escolheu o número {}\nA máquina venceu!!!'.format(randnum))
