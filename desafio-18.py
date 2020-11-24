#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite o Angulo qu e voce quer: '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o Sena {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tan = math.tan(math.radians(an))
print('O angulo de {} tem a Tangente de {:.2f}'.format(an, tan))