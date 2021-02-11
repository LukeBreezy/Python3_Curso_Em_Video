num = int(input('Digite um número entre 0 e 9999: '))

digitos = ['Unidade', 'Dezena', 'Centena', 'Milhar']

print('Método Guanabara')
for i in range(0, 4):
    print(digitos[i], '=', num // 10**i % 10)
