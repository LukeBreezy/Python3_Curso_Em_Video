infos = ['Lucas', 20]

galera = list()
galera.append(infos)
print(galera)

# Ao inserir a lista infos, dentro da lista galera da maneira acima, foi criada uma ligação.
# Portanto, qualquer alteração em infos, influenciará em galera, conforme abaixo

infos[0] = 'Breezy'
infos[1] = 25

galera.append(infos)
print(galera, '\n')

# Dito isso, a forma apropriada de incluir uma lista dentro de outra lista. é usando fatiamento.

infos.clear()
galera.clear()

infos = ['Lucas', 20]

galera.append(infos[:])
print(galera)

# Ao inserir a lista infos, dentro da lista galera da maneira acima, foi criada uma cópia de
# infos, dentro de galera. Portanto, qualquer alteração em infos, não incluenciará em galera

infos[0] = 'Breezy'
infos[1] = 30

galera.append(infos[:])
print(galera, '\n')

# Outros exemplos

infos.clear()
galera.clear()

for i in range(0, 3):
    infos.append(input(f'Digite o nome da {i+1}ª pessoa: '))
    infos.append(int(input(f'Digite a idade da {i+1}ª pessoa: ')))
    galera.append(infos[:])
    infos.clear()

print(galera, '\n')

# Exibindo a quantiadde de maiores e menores de 18 anos de idade

maior = 0
menor = 0

for i in galera:
    if i[1] > 18:
        maior += 1
    else:
        menor += 1

print(f'Temos nessa lista {maior} pessoas com mais de 18 anos, e {menor} pessoas com menos de 18 anos')
