nums = []   # Lista de números que serão inseridos pelo usuario
ent = 0     # Variavel auxiliar para a entrada de dados

print('''Digite números inteiros, e ao final veja a soma de todos eles.
Caso queira parar digite o número 999''')
while ent != 999:
    ent = int(input('Digite um número: '))
    if ent >= 999:
        print('Por favor digite números abaixo de 999.')
    elif ent != 999:
        nums.append(ent)

soma = sum(nums)
print('O resultado da soma dos números que você inseriu é de {}.'.format(soma))
