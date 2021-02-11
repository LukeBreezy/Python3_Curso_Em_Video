# Este modulo contem algumas funções para estetica, como colocar uma linha para separar ou exibir uma mensagem formatada

def msg(txt, cor=0, adpt=False, tam_c=60):
    """
    Formata um texto e deixa confortavel visualmente, ou uma linha acima e outra abaixo.
    :param txt: texto a ser exibido.
    :param cor: cor de fundo, por padrão não tem.
    :param adpt: booleana que determina se as linhas vão se adaptar ao tamanho do texto ou não, por padrão é False
    :param tam_p: tamanho customizado das linhas, por padrão é 60.
    :return: texto formatado
    """
    if adpt:
        tam = len(txt) + 4
    else:
        tam = tam_c

    print('\033[1;' + str(cor) + 'm' + '-' * tam)
    print(f'{txt:^{tam}}')
    print('-' * tam, '\n\033[0m', end='')


def linha(x=60):
    """
    Introduz uma linha em determinada parte do programa
    :param x: recebe o tamanho da linha, por padrão é 60
    :return: exibe a linha
    """
    print('-' * x)