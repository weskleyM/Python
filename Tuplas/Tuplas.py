from random import randint

# # RECEBE UM NÚMERO E RETORNA O MESMO POR EXTENSO DE ACORDO COM A TUPLA
# num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
# while True:
#     n = int(input('Digite um número entre 0 e 5: '))
#     if 0 <= n <= 5:
#         break
#     print('** Número Inválido **')
# print(f'Você escolheu o número {num[n]}')

# # FATIANDO UMA TUPLA
# time = ('Flamengo', 'Botafogo', 'Fluminense', 'Vasco', 'Madureira')
# print(f'Tabela: {time}')
# print('='*50)
# print('Os 2 primeiros são: ', end='')
# print(f'{time[:2]}')
# print('='*50)
# print('Os 2 últimos são: ', end='')
# print(f'{time[-2:]}')
# print('='*50)
# print('Os time em ordem alfabética: ', end='')
# print(f'{sorted(time)}')
# print('='*50)
# pos = input('Escolha um time: ').capitalize()
# print(f'O {pos} está na {time.index(pos)+1}ª posição')

# # GERA 5 NÚMEROS ALEATÓRIOS EM UMA TUPLA E RETORNA O MAIOR E MENOR ENTRE ELES
# num = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
# print('Os números sorteados foram: ', end='')
# for n in num:
#     print(f'{n} ', end='')
# print(f'\nO maior número é: {max(num)}')
# print(f'O maior número é: {min(num)}')
