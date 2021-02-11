infos = dict()
infos = {
    "nome": 'Lucas',
    "idade": 20
}

print(infos)

# Adicionando um novo elemento a um dicionario
infos['sexo'] = 'M'

print(infos, end='\n\n')

# No exemplo abaixo, temos o dicionario filme, ele contem os elementos: Titulo, Ano e Diretor
# Em Python, esses elementos são chamados de keys
filme = {
    'Titulo': 'Vingadores Ultimato',
    'Ano': 2019,
    'Diretor': 'Irmãos Russo'
}

print(filme, end='\n\n')

# filme.keys() vai retornar as chaves presentes no dicionario
print('print(filme.keys()) =\033[1;33m', filme.keys(), end='\033[0m\n')

# filme.values() vai retornar os valores presentes no dicionario
print('print(filme.values()) =\033[1;33m', filme.values(), end='\033[0m\n')

# filme.items() vai retornar as chaves e seus respectivos valores
print('print(filme.items()) =\033[1;33m', filme.items(), end='\033[0m\n\n')

# -----------------------------------------------------------------------------
# Exibindo algumas informações com laço de repetição

print('=-=-= INFORMAÇÕES DO FILME =-=-=')
for k, v in filme.items():
    print(f'{k}: {v}')

print()
# Utilizando um dicionario dentro de uma lista
locadora = [filme]
print('print(locadora[0]["Ano"]) =\033[1;33m', locadora[0]["Ano"], '\033[0m')
print()

estados = []
estado1 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
estado2 = {
    'uf': 'Bahia',
    'sigla': 'BA'
}
estados.append(estado1)
estados.append(estado2)
print(estados)
print()
del estados, estado1, estado2

estado = dict()
brasil = list()
for i in range(3):
    estado['uf'] = input('UF: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()

print()
# Outros exemplos
print(f'O {infos["nome"]} tem {infos["idade"]} anos de idade')

print(infos)

infos['nome'] = 'Luke'
del infos['sexo']
infos['estado'] = 'SP'

print(infos)