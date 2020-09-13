larg = float(input('Qual O valor da Largura: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt
print('Sua parede mede {}X{} e sua area é de {}m2.'.format(larg, alt, area))
tnt = area / 2
print('Para pintar essa parede, voce vai precisar de {:.0f} Litros de tinta'.format(tnt))