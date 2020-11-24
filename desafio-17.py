# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#co = float(input('Cateto oposto: '))
#ca = float(input('Cateto Adjancente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {}'.format(hi))
from math import hypot
co = float(input('catetos opostos:'))
ca = float(input('catettos adjancentes: '))
hi = hypot(co, ca)
print('A Hipotenusa vai medir {}'.format(hi))