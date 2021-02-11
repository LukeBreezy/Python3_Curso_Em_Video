from math import pow

print('Informe seu \033[1;32mpeso\033[m e \033[1;31maltura\033[m para calcular o seu \033[1;33mIMC\033[m, e ver em qual a sua classificação!')

IMC = float(input('\033[1;32mPeso\033[m: ')) / pow(float(input('\033[1;31mAltura\033[m: ')), 2)

print('\033[1;33mIMC\033[m = {:.2f}'.format(IMC))

print('Sua classificação é: ', end='')
if IMC < 18:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif 40 < IMC:
    print('Obesidade mórbida')
