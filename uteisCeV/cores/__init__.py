def cor(txt, corFonte='limp', corFundo='limp', fonte=True, fundo=False):
    """
    Personaliza a cor da fonte e do fundo de textos
    :param txt: texto a ser retornado
    :param corFonte: string com as 4 primeiras letras do nome da cor que será usada para a fonte
    :param corFundo: string com as 4 primeiras letras do nome da cor que será usada para o fundo
    :param fonte: booleana que determina se alguma cor será aplicada a fonte, por padrão é True
    :param fundo: booleana que determina se alguma cor será aplicada ao fundo, por padrão é False
    :return: texto com fonte e fundo personalizados
    """
    cores = {
        'pret': 0,
        'verm': 1,
        'verd': 2,
        'amar': 3,
        'azul': 4,
        'roxo': 5,
        'cian': 6,
        'cinz': 7,
        'limp': ''
    }
    if corFonte == 'limp':
        fonte = False
    if corFundo == 'limp':
        fundo = False

    if fonte and fundo:
        return '\033[1;' + str(30+cores[corFonte]) + ';' + str(40+cores[corFundo]) + 'm' + txt + '\033[m'
    elif fonte:
        return '\033[1;' + str(30+cores[corFonte]) + 'm' + txt + '\033[m'
    elif fundo:
        return '\033[1;' + str(40+cores[corFundo]) + 'm' + txt + '\033[m'
    else:
        return f'\033[m{txt}'
