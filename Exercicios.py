# Sucessor e Antecessor de uma variável
var = int(input('Digite um número: '))
sucessor = var + 1
antecessor = var - 1
print('O antecessor de {} é {}'.format(var, antecessor))
print('O sucessor de {} é {}'.format(var, sucessor))
# Dobro, Triplo e Raíz quadrada de uma variável
dobro = var * 2
triplo = var * 3
raizQ = var ** (1 / 2)  # ou pow(n, (1/2))
print('O dobro de {} é {}'.format(var, dobro))
print('O triplo de {} é {}'.format(var, triplo))
print('A raíz quadrada de {} é {:.2f}\n'.format(var, raizQ))
# Média aritimética de 2 variáveis
n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
media = (n1+n2)/2
print('A média entre {} e {} é {:.2f}'.format(n1, n2, media))
