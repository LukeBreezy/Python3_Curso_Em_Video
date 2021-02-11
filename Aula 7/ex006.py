def numbers(y):
    if y.isnumeric() is False:
        numbers(input('Digite um número: '))
    else:
        print('O dobro de {} é {}'.format(y, int(y) * 2))
        print('O triplo de {} é {}'.format(y, int(y) * 3))
        print('A raiz quadrada de {} é {:.2f}'.format(y, int(y) ** (1/2)))


x = input('Digite um número: ')
numbers(x)
