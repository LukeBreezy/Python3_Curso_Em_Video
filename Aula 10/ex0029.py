velocidade = int(input('Qual foi a velocidade do carro em KM/H: '))
multa = 7.00
if velocidade > 80:
    print('''
A velocidade ultrapassou o limite de 80KM/H.
Sua multa é de R${:.2f}!
'''.format(multa * (velocidade - 80)))
else:
    print('Não ultrapassou o limite de velocidade!')
