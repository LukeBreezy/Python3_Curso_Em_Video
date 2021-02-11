from datetime import date
print('Digite o ano de nascimento de 7 pessoas, e veja quantas delas ja são maiores de idade e quantas não são.\n(Considerando a maior idade 21 em diante)')

nascimento = []

for i in range(0, 7):
    nascimento.append(int(input('Ano de nascimento da {}ª pessoa: '.format(i+1))))

maior_21 = 0
menor_21 = 0
for i in range(0, 7):
    if date.today().year - nascimento[i] >= 21:
        maior_21 += 1
    else:
        menor_21 += 1

print('''
Entre essas pessoas temos
{} maiores de idade
{} menores de idade
'''.format(maior_21, menor_21))
