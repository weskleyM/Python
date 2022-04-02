real = float(input('Digite um valor: R$ '))
dolar = real / 4.66
euro = real / 5.15
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))
