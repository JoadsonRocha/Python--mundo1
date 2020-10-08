#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temp = float(input('Qual a temperatura C: '))
#f = ((9 * temp) / 5) + 32
f = 9 * temp / 5 + 32
print('A temperatura de {}ºC corresponde a {}F!'.format(temp, f))
