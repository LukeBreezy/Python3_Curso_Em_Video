from random import randint, shuffle

qtd = int(input('Digite a quentidade de alunos presentes na sala: '))
alunos = []
ordem = []

for i in range(0, qtd):
    alunos.append(input('Nome do aluno {}: '.format(i+1)))

# De forma manual com randint
while len(ordem) < qtd:
    x = randint(0, qtd-1)
    if x in ordem:
        continue
    else:
        ordem.append(x)

print('A ordem de apresentações é a seguinte: ')
for i in range(0, qtd):
    print('{}ª apresentação: {}'.format(i+1, alunos[ordem[i]]))

# Utilizando shuffle para embaralhar a ordem da lista
shuffle(alunos)
print(alunos)
