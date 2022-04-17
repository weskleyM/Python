from random import randint
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
print('\n[1] Pedra'
      '\n[2] Papel'
      '\n[3] Tesoura')

pc = randint(1, 3)
player = int(input('\nEscolha uma das opções acima: '))

print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')

print('\nComputador escolheu: {}'.format(lista[pc-1].upper()))
print('Você escolheu:       {}'.format(lista[player-1].upper()))

if player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2:
    print('\nVocê VENCEU!')
elif pc == player:
    print('\nEMPATOU!')
else:
    print('\nComputador VENCEU')
