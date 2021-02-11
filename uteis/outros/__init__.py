# P Y H E L P   S I S T E M A   D E   A J U D A   I N T E R A T I V O

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
