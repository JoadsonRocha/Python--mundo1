#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import ceil
nu= float(input('digite um numero: '))
inteiro = ceil(nu)
print('O numero {} e o seu real é: {}'.format(nu, inteiro))

