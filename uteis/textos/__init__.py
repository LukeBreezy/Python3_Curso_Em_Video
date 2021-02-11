# L I N H A   A D A P T A V E L
def linha(x):
    print('-' * (len(x) + 4))


# M E N S A G E M   C O M   C O R   N O   F U N D O
def msg(txt, cor):
    tam = len(txt) + 4
    print('\033[1;' + str(cor) + 'm' + '=' * tam)
    print(f'{txt:^{tam}}')
    print('=' * tam, '\n\033[0m', end='')
