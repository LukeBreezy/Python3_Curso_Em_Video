x = int(input('Digite um número e veja sua tabuada: '))

for i in range(0, 11):
    print('{:^2} * {:^2} = {}'.format(x, i, x*i))
    i = i + 1
