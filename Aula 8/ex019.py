from random import randint, choice

qtd = int(input('Digite a quentidade de alunos presentes na sala: '))
alunos = []

for i in range(0, qtd):
    alunos.append(input('Nome do aluno {}: '.format(i+1)))

# Utilizando randint com um range entre 0 e a quantidade de alunos
escolhido = alunos[randint(0, qtd)]
print('\nO aluno escolhido para apagar o quadro foi {}'.format(escolhido))

# Utilizando choice para escolher um dos alunos
escolhido = choice(alunos)
print('\nO aluno escolhido para apagar o quadro foi {}'.format(escolhido))
