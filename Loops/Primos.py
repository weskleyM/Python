cont = 0
n = int(input('Digite um número: '))
for i in range(1, n+1):
    if n%i==0:
        print('\033[32m', end='')
        cont+=1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
if cont == 2:
    print('\n\033[mO número {} é primo!'.format(n))
else:
    print('\n\033[mO número {} não é primo!'.format(n))
