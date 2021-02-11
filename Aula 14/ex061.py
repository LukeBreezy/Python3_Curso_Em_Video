termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
enesimo = termo + razao * 10
print('A seguir, os 10 primeiros termos da PA')
while termo < enesimo:
    print(termo, end=' | ')
    termo += razao
