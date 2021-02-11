nums = []

continuar = 'S'

while continuar in 'Ss':

    aux = int(input('\nDigite um número: '))
    if aux not in nums:
        nums.append(aux)
        continuar = ' '
        while continuar not in 'SsNn':
            continuar = input('Quer continuar? [S/N]: ')
    else:
        print(f'O número {aux} já existe na lista, não vou adicioná-lo.')
        continuar = 'S'
        continue


print(f'\nOs números são {str(sorted(nums)).replace("[", "").replace("]", "")}')
