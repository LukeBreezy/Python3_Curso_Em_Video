lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutaveis
# Portanto o comando abaixo não funciona
# lanche[1] = 'Refrigerante'

for pos, comida in enumerate(lanche):
    print(f'Posição {pos} - Lanche: {comida}')

print('=~'*10)

for i in range(0, len(lanche)):
    print(f'Posição {i} - Lanche: {lanche[i]}')


print('=~'*10)

print(lanche)
print(lanche[3])
print(lanche[2:])
print(lanche[0:3])
print(lanche[-4:-1])
# Ordena em ordem alfabetica
print(sorted(lanche))

print('=~'*10)

x = (10, 20, 15, 100, 17)
y = (17, 35, 15, 95)
z = x + y

for i in (x, y, z):
    print(i)

print(f'\nz.count(17) = {z.count(17)}')

print(f'z.index(15) = {z.index(15)}')
print(f'z.index(15, 3) = {z.index(15, 3)}')

