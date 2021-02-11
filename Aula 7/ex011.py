alt = float(input('Altura da parede: '))
larg = float(input('Largura da parede: '))
area = alt*larg
tinta = area/2
print('\nA área da parede é de {:.2f}m².\nPara pintá-la é necessário {:.3f}L de tinta.'.format(area, tinta))
