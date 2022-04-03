# Separa por unidades um valor
var = int(input('Digite um número: '))
u = var // 1 % 10
d = var // 10 % 10
c = var // 100 % 10
m = var // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
