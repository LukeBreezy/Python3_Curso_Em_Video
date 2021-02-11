# =-=-=-=  FUNÇÕES  =-=-=-=

def fatorial(fat, show=False):
    """
    Calcula o fatorial do valor na variável fat.
    :param fat: int - Número usado para calcular o fatorial.
    :param show: bool - Caso tenha valor True, a função retorna o passo a passo para chegar no fatorial da variável fat;
                        Caso tenha o valor False, a função retorna apenas o fatorial da variável fat.
    :return: Fatorial de fat ou processo para calcular o fatorial de fat, de acordo com a variável show
    """
    processo = f'{fat} x '
    for i in range(fat-1, 0, -1):
        fat *= i
        processo += f'{i} x ' if i != 1 else f'{i} = {fat}'

    if show:
        return processo
    else:
        return fat


num = 5
teste = fatorial(num, show=True)

print(teste)
help(fatorial)
