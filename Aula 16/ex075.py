nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')))

print(f'Os números são: {str(nums).strip("()")}')

# QUANTAS VEZES APARECE O NÚMERO 9
if 9 in nums:
    print(f'O número 9 apareceu {nums.count(9)} vezes.')
else:
    print('O número 9 não apareceu nenhuma vez.')

# QUAL A POSIÇÃO DA PRIMEIRA OCORRENCIA DO NÚMERO 3
if 3 in nums:
    print(f'A primeira ocorrência do número 3 foi na {nums.index(3)+1}ª posição.')
else:
    print('O número 3 não apareceu nenhuma vez.')

# QUAIS SÃO OS NÚMEROS PARES
print('Os números pares são: ', end='')
for i in nums:
    if i % 2 == 0:
        print(i, end=' ')
