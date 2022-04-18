aux = 0
cont = 0
for i in range(1, 501, 2):
    if i%3==0:
        aux += i
        cont += 1
print('\nForam encontrados {} números ímpares múltiplos de 3 de 1 a 500!'.format(cont))
print('A soma desses números é: {}\n'.format(aux))
