jogador = dict()

jogador['nome'] = input('Nome do aux: ')
qtde_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []

for i in range(qtde_partidas):
    jogador['gols'].append(int(input(f'Quantidade de gols na {i+1}ª partida: ')))

jogador['total'] = sum(jogador['gols'])

print('=-'*20)

print(f'O aux {jogador["nome"]} jogou {len(jogador["gols"])}', 'partidas' if len(jogador["gols"]) > 1 else 'partida')

for i in range(len(jogador["gols"])):
    print(f'\t=> Na {i+1}ª partida, fez {jogador["gols"][i]} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
