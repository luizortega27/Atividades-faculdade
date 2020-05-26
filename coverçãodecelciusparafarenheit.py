#Faça um programa em Python3 que receba uma temperatura em Fahrenheit, calcule e imprima o valor convertido para a 
# escala Celsius e para a escala Kelvin, de acordo com as equações de conversão abaixo:
#t_celsius = (t_fahrenheit - 32) * 5/9
#t_kelvin = t_celsius + 273.15

#Entrada/Input
t_fahrenheit = float(input())
t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15

#Processsamento/Processing

#Saída/Output

print('''Convertendo {}°F temos:
{} °C e {} K'''.format(t_fahrenheit, t_celsius, t_kelvin))