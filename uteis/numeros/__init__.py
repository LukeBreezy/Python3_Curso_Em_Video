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
