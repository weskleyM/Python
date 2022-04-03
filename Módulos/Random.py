from random import choice

# Escolhe aleatóriamente um valor em uma lista
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
sortear = choice(lista)
print('O aluno sorteado foi: {}'.format(sortear))
