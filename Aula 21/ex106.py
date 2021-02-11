def msg(txt, cor):
    tam = len(txt) + 4
    print('\033[1;' + str(cor) + 'm' + '=' * tam)
    print(f'{txt:^{tam}}')
    print('=' * tam, '\n\033[0m', end='')


def pyHelp():
    while True:

        msg('PyHelp - Sistema de Ajuda', 42)
        fnc = input('Função / Biblioteca > ')

        if fnc.upper() == 'FIM':
            msg('Obrigado, até logo!', 41)
            break

        msg(f"Acessando o manual do comando '{fnc}'", 44)

        from time import sleep

        for i in range(0, 159):
            print('\033[7m ', end='')
            sleep(.01)

        print('\033[7m')
        help(fnc)
        print('\033[0m', end='')


pyHelp()
