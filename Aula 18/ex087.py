mat = [[], [], []]
tam = 0
for i in range(3):
    for j in range(3):
        mat[i].append(int(input(f'Digite o valor da posição [{i}, {j}]: ')))
        if i == 0 and j == 0:
            tam = len(str(mat[i][j]))
        elif len(str(mat[i][j])) > tam:
            tam = len(str(mat[i][j]))

print('\n')

for i in range(3):
    for j in range(3):
        print(f'| {mat[i][j]:^{tam}}', end=' ')
    print('|')

del tam

A = 0   # A = soma de todos os valores pares
B = 0   # B = soma dos valores da terceira coluna
C = 0   # C = O maior valor da segunda linha

for i in range(3):
    for j in range(3):
        # A
        if mat[i][j] % 2 == 0:
            A += mat[i][j]
        # B
        if j == 2:
            B += mat[i][j]
        # C
        if i == 1:
            if j == 0:
                C = mat[i][j]
            elif mat[i][j] > C:
                C = mat[i][j]

# Exibindo algumas informações
print(f"""
A soma dos valores pares é igual a {A};
A soma dos valores terceira coluna é igual a {B};
O maior valor da segunda linha é {C}.
""")
