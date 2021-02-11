x, y = map(int, input().split())
aux_x = 0
aux_y = 0
cont = 0
print(x)
print(y)

while cont[1] == cont[2]:

    aux_x += 1
    aux_y += 1

    if aux_x / x == 0:
        cont += 1


print('''
Contador: {}
X: {}
Y: {}
'''.format(cont, aux_x, aux_y))
