from math import pow, sqrt, hypot

adja = int(input('Digite o comprimento do cateto adjacente em cm: '))
opos = int(input('Digite o comprimento do cateto oposto em cm: '))

# De forma manual
hipotenuza = sqrt(pow(adja, 2) + pow(opos, 2))
print('O cumprimento da hipotenuza é de {:.2f}cm'.format(hipotenuza))

# Utilizando hypot da biblioteca math
hipotenuza = hypot(adja, opos)
print('O comprimento da hipotenuza é de {:.2f}cm'.format(hipotenuza))
