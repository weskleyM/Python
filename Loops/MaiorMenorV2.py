maior = 0
menor = 0
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
print('\nO maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))
