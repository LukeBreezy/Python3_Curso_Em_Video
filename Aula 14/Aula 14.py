num = 1
while num != 0:
    num = int(input('Digite um número: '))

print('Fim do primeiro parenteses.\n\n')

s_n = 'S'
while s_n == 'S':
    num = int(input('Digite um número: '))
    s_n = input('Quer continuar? [S/N]').upper()

print('Fim do segundo parenteses\n\n')
num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números. Entre eles {} são pares e {} são impares.'.format(par+impar, par, impar))
