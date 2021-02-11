print('Calculo do preço de aluguel do carro')

dias = int(input('Quantidade de dias: '))
km = float(input('Km rodados: '))

aluguel = (dias * 60) + (km * 0.15)

print('O preço do aluguel do carro é de R${:.2f}'.format(aluguel))
