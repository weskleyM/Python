# Calculando área de um cômodo quadrado
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2  # 1l de tinta pinta 2m² de area
print('\nO cômodo tem {:.2f}m² e irá gastar {:.2f}l de tinta para ser pintado.'.format(area, tinta))
