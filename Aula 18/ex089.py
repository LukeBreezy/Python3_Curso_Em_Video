alunos = []   # Lista que vai armazenar os nomes e notas dos alunos
opt = 'S'     # Variavel que determina se o usuário vai inserir mais alunos
c = 0         # Contador para fazer o controle do índice na lista de alunos

while opt in 'Ss':
    # Criando a lista que receberá informações de 1 aluno
    alunos.append([])

    # Inserindo nome do aluno
    alunos[c].append(input('Nome do aluno: '))
    while alunos[c][0].replace(' ', '') == '':
        print('\033[1;31mPor favor, insira um nome para prosseguir!\033[0m')
        alunos[c][0] = input('Nome do aluno: ')

    # Criando a lista que receberá as notas
    alunos[c].append([])

    # Inserindo Nota 1, e garantindo que esteja entre 0 e 10
    alunos[c][1].append(float(input('Nota 1: ')))
    while alunos[c][1][0] < 0 or alunos[c][1][0] > 10:
        print('\033[1;31mNota inválida! São permitidas apenas notas entre 0 e 10.\033[0m')
        alunos[c][1][0] = float(input('Nota 1: '))

    # Inserindo Nota 2, e garantindo que esteja entre 0 e 10
    alunos[c][1].append(float(input('Nota 2: ')))
    while alunos[c][1][1] < 0 or alunos[c][1][1] > 10:
        print('\033[1;31mNota inválida! São permitidas apenas notas entre 0 e 10.\033[0m')
        alunos[c][1][1] = float(input('Nota 2: '))

    # Calculando a média do aluno
    alunos[c][1].append((sum(alunos[c][1])) / 2)

    # Verificando se o usuário quer continuar inserindo alunos e notas
    opt = input('Quer continuar? [S/N]: ')
    while opt.upper() not in 'SN' or len(opt) != 1:
        print('\033[1;31mOpção inválida!\033[0m')
        opt = input('Quer continuar? [S/N]: ')

    # Incrementando o contador
    c += 1

# Exibindo uma lista zebrada, com nomes e média dos alunos
print('=-' * 15)

print(f'\033[1;33;7m {"No.":<4} | {"Nome":<15} | {"Média":>4} \033[0m')
for pos, i in enumerate(alunos):
    if pos % 2 != 0:
        print(f'\033[1;37;7m {pos:<4} | {i[0][:15]:<15} | {i[1][2]:>5.2f} \033[0m')
    else:
        print(f'\033[1;7m {pos:<4} | {i[0][:15]:<15} | {i[1][2]:>5.2f} \033[0m')

print('=-' * 15)

# Exibindo as notas de um aluno específico, escolhido pelo usuário
opt = 0
while opt != 999:
    opt = int(input('\nMostrar notas de qual aluno? (999: Interromper): '))

    while 999 != opt not in range(0, len(alunos)):
        print('\033[1;31mNão existe um aluno cadastrado nesse índice, tente novamente!\033[0m')
        opt = int(input('\nMostrar notas de qual aluno? (999: Interromper): '))

    if opt == 999:
        print('\033[1;33mObrigado por utilizar nosso sistema, até a logo!')
        break
    else:
        print(f'\033[1;33;7m {"No.":<4} | {"Nome":<15} | {"Nota 1":} | {"Nota 2":} \033[0m')
        print(f'\033[1;7m {opt:<4} | {alunos[opt][0]:<15} | {alunos[opt][1][0]:>6.2f} | {alunos[opt][1][1]:>6.2f} \033[0m')
