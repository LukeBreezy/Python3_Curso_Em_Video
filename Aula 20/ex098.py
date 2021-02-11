# =-=-=-=  BIBLIOTECAS  =-=-=-=
from time import sleep
from random import randint


# =-=-=-=  FUNÇÕES  =-=-=-=
def linha():
    print('\033[0m=' * 50, '\033[0m')


def contador(inicio, fim, passo):
    if (inicio > fim and passo > 0) or (inicio < fim and passo < 0):
        passo *= -1
    elif passo == 0:
        passo = 1

    linha()
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}.')
    for i in range(inicio, (fim+1 if fim > inicio else fim-1), passo):
        sleep(.5)
        print(i, end=' ', flush=False)
    print('FIM.')


# =-=-=-=  MAIN  =-=-=-=
# A seguir, dois exemplos usando números aleatórios, para mostrar ao usuário como o programa funcionará
contador(inicio=randint(-100, 100), fim=randint(-100, 100), passo=randint(-20, 20))
contador(inicio=randint(-50, 50), fim=randint(-50, 50), passo=randint(-10, 10))

# A seguir, o programa funcionando com os parâmetros passados pelo usuário
linha()
print('Agora é sua vez')
contador(inicio=int(input('Inicio: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))
