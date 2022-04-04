from random import randint
from time import sleep

n = randint(0, 5)  # Gera um valor entre 0 e 5
print('Em que número estou pensando entre 0 a 5?')
m = int(input('Digite aqui: '))
print('Processando...')
sleep(2)  # Espera por n segundos para dar sequência ao código
print('Eu pensei no número: {}'.format(n))
if m == n:  # Se m for igual a n
    print('Parabéns! Você acertou!')
else:  # Se m não for igual a n
    print('Você errou!')
