prod = float(input('Qual o valor do produto? R$ '))
promo = prod * 0.95

print('O produto com o valor de R$ {:.2f}, na promoção com 5% de desconto fica R$ {:.2f}.'.format(prod, promo).replace('.', ',', 1))