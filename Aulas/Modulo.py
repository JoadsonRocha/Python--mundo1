#print('Aulas de Modulos')
#import math #Importa todo o modulo
#from math import sqrt #Apenas partes do modulo

#import emoji
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a: {}'.format(num, floor(raiz)))
#print ('A Raiz de {} é igual a {}'.format(num, math.ceil(raiz)))