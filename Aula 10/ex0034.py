salario = float(input('Digite o valor do seu salário: R$'))

if salario > 1250:
    salario *= 1.1
else:
    salario *= 1.15

print('O seu salário foi aumentado para R${:.2f}'.format(salario))
