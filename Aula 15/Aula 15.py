while True:
    num = int(input('Digite um número [0 para sair]: '))
    if num == 0:
        break
    else:
        print(f'O número agora é {num:^6}')
