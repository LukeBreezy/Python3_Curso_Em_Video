aux = []
pessoas = []
continuar = 'S'

while continuar in 'Ss':
    # Solicitando informações ao usuario
    aux.append(input('Nome: '))
    aux.append(float(input('Peso: ')))
    pessoas.append(aux[:])
    aux.clear()

    # Verificando se o usuario deseja cadastrar mais alguem na lista
    continuar = input('Quer continuar? [S/N]: ')
    while continuar not in 'SsNn':
        print('\033[1;31mOpção inválida!\033[0m')
        continuar = input('Quer continuar? [S/N]: ')
del aux

# Separando os diferentes pesos presentes na lista
pesos = []
for i in pessoas:
    if i[1] not in pesos:
        pesos.append(i[1])

# Definindo o maior e menor peso da lista de pessoas respectivamente
pesado = max(pesos)
leve = min(pesos)
del pesos

# Quantidade de pessoas cadastradas
print(f'Foram cadastradas {len(pessoas)} pessoas.')

# Pessoas mais pesadas
print(f'O maior peso é {pesado:.2f}KG, peso de: | ', end='')
for i in pessoas:
    if i[1] == pesado:
        print(i[0], end=' | ')

# Pessoas mais leves
print(f'\nO menor peso é {leve:.2f}KG, peso de: | ', end='')
for i in pessoas:
    if i[1] == leve:
        print(i[0], end=' | ')
