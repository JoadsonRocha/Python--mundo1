preco = float(input('Qual o preço do produto R$: '))
novo = preco - (preco * 5 / 100)
print('O produto que Custava {:.2f}, com desconto custa {:.2f}'.format(preco, novo))