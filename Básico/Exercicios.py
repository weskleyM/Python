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
print('A média entre {} e {} é {:.2f}\n'.format(n1, n2, media))
# Conversão de valores métricos
var2 = float(input('Digite um valor em metros: '))
km = var2 * 1000
hm = var2 * 100
dam = var2 * 10
dm = var2 / 10
cm = var2 / 100
mm = var2 / 1000
print('{} metro(s) em quilômetros é {:.0f}'.format(var2, km))
print('{} metro(s) em hectômetros é {:.0f}'.format(var2, hm))
print('{} metro(s) em decâmetros é {:.0f}'.format(var2, dam))
print('{} metro(s) em decímetros é {}'.format(var2, dm))
print('{} metro(s) em centímetros é {}'.format(var2, cm))
print('{} metro(s) em milímetros é {}'.format(var2, mm))
