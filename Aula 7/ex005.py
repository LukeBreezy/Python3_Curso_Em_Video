def antesuc(y):
    if y.isnumeric() is False:
        print('{} não é um número.'.format(y))
        antesuc(input('Digite um número'))
    else:
        print('O antecessor de {} é'.format(y), int(y)-1, 'e o sucessor é', int(y)+1)


x = input('Digite um número')
antesuc(x)
