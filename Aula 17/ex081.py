nums = []

continuar = 'S'

while continuar in 'Ss':
    # Inserindo um número na lista
    nums.append(int(input('Digite um número: ')))

    # Verificando se o usuario quer continuar adicionando números na lista
    continuar = input('Quer continuar? [S / N]: ')

    # Garantindo que o usuario dê uma resposta válida
    while continuar not in 'SsNn':
        print('\033[1;31mComando inválido!\033[0m')
        continuar = input('Quer continuar? [S / N]: ')

print(f"""
Foram inseridos {len(nums)} números na lista.
Lista ordenada decrescente: {sorted(nums, reverse=True)}.
O número 5 {f'foi inserido {nums.count(5)} vezes' if 5 in nums else 'não foi inserido'} na lista.
""")
