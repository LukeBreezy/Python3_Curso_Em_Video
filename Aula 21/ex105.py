# =-=-=-=  FUNÇÕES  =-=-=-=

def notas(*n, sit=False):
    """

    :param n: Recebe a(s) nota(s) dos alunos
    :param sit: Determina se a situação da sala de acordo com a média
                (media > 7 = BOA; 5 < media < 7 = RAZOÀVEL; media < 5 = RUIM)
    :return: Dicionário com as informações da sala
    """
    estats = dict()
    estats['Quantidade'] = len(n)
    estats['Maior'] = max(n)
    estats['Menor'] = min(n)
    estats['Média'] = sum(n) / estats['Quantidade']

    infos = ''

    for k, v in estats.items():
        infos += f'{k}: {v}\n'
    if sit:
        if estats['Média'] > 7:
            infos += 'Situação: BOA'
        elif estats['Média'] > 5:
            infos += 'Situação: RAZOÁVEL'
        else:
            infos += 'Situação: RUIM'
    return infos


# =-=-=-=  MAIN  =-=-=-=
res = notas(5.5, 2.5, 1.5, sit=True)
print(res)
help(notas)

