print('{:=^40}'.format('Somando números pares'))
num = 0
soma = 0
for i in range(0, 6):
    num = int(input('Digite o {}º número: '.format(i + 1)))
    if num % 2 == 0:
        soma += num

print('Soma = ', soma)
