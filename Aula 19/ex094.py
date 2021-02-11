infos = dict()      # Modelo de dicionario que vai receber os dados
pessoas = []        # Lista contendo as infomações cadastradas
continuar = 'S'     # Variavel que vai determinar se o usuario quer ou nao continuar cadastrando

while continuar.upper() == 'S':
    # Inserindo nome e garantindo que o campo não esteja vazio
    infos['nome'] = input('Nome: ').title()
    while infos['nome'].replace(' ', '') == '':
        print('\033[1;31mDigite um nome para continuar!\033[0m')
        infos['nome'] = input('Nome: ').title()

    # Inserindo sexo e garantindo que o campo não esteja inválido
    infos['sexo'] = input('Sexo [M/F]: ').upper()
    while infos['sexo'].upper() not in ['M', 'F']:
        print('\033[1;31mOpção inválida!\033[0m')
        infos['sexo'] = input('Sexo [M/F]: ').upper()

    # Inserindo idade e garantindo que não seja uma idade inválida
    infos['idade'] = int(input('Idadde: '))
    while infos['idade'] < 0:
        print('\033[1;31mValor inválido!\033[0m')
        infos['idade'] = int(input('Idadde: '))

    # Fazendo uma cópia do dicionario, e colocando em uma lista
    pessoas.append(infos.copy())

    # Verificando se o usuario quer continuar cadastrando
    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in ['S', 'N']:
        print('\033[1;31mOpção inválida!\033[0m')
        continuar = input('Quer continuar? [S/N]: ').upper()

A = len(pessoas)    # Quantidade de pessoas cadastradas
B = 0               # Média de idade das pessoas cadastradas
C = []              # Lista com todas as mulheres
D = []              # Lista com todas as pessoas com idade acima da média

# Tratando B
for i in pessoas:
    B += i['idade']
B /= A

# Tratando C
for i in pessoas:
    if i['sexo'] == 'F':
        C.append(i)

# Tratando D
for i in pessoas:
    if i['idade'] > B:
        D.append(i)

print('=-='*15)

# Exibindo A
print(f'\n-> Quantidade de pessoas cadastradas: {A}')

# Exibindo B
print(f'\n-> Média de idade das pessoas cadastradas:  {B:.2f}')

# Exibindo C
print('\n-> Mulheres cadastradas: | ', end='')
for m in C:
    print(f'{m["nome"]}', end=' | ')

# Exibindo D
print('\n\n-> Pessoas com idade acima da média: ')
for p in D:
    print('\t| ', end='')
    for k, v in p.items():
        print(f'{k.capitalize()}: {v}', end=' | ')
    print()
