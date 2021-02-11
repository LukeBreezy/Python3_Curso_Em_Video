aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situacao'] = '\033[1;32mAprovado!\033[0m' if aluno['media'] >= 7 else '\033[1;31mReprovado!\033[0m'

print(f'''
Nome: {aluno['nome']}
Média: {aluno['media']}
Situação: {aluno['situacao']}
''')


