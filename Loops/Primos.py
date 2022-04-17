cont = 0
n = int(input('Digite um número: '))
for i in range(2, n):
    if n%2==0:
        cont+=1
if cont == 0:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))
