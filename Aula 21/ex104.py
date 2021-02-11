# =-=-=-=  FUNÇÕES  =-=-=-=

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


num = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {num}.')
