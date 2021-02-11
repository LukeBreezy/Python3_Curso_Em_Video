mat = [[], [], []]
tam = 0
for i in range(3):
    for j in range(3):
        mat[i].append(int(input(f'Digite o valor da posição [{i}, {j}]: ')))
        if i == 0 and j == 0:
            tam = len(str(mat[i][j]))
        elif len(str(mat[i][j])) > tam:
            tam = len(str(mat[i][j]))

print()

for i in range(3):
    for j in range(3):
        print(f'| {mat[i][j]:^{tam}}', end=' ')
    print('|')
