# =-=-=-=  FUNÇÕES  =-=-=-=

def ficha(nome, pts):

    if nome == '':
        nome = '<desconhecido>'

    if pts == '' or pts.isnumeric() is False:
        pts = 0

    return f'O jogador {nome} fez {pts} ponto(s) no torneio.'


nome = input('Nome do jogador: ')
pts = input('Quantidade de pontos: ')

infos = ficha(nome, pts)
print(infos)
