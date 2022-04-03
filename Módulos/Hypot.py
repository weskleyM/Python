from math import sqrt, hypot

# Calculando a hipotenusa de um triângulo
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = hypot(co, ca)  # ou hp = sqrt(co**2 + ca**2)
print('O valor da hipotenusa é {:.2f}'.format(hp))
