num = int(input('Digite um número e veja sua tabuada: '))

for i in range(1, 11):
    print('{} * {:^2} = {:^2}'.format(num, i, num*i))
