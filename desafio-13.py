#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual seu Salário Atual R$: '))
novo = sal + (sal * 15 / 100)
print('Seu Salário Atual é: {:.2f} e com Aumento fica: {:.2f}'.format(sal, novo))