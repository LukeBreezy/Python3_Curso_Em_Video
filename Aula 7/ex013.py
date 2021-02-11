salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario * 1.15
print('O salário de R$ {:.2f}, com 15% de aumento passa a valer R$ {:.2f}.'.format(salario, novo).replace('.', ',', 2))
