"""(°C × 9/5) + 32 = °F"""

celsius = float(input('Temperatura em °C: '))
fahrenheit = celsius * 9 / 5 + 32

print('{:.2f} °C é equivalente a {:.2f} °F.'.format(celsius, fahrenheit))
