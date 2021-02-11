from math import sqrt, ceil, floor
import random
import emoji

num = 29
raiz = sqrt(num)

print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))

print('----------------------------------')

print('Teste com random: {:.2}'.format(random.random()))
print('Teste com randint: {}'.format(random.randint(1, 50)))

print('----------------------------------')

print(emoji.emojize("Testes com Emojis: :middle_finger:", use_aliases=True))


