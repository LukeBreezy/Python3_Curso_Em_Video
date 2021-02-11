jogadores = list()
aux = dict()
continuar = 'S'

t_aux = 0

while continuar == 'S':
    # Cadastrando nome do jogador e quantidade partidas jogadas
    aux['nome'] = input('Nome do jogador: ')
    qtde_partidas = int(input(f'Quantas partidas {aux["nome"]} jogou? '))
    if qtde_partidas > t_aux:
        t_aux = qtde_partidas
    aux['gols'] = []

    # Inserindo a quantidade de gols feitos em cada partida
    for i in range(qtde_partidas):
        aux['gols'].append(int(input(f'Quantidade de gols na {i + 1}ª partida: ')))

    # Somando a quantidade de gols feitos por um jogador
    aux['total'] = sum(aux['gols'])

    # Inserindo informações do jogador na lista de jogadores
    jogadores.append(aux.copy())

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in ['S', 'N']:
        print('\033[1;31mOpção inválida!\033[0m')
        continuar = input('Quer continuar? [S/N]: ').upper()

print('=-'*20)

print(f'{"cod":<3} {"nome":<15} {"gols":<{qtde_partidas*3}} {"total":<5}')
for i in jogadores:
    print(f'{jogadores.index(i):<3} {i["nome"]:<15} {str(i["gols"]):<{qtde_partidas*3}} {i["total"]:<5}')
print('=-'*20)

opc = 0

while opc != 999:
    opc = int(input('Mostrar dados de qual jogador? '))
    if opc not in range(0, len(jogadores)):
        print('\033[1;31mOpção inválida!\033[0m')
    else:
        print(f'Levantamento do jogador {jogadores[opc]["nome"]}')
        for i in range(len(jogadores[opc]["gols"])):
            print(f'No {i+1}º jogo fez {jogadores[opc]["gols"][i]} gols')
