# Modulo criado por Lucas de Paula (Luke Breezy)

def moeda(x):
    """
    Formata para valor monetario.
    :param x: recebe o valor.
    :return: Valor formatado para monetario.
    """
    return f'R${x:.2f}'.replace('.', ',')


def dobro(x, fmt=True):
    """
    Calcula o dobro de um número.
    :param x: recebe o número que será dobrado.
    :param fmt: booleana que determina se o valor retornado estará formatado com a função 'moeda()'
    :return: dobro de 'x'.
    """
    x *= 2
    return moeda(x) if fmt else x


def metade(x, fmt=True):
    """
    Calcula a metade de um número.
    :param x: recebe o número que será dividido pela metade
    :param fmt: booleana que determina se o valor retornado estará formatado com a função 'moeda()'
    :return: metade de 'x'
    """
    x /= 2
    return moeda(x) if fmt else x


def aumentar(x, ptgm, fmt=True):
    """
    Aumenta 'x' em 'ptgm' porcento.
    :param x: recebe o número que será aumentado.
    :param ptgm: recebe a porcentagem a ser aumentada em 'x'.
    :param fmt: booleana que determina se o valor retornado estará formatado com a função 'moeda()'
    :return: o novo valor aumentado de 'x'.
    """
    ptgm /= 100
    x *= (1 + ptgm)
    return moeda(x) if fmt else x


def diminuir(x, ptgm, fmt=True):
    """
    Diminui 'x' em 'ptgm' porcento.
    :param x: recebe o número que será diminuido
    :param ptgm: recebe a porcentagem a ser diminuida em 'x'
    :param fmt: booleana que determina se o valor retornado estará formatado com a função 'moeda()'
    :return: o novo valor de diminuido de 'x'
    """
    ptgm /= 100
    x *= (1 - ptgm)
    return moeda(x) if fmt else x
