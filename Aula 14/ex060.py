from math import factorial
num = int(input('Digite um número e veja o fatorial: '))

fatorial = factorial(num)

print('''
Utilizando módulo factorial()
O fatorial de {} é {}'''.format(num, fatorial))

# ===========================================

print('=*' * 20)

fatorial = num

for i in range(num-1, 0, -1):
    fatorial *= i

print('''
Utilizando for():
O fatorial de {} é {}'''.format(num, fatorial))

# ===========================================

print('=*' * 20)

fatorial = num

print('\nUtilizando while:')
print('O fatorial de {} é '.format(num), end='')

while num > 1:
    num -= 1
    fatorial *= num

print(fatorial)




