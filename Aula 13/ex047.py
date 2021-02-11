print('{:=^35}'.format('Numeros Pares'))
for i in range(1, 51):
    if i % 2 == 0:
        if i % 10 == 0:
            print('{:^4} | '.format(i), end='\n')
        else:
            print('{:^4} | '.format(i), end='')
