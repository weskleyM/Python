from math import trunc

# Separa a parte inteira de um número
var = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(var, trunc(var)))  # Ou int(var)
