from random import randint

cont = 1
pc = randint(1, 11)
j = int(input('Digite um número de 1 a 5: '))

while j != pc:
    if j > pc:
        print('Quase...um pouco abaixo!')
        j = int(input('Tente novamente: '))
    elif j < pc:
        print('Quase...um pouco acima!')
        j = int(input('Tente novamente: '))
    cont += 1
print('Parabéns! Você adivinhou o número em {} tentativas'.format(cont))
