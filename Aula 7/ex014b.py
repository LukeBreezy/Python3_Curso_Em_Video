"""(°F - 32) / 9 * 5 = °C"""

fahrenheit = float(input('Temperatura em °F: '))
celsius = (fahrenheit - 32) / 9 * 5

print('{:.2f} °F é equivalente a {:.2f} °C.'.format(fahrenheit, celsius))
