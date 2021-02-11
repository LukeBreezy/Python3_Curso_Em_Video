def leiaInt(txt):
    """
    Valída se o valor digitado é um número inteiro, enquanto não for, o programa não prossegue.
    :param txt: será exibido na tela, solicitando o valor para o usuário.
    :return: valor inteiro digitado pelo usuário.
    """

    while True:
        try:
            n = int(input(txt))

        except (ValueError, KeyboardInterrupt):
            print('\033[1;31mErro, valor inválido!\033[m')
            continue

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

        except (ValueError, KeyboardInterrupt):
            print('\033[1;31mErro, valor inválido1\033[m')
            continue

        else:
            return n


def leiaStr(txt):
    """
    Valida se o texto digitado é alfabetico, não contendo números ou símbolos.
    :param txt: será exobido na tela, solicitando o texto para o usuário.
    :return: texto alfabetico digitado pelo usuario.
    """
    while True:
        s = input(txt)
        if not s.replace(' ', '').isalpha():
            print('\033[1;31mErro! Só são permitidas letras.\033[m')
            continue
        else:
            break
    return s.strip()
