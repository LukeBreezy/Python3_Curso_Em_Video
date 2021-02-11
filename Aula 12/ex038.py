print('Digite dois números inteiros e veja se um deles é maior que o outro!')

nums = []
nums.append(int(input('1º número: ')))
nums.append(int(input('2º número: ')))

if nums[0] > nums[1]:
    print('O primeiro número ({}) é maior!'.format(nums[0]))
elif nums[1] > nums[0]:
    print('O segundo número({}) é maior!'.format(nums[1]))
else:
    print('Nenhum é maior que o outro, ambos são iguais!')
