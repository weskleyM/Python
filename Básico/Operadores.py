n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
rq = n1 ** (1/2)
rc = n1 ** (1/3)
print('A soma entre {} e {} é {}'.format(n1, n2, s))
print('A subtração entre {} e {} é {}'.format(n1, n2, su))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
print('A divisão entre {} e {} é {}'.format(n1, n2, d))
print('A divisão inteira entre {} e {} é {}'.format(n1, n2, di))
print('O resto da divisão entre {} e {} é {}'.format(n1, n2, r))
print('{} elevado a {} é {}'.format(n1, n2, e))
print('A raíz quadrada de {} é {}'.format(n1, rq))
print('A raíz cúbica de {} é {}'.format(n1, rc))
