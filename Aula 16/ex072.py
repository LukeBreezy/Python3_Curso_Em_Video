nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num in range(0, 21):
        print(f'Você digitou o número {nums[num]}.')
        break
    else:
        print('\n\033[1;31mNúmero inválido!!!\n\033[0mSó são permitidos números entre 1 e 20.')
