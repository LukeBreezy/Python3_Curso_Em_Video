from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo qualquer: '))
rad = radians(ang)
seno = sin(rad)
coseno = cos(rad)
tangente = tan(rad)

print('''O ângulo de {}° tem os seguintes atributos: 
Seno = {:.5f}
Coseno = {:.5f}
Tangente = {:.5f}
'''.format(ang, seno, coseno, tangente))




