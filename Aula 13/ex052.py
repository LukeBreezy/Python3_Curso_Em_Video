print('{:=^30}'.format('Número Primo'))

num = int(input('Digite um número inteiro e veja se ele é um número primo: '))
for i in range(1, num + 1):
    if num == 2:
        print('Primo')
        break
    elif num == 1 or num % 2 == 0 or num != i != 1 and num % i == 0:
        print('Nao')
        break
    elif num != i != 1 and num % i != 0 or num != i == 1 and num % i == 0:
        continue
    else:
        print('primo')
