nums = []

for i in range(0, 5):
    aux = int(input('Digite um número: '))
    if i == 0:
        nums.append(aux)
    else:
        if aux >= max(nums):
            nums.append(aux)
        elif aux <= min(nums):
            nums.insert(0, aux)
        else:
            for pos, j in enumerate(nums):
                if j < aux <= nums[pos+1]:
                    nums.insert(pos+1, aux)
                    break
    print(f'O número {aux} foi adicionado na {nums.index(aux)+1}ª posição.')

print(f'\nOs números são: {str(nums).replace("[", "").replace("]", "")}')
