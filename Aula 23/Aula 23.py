# TRATAMENTO DE ERROS

try:    # try vai tentar executar os comandos
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    s = a / b

except Exception as err:    # except faz o tratamento do erro e pode mostrar uma mensagem personalizada
    print(f'{err.__class__}\nNão é possível dividir por 0.')

else:   # else executa os comandos, caso os comandos em try funcionem corretamente (opcional)
    print(f'{a} + {b} = {s}')

finally:    # finally irá executar os comandos, caso os comandos em try funcionem ou não (opcional)
    print('Volte sempre.')

from uteisCeV.perfumaria import linha
linha(150)
###################################################################################

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    s = a / b

except (ValueError, ZeroDivisionError) as err:
    print(f'\033[1;31m{err}\033[m')

else:
    print(f'{a} + {b} = {s}')

finally:
    print('Volte sempre.')

linha(150)
###########################################################################

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    s = a / b

except ValueError as err:
    print(f'\033[1;31m{err}\033[m')

except ZeroDivisionError as err:
    print(f'\033[1;31m{err}\033[m')

except KeyboardInterrupt as err:
    print(f'\033[1;31m{err}\033[m')

except Exception as err:
    print(f'\033[1;31m{err}\033[m')

else:
    print(f'{a} + {b} = {s}')

finally:
    print('Volte sempre.')


