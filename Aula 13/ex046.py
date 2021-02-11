from emoji import emojize
from time import sleep

for i in range(10, 0, -1):
    print('{}!'.format(i))
    sleep(1)
print(emojize(':fireworks:', use_aliases=True))