# Este arquivo é um modulo, contem diversas funções criadas por mim mesmo.

# Com ele é possivel importar essas funções para outros projetos,
# da mesma forma que importamos modulos internos e não internos do Python, como time, math, random entre outras.

# Modulos são muito uteis quando começamos trabalhar com projetos maiores e que exigem mais funcionalidades.
# Mas pode chegar um momento em que este arquivo fique muito cheio de informações, e até dificil de encontrar as coisas.
# Eis então que podemos usar pacotes, onde basicamente podemos separar modulos por assunto (valida, texto, data e etc).
# Assim na hora de importar nossas funções para um projeto, temos menos trabalho para identificar a funcionalidade
# necessaria, temos as funções e os modulos organizados e potencialmente projetos "mais leves".


# ----------------------------------------------------------------------------------------------------------------------

# L I N H A   A D A P T A V E L
def linha(x):
    print('-' * (len(x) + 4))


# M E N S A G E M   C O M   C O R   N O   F U N D O
def msg(txt, cor=0):
    tam = len(txt) + 4
    print('\033[1;' + str(cor) + 'm' + '=' * tam)
    print(f'{txt:^{tam}}')
    print('=' * tam, '\n\033[0m', end='')


# F A T O R I A L
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


# L E I T O R   D E   I N T E I R O
def leiaInt(txt):
    """
    Valída se o valor digitado é um número inteiro, enquanto não for, o programa não prossegue.
    :param txt: Será exibido na tela, solicitando o valor para o usuário.
    :return: Valor inteiro digitado pelo usuário.
    """
    n = input(txt)
    while n.isdecimal() is False:
        print('\033[1;31mDigite um valor númerico inteiro!\033[0m')
        n = input(txt)
    return n


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
