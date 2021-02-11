def linha():
    print('=' * 50)


def maior(* n):
    linha()
    print(f'Foram passados {len(n)} valores.\nSendo eles: ', end='')
    for i in n:
        print(i, end=' ')
    print(f'\nO maior valor informado foi {max(n)}')


maior(27, 21, 68)
maior(28, 64, 87, 68, 0, 72, 38)
maior(81, 96, 92, 9, 36, 6)
maior(30, 80)
maior(82, 37)
