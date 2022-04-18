# 10 Termos de uma Progressão Aritmética
n = int(input('Digite o termo inicial: '))
p = int(input('Digite a razão: '))
for i in range(10):
    pa = n + i * p
    print('{}'.format(pa), end=' - ')
print('Fim!\n')
