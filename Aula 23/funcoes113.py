def leiaInt(txt):
    """
    Valída se o valor digitado é um número inteiro, enquanto não for, o programa não prossegue.
    :param txt: será exibido na tela, solicitando o valor para o usuário.
    :return: valor inteiro digitado pelo usuário.
    """

    while True:
        try:
            n = int(input(txt))

        except ValueError:
            print('\033[1;31mErro, valor inválido!\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário não quis digitar este número.\033[m')
            n = 0
            return n

        else:
            return n


def leiaFloat(txt):
    """
    Valída se o valor digitado é um número real, enquanto não for, o programa não prossegue.
    :param txt: será exibido na tela, solicitando o valor para o usuário.
    :return: valor real digitado pelo usuário.
    """

    while True:
        try:
            n = float(input(txt))

        except ValueError:
            print('\033[1;31mErro, valor inválido1\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário não quis digitar este número.\033[m')
            n = 0
            return n

        else:
            return n
