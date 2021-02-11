print('Digite o peso de 5 pessoas e veja qual o maio e o menor peso!')

pesos = []

for i in range(0, 5):
    pesos.append(float(input('Peso da {}ª pessoa: '.format(i+1))))

maior = max(pesos)
menor = min(pesos)

print('''
Maior: {}
Menor: {}'''.format(maior, menor))
