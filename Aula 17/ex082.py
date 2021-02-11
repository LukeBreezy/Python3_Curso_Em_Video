nums = []
par = []
impar = []
continuar = 'S'

while continuar in 'Ss':
    # Inserindo um número na lista
    nums.append(int(input('Digite um número: ')))

    # Verificando se o usuario quer continuar inserindo números na lista
    continuar = input('Quer continuar? [S / N]: ')
    while continuar not in 'SsNn':
        print('\033[1;31mComando inválido!\033[0m')
        continuar = input('Quer continuar? [S / N]: ')

for i in nums:
    # Separando números pares e ímpares
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"""{'=-' * 40}
Números: {nums}
Pares: {par}
Impares: {impar}
""")
