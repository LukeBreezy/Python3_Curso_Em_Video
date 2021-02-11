from time import sleep
print('='*20)
print('{:^20}'.format('CAIXA ELETRONICO'))
print('='*20)

sacar = int(input('Digite o valor a ser sacado: R$'))
cedulas = [50.0, 20.0, 10.0, 1.0]

print('\033[1;33mProcessando', end='')
for i in range(0, 4):
    sleep(.5)
    print('.', end='')
    if i == 3:
        print('\n')


print('\033[0m='*20)

cont_ced = sacar
i = 0

while True:
    aux = int(cont_ced // cedulas[i])
    if aux != 0:
        print(f'Total de {aux} notas de R$ {cedulas[i]:.2f}')
        cont_ced -= aux * cedulas[i]
    i += 1
    if cont_ced == 0:
        break
