from random import randint
aux = []

for i in range(0, 5):
    aux.append(randint(0, 10))

nums = (aux[0], aux[1], aux[2], aux[3], aux[4])
del aux

print(f"""
Os números são: {str(nums).strip('()')}
Maior número: {max(nums)}
Menor número: {min(nums)}
""")

