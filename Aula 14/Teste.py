"""parenteses = {
    'nome': [],
    'idade': [],
    'sexo': []
}

for i in range(0, 3):
    parenteses['nome'].append(str(input('Nome: ')))
    parenteses['idade'].append(int(input('Idade: ')))
    parenteses['sexo'].append(str(input('Sexo: ')))

print(parenteses)

for i in range(0, 3):
    print('''\t\t===== {}ª PESSOA =====
    Nome: {}
    Idade: {}
    Sexo: {}
    '''.format(i+1, parenteses['nome'][i], parenteses['idade'][i], parenteses['sexo'][i]))

print('tamanho: ', len(parenteses))

indice = parenteses['idade'].index(max(parenteses['idade']))

print('mais velho: ', parenteses['nome'][indice])


parenteses = {
    'nome': ['Lucas', 'Ingrid', 'Luke'],
    'idade': [54, 56, 11],
    'sexo': ['M', 'M', 'M']
}
ind = parenteses['sexo'].index('M')
print(ind)
"""

while num != 0:
    try:
        num = int(input('Numero: '))
        print(num)
    except NameError:
        num = int(input('Numero: '))