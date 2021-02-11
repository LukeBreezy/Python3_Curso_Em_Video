nums = []   # Lista que receberá os números inseridos pelo usuarios
opt = 'S'   # Variavel que determina se o usuario quer continuar inserindo números ou não

print('Digite números inteiros, e ao final, veja qual é o maior número, menor número e a média entre eles.')

while opt != 'N':
    if opt == 'S':
        nums.append(int(input('\nDigite um número: ')))
    else:
        print('Opção inválida, por favor responda com S para sim ou N para não.')
    opt = input('Deseja inserir outro número? [S / N]: ').upper()

media = sum(nums) / len(nums)   # Média dos valores na lista nums

# Exibindo algumas informações
print('''
Média: {}
Maior: {}
Menor: {}
'''.format(media, max(nums), min(nums)))
