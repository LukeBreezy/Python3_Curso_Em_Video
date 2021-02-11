from random import randint      # Método utilizado para a máquina escolher um número aleatorio
print('{:~^20}'.format(' PAR OU ÍMPAR '))

vitorias = 0    # Conta quantas vezes o usuario venceu

while True:       # Enquanto o usuário estiver vencendo o jogo continua
    print('~='*15)
    player = int(input('Digite um valor: '))    # Valor a ser escolhido pelo usuário
    machine = randint(0, 11)                    # Valor a ser escolhido pela máquina
    total = player + machine                    # Soma dos valores, para determinar se é par ou ímpar

    par_impar = input('Você escolhe par ou ímpar? [P/I]: ')      # O usuário escolhe par ou ímpar
    while par_impar not in 'PpIi':      # Enquanto o usuário não escolher entre [P/I], o jogo não prossegue
        print('Valor inválido!!!')
        par_impar = input('Você escolhe par ou ímpar? [P/I]: ')  # O usuário escolhe par ou ímpar

    print(f'''Você escolheu {player} e a máquina escolheu {machine}.
O total é {total}, ''', end='')

    if total % 2 == 0:      # Caso o total seja par
        print('PAR')
        if par_impar in 'Pp':       # Caso o usuário tenha escolhido par
            print('Você Venceu!!!')
            vitorias += 1
            continue
        else:
            print('Você Perdeu!!!')
            break
    else:                   # Caso o total seja ímpar
        print('ÍMPAR')
        if par_impar in 'Ii':       # Caso o usuário tenha escolhido ímpar
            print('Você Venceu!!!')
            vitorias += 1
            continue
        else:
            print('Você Perdeu!!!')
            break

print('~=' * 20)

if vitorias == 0:
    print('Você não venceu nenhuma vez!')
elif vitorias == 1:
    print(f'Você venceu {vitorias} vez!')
else:
    print(f'Você venceu {vitorias} vezes!!!')
