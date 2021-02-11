print('SUPER LOJÃO')
print('~=' * 10)

prod = {
    'produto': [],
    'valor': []
}

continua = 'S'
maior_mil = 0
while True:
    prod['produto'].append(input('Produto: '))
    prod['valor'].append(float(input('Valor: R$ ')))

    aux = len(prod['produto']) - 1

    if prod['valor'][aux] > 1000:
        maior_mil += 1

    continua = input('Deseja continuar? [S/N]: ').upper()
    if continua == 'N':
        break


barato = prod['valor'].index(min(prod['valor']))
total = sum(prod['valor'])


print(f'''
O total da compra é de R$ {total}
Você comprou {maior_mil} produtos que custam mais de R$ 1000.00
O produto mais barato é: {prod['produto'][barato]}''')
