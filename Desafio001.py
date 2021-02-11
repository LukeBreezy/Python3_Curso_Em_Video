#A função abaixo valída se o tipo de dado do primeiro valor inserido pelo usuario, está de acordo com o solicitado
def valid(x):
    if x.isnumeric() is False:
        print('''
Caractere inválido! Apenas números inteiros positivos são aceitos.
Faça as correções necessárias e tente novamente.
''')
        return False
    elif x.isnumeric() is True and int(x) == 0:
        print('Valor inválido!\nO número deve ser maior que 0.')
        return False
    elif x.isnumeric() is True and int(x) > 0:
        return True


#A função abaixo valída se o tipo de dado do segundo valor inserido pelo usuario, está de acordo com o solicitado
def valid2(y, x):
    if str(y).isnumeric() is False:
        print('''
Caractere inválido! Apenas números inteiros a partir de 0 em diante são aceitos.
Faça as correções necessárias e tente novamente.        
''')
        return False
    elif str(y).isnumeric() is True and int(y) > int(x):
        print('Valor inválido!\n{} é maior que {}'.format(y, x))
        return False
    elif str(y).isnumeric() is True and int(y) >= int(x):
        return True


#Estes inputs de x e y, e os whiles após ambos, garantem que o programa solicite o valor novamente caso esteja fora dos padrões solicitados
x = input('Digite um número inteiro positivo: ')
while valid(x) is False:
    x = input('Digite um número inteiro positivo: ')

x = int(x)

y = input('Digite um número inteiro entre 0 e {} inclusive: '.format(x))
while valid2(y, x) is False:
    y = input('Digite um número inteiro entre 0 e {} inclusive: '.format(x))

y = int(y)


#O código abaixo faz a verificação dos números que dividem o segundo valor inserido pelo usuario
print('''
{} é divisivel por: 
'''.format(y))

j=0
for i in range(1, x+1):
    if y % i == 0:
        print('|{:^{}}'.format(i, len(str(y)) + 2), end = '')
        j = j + 1
        if j == 10:
            j = 0
            print('|\n')