print('Digite um número e veja sua tabuada.\nDigite um número negativo para parar.')
while True:
    print('~'*20)
    num = int(input('Digite um número: '))
    if num < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{num} * {i} = {num*i}')

