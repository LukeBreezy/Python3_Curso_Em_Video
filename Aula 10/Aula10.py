nome = str(input('Qual o seu nome? '))

if nome == 'Lucas':
    print('Vc é foda!!!')
else:
    print('Vc é normalzinho!')
print('Bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2

print('Sua média é de {:.1f}'.format(med))
print('Parabens!!!' if med >= 7 else 'Vai estudar seu inseto!!!')

