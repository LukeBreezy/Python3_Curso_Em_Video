num = []

for i in range (0, 3):
    num.append(int(input('Digite o {}º número: '.format(i+1))))

maior = num[0]
menor = num[0]
print('\nDe maneira lógica: ')

for i in range(0, 3):
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]

print('''
Maior = {}
Menor = {}
'''.format(maior, menor))

print('Utilizando método max: ')

print('''
Maior = {}
Menor = {}
'''.format(max(num), min(num)))