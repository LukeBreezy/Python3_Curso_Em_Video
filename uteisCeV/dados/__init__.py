def leiaDinheiro(x):
    """
    Valida se o valor é numerico e impede que o usuario continue enquanto o valor for invalido
    :param x: recebe o valor
    :return: float(x)
    """
    if str(x).replace(',', '').replace('.', '').isdigit():
        return float(str(x).replace(',', '.'))
    else:
        while not str(x).replace(',', '').replace('.', '').isdigit():
            print(f'\033[1;31mErro, "{x}" é um valor inválido. Insira um valor numerico!\033[m')
            x = str(input('Digite um valor: R$ '))
        return float(str(x).replace(',', '.'))


def resumo(v, aum, dim):
    """
    Faz um resumo de 'v', contendo dobro, metade, aumento e redução.
    :param v: valor a ser analisado.
    :param aum: porcentagem a ser aumentada em 'v'
    :param dim: porcentagem a ser diminuida em 'v'
    :return: exibe todas as analises feitas com 'v'
    """

    import uteisCeV.moeda as m
    from uteisCeV.perfumaria import msg, linha

    v = float(leiaDinheiro(v))

    msg(txt='RESUMO DO VALOR', tam_c=32)

    print(f'Preço analisado: {m.moeda(v):>15}')
    print(f'Metade do preço: {m.metade(v):>15}')
    print(f'Dobro do preço: {m.dobro(v):>16}')
    print(f'{aum}% de aumento: {m.aumentar(v, aum):>{16 if aum >= 10 else 17}}')
    print(f'{dim}% de redução: {m.diminuir(v, dim):>{16 if dim >= 10 else 17}}')

    linha(32)
