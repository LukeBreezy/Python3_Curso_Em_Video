#A função abaixo valída se o tipo de dado do valor inserido pelo usuario, está de acordo com o solicitado
def valid(x):
    if x.isnumeric() is False:
        print('''Caractere inválido! Apenas números inteiros positivos são aceitos.
Faça as correções necessárias e tente novamente.
''')
        return False
    elif x.isnumeric() is True and int(x) == 0:
        print('Valor inválido!\nO número deve ser maior que 0.')
        return False
    elif x.isnumeric() is True and int(x) > 0:
        return True


#Este input de x e o while, garantem que o programa solicite o valor novamente caso esteja fora dos padrões solicitados
x = input('Digite um número inteiro positivo, e veja os números primos entre 0 e ele: ')
while valid(x) is False:
    x = input('Digite um número inteiro positivo, e veja os números primos entre 0 e ele: ')

print('''

São primos os seguintes números:

''')

#E aqui é onde a mágiica acontece!!!
#Baseado no número solicitado no início, o programa identifica todos os números primos,
#num intervalo de 0 até o número inserido pelo usuário
x = int(x)
k = 0
for i in range(1, x + 1):
    if i == 1:
        continue
    elif i == 2:
        print('|{:^{}}'.format(i, len(str(x))+4), end='')
        k = k + 1
    if i % 2 == 0:
        continue
    else:
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                break
            elif i % j != 0:
                continue
            else:
                print('|{:^{}}'.format(i, len(str(x))+4), end='')
                k = k + 1
    if k == 10:
        print('|\n')
        k = 0
