n = int(input('Escolha um número: '))

print('-='*10)
print('Tabuada de {}'.format(n))
print('-='*10)
print('')
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))
print('\n')
