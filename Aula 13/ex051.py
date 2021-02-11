print('{:=^50}'.format('Progressao Aritmetica'))

PA = []

PA.append(int(input('Digite o primeiro termo da Progressão Aritmetica: ')))
razao = int(input('Digite a razaão da Progressão Aritmetica: '))

for i in range(1, 10):
    PA.append(PA[i-1] + razao)

print('A seguir, os 10 primeiros termos da P.A.:')

for i in range(0, 10):
    print('{} | '.format(PA[i]), end='')
