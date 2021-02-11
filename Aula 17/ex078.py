nums = []

for i in range(0, 5):
    nums.append(int(input(f'Insira o {i+1}º número: ')))

print(f'\nOs números são: {str(nums).replace("[", "").replace("]", "")}')

print(f"\nO maior valor da lista é {max(nums)}, localizado nas posições ", end='')

# MAIOR
for pos, i in enumerate(nums):
    if i == max(nums):
        print(f"{pos+1}... ", end='')

print(f"\nO menor valor da lista é {min(nums)}, localizado nas posições ", end='')

# MENOR
for pos, i in enumerate(nums):
    if i == min(nums):
        print(f"{pos+1}... ", end='')
