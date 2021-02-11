distancia = int(input('Digite a distancia da viagem em KM: '))

print('''
As viagens com até 200KM de distancia, cobram R$0.50 por KM.
Para viagens mais lingas que 200KM, serão cobrados R$0.45 por KM.
''')

if distancia <= 200:
    print('Sendo assim, o valor da sua viagem será o total de R${:.2f}.'.format(distancia * 0.5))
else:
    print('Sendo assim, o valor da sua viagem será o total de R${:.2f}.'.format(distancia * 0.45))
