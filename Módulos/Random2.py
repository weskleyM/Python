from random import shuffle

# Escolhe e organiza aleatóriamente valores de uma lista
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem fica:')
print(lista)
