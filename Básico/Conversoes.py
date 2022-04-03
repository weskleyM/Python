# Conversão de moedas
real = float(input('Digite um valor: R$'))
dolar = real / 4.66
euro = real / 5.15
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))

# Conversão de temperaturas
c = float(input('\nDigite a temperatura(ºC): '))
f = (9 * c / 5) + 32
print('{}ºC corresponde a {}ºF'.format(c, f))
