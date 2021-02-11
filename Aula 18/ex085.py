# a primeira lista dentro de nums receberá os números pares, e a segunda receberá os ímpares
nums = [[], []]

for i in range(7):
    aux = int(input(f'Digite o {i+1}º valor: '))
    if aux % 2 == 0:
        nums[0].append(aux)
    else:
        nums[1].append(aux)

print(f"""
Os números pares são: {sorted(nums[0])}
Os números ímpares são: {sorted(nums[1])}
""")

