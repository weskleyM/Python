from random import randint

cont = 1
pc = randint(1, 15)
j = int(input('Digite um número de 1 a 15: '))

while j != pc:
    j = int(input('Tente novamente: '))
    cont += 1
print('Parabéns! Você adivinhou o número em {} tentativas'.format(cont))
