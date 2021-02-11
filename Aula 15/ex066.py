num = []

while True:
    aux = int(input('Digite um número [999 para parar]: '))
    if aux == 999:
        break
    num.append(aux)

soma = sum(num)
qtde = len(num)
print(f'Você inseriu {qtde} números, a soma entre eles é igual a {soma}')
