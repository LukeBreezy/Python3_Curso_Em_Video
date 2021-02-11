expressao = input('Digite abaixo a sua expressão: \n')

parenteses = []

for i in expressao:
    if i in '()':
        parenteses.append(i)

verif = 0

if parenteses.count('(') != parenteses.count(')') or parenteses[0] != '(' or parenteses[-1] != ')':
    verif -= 1
else:
    for i in parenteses:
        if i == '(':
            verif += 1
        elif i == ')':
            verif -= 1
        if verif < 0:
            break

if verif == 0:
    print('\033[1;32mA expressão é válida!\033[0m')
else:
    print('\033[1;31mA expressão é inválida!\033[0m')

