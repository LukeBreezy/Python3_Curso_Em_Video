from moeda import *
def resumo(v, aum, dim):
    """
    Faz um resumo de 'v', contendo dobro, metade, aumento e redução.
    :param v: valor a ser analisado.
    :param aum: porcentagem a ser aumentada em 'v'
    :param dim: porcentagem a ser diminuida em 'v'
    :return: exibe todas as analises feitas com 'v'
    """

    from perfumaria import msg, linha
    msg(txt='RESUMO DO VALOR', tam_c=32)

    print(f'Preço analisado: {moeda(v):>15}')
    print(f'Metade do preço: {metade(v):>15}')
    print(f'Dobro do preço: {dobro(v):>16}')
    print(f'{aum}% de aumento: {aumentar(v, aum):>{16 if aum >= 10 else 17}}')
    print(f'{dim}% de redução: {diminuir(v, dim):>{16 if dim >= 10 else 17}}')

    linha(32)
