celsius = float(input('Informe a temperatura em °C: '))
kelvin = celsius + 273
fahrenheit = ((9 * celsius) / 5) + 32

print('A temperatura de {:.2f}°C corresponde a {:.2f}°F e {:.2f}°K'.format(celsius, fahrenheit, kelvin))
