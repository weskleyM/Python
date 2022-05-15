# # A LISTA RECEBE 5 VALORES E RETORNA O MAIOR E MENOR VALOR COM SUA RESPECTIVA POSIÇÃO
# lista = []
# maior = 0
# menor = 0
# for i in range(5):
#     lista.append(int(input('Digite um valor: ')))
#     if i == 0:
#         maior = lista[i]
#         menor = lista[i]
#     else:
#         if lista[i] > maior:
#             maior = lista[i]
#         if lista[i] < menor:
#             menor = lista[i]
# print(lista)
# # OU PODERIA SER maior = max(lista)
# # OU PODERIA SER menor = min(lista)
# print(f'O maior é {maior} nas posições: ', end='')
# for i, v in enumerate(lista):
#     if v == maior:
#         print(f'#{i+1} ', end='')
# print(f'\nO menor é {menor} nas posições: ', end='')
# for i, v in enumerate(lista):
#     if v == menor:
#         print(f'#{i+1} ', end='')
# print()

# # RECEBE VALORES DE ACORDO COM A VONTADE DO USUÁRIO
# lista = []
# while True:
#     n = int(input('digite um número: '))
#     if n not in lista:
#         lista.append(n)
#         print('Número salvo!')
#     else:
#         print('Número já utilizado!')
#     resp = input('Deseja continuar? [S/N]').strip().upper()
#     while resp not in 'SN':
#         print('opção inválida!')
#         resp = input('Deseja continuar? [S/N]').strip().upper()
#     if resp in 'S':
#         continue
#     elif resp in 'N':
#         break
# lista.sort()
# print(lista)

# # INSERINDO E ORGANIZANDO AO MESMO TEMPO ELEMENTOS NA LISTA
# lista = []
# for i in range(5):
#     n = int(input('Digite um número: '))
#     if i == 0:
#         lista.append(n)
#     else:
#         while n in lista:
#             print('Número já inserido!')
#             n = int(input('Digite um número: '))
#     if n > lista[len(lista)-1]:
#         lista.append(n)
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n < lista[pos]:
#                 lista.insert(pos, n)
#                 break
#             pos += 1
# print(lista)

# # RECEBE N VALORES E RETORNA UMA LISTA COM OS VALORES DIGITADOS E OUTRAS 2 LISTAS COM OS MESMOS SEPARADOS POR PAR E IMPAR
# lista = []
# pares = []
# impares = []
# while True:
#     while True:
#         n = int(input('Digite um número: '))
#         if n in lista:
#             print('Número já está na lista!')
#         else:
#             lista.append(n)
#             # OUTRO MODO PARA SEPARAR EM PAR E IMPAR
#             # if n % 2 == 0:
#             #     pares.append(n)
#             # else:
#             #     impares.append(n)
#             break
#     r = input('Deseja continuar?[S/N] ').strip().upper()
#     while r not in 'SN':
#         print('Opção Inválida!')
#         r = input('Deseja continuar?[S/N] ').strip().upper()
#     match r:
#         case 'S':
#             continue
#         case 'N':
#             break
# print(f'Sua lista: {lista}')
# for i, v in enumerate(lista):
#     if v % 2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)
# print(f'Números pares: {pares}')
# print(f'Números ímpares: {impares}')

# # CADASTRA N PESSOAS/PESOS E RETORNA A QUANTIDADE DE PESSOAS CADASTRADAS, QUAL A(S) MAIS PESADAS E MAIS LEVES ENTRE ELAS
# pessoa = list()
# lista = list()
# maior = menor = 0
# while True:
#     pessoa.append(input('Nome: ').strip().capitalize())
#     pessoa.append(float(input('Peso: ')))
#     lista.append(pessoa[:])
#     if len(lista) == 1:
#         maior = menor = pessoa[1]
#     else:
#         if pessoa[1] > maior:
#             maior = pessoa[1]
#         if pessoa[1] < menor:
#             menor = pessoa[1]
#     pessoa.clear()
#     r = input('Deseja continuar?[S/N] ').strip().upper()
#     while r not in 'SN':
#         print('Opção Inválida!')
#         r = input('Deseja continuar?[S/N] ').strip().upper()
#     match r:
#         case 'S':
#             continue
#         case 'N':
#             break
# # print(lista)
# print(f'Foram cadastradas {len(lista)} pessoas!')
# print('O mais pesado é ', end='')
# for p in lista:
#     if p[1] == maior:
#         print(f'{p[0]}, ', end='')
# print(f'com: {maior:.2f}kg')
# print('O mais leve é ', end='')
# for l in lista:
#     if l[1] == menor:
#         print(f'{l[0]}, ', end='')
# print(f'com: {menor:.2f}kg')

# # NUMEROS PARES E ÍMPARES V2.0 EM ORDEM DECRESCENTE
# lista = [[],[]]
# num = 0
# for i in range(8):
#     num = int(input(f'Digite o {i+1}º número: '))
#     if num % 2 == 0:
#         lista[0].append(num)
#     else:
#         lista[1].append(num)
# lista[1].sort(reverse=True)
# print(f'O número pares são: {sorted(lista[0], reverse=True)}')
# print(f'Os números ímpares são: {lista[1]}')

# # PREENCHE UMA MATRIZ, SOMA SEUS ELEMENTOS PARES E SOMA A ULTIMA COLUNA
# matriz = []
# elem = []
# soma = soma_col = 0
# for l in range(3):
#     for c in range(3):
#         elem.append(int(input(f'Digite N{l,c}: ')))
#     matriz.append(elem[:])
#     elem.clear()
# for m in range(len(matriz)):
#     for n in range(len(matriz)):
#         print(f'{matriz[m][n]} ', end='')
#         if matriz[m][n] % 2 == 0:
#             soma += matriz[m][n]
#     print()
# print(f'A soma dos pares é: {soma}')
# for i in range(len(matriz)):
#     soma_col += matriz[i][2]
# print(f'A soma da 3ª coluna é: {soma_col}')

# # GERA 6 NUMEROS ALEATÓRIOS N VEZES; EXEMPLO: JOGOS DE LOTERIA
# from random import randint
# from time import sleep

# lista = list()
# jogos = list()
# total = 0
# qtd = int(input(f'Quantos jogos você deseja gerar? '))
# while total < qtd:
#     cont = 0
#     while cont < 6:
#         n = randint(1, 60)
#         if n not in lista:
#             lista.append(n)
#             cont += 1
#     total += 1
#     jogos.append(lista[:])
#     lista.clear()
# print('PROCESSANDO...')
# for i, l in enumerate(jogos):
#     sleep(1)
#     print(f'Jogo #{i+1}: {sorted(l)}')

# # GERA UMA LISTA COMPOSTA COM DADOS DE UM ALUNO[NOME, NOTA#1, NOTA#2, MÉDIA] E RETORNA UM BOLETIM DE TODOS ALUNOS CADASTRADOS
# aluno = list()
# turma = list()
# while True:
#     aluno.append(input('Nome: ').strip().capitalize())
#     aluno.append(float(input('Nota 1: ')))
#     aluno.append(float(input('Nota 2: ')))
#     media = (aluno[1]+aluno[2])/2
#     aluno.append(media)
#     turma.append(aluno[:])
#     aluno.clear()
#     r = input('Deseja continuar?[S/N] ').strip().upper()
#     while r not in 'SN':
#         print('Opção inválida!')
#         r = input('Deseja continuar?[S/N] ').strip().upper()
#     match r:
#         case 'S':
#             continue
#         case 'N':
#             break
# # print(turma)
# print(f'\n{"No.":<4}{"Nome":<10}{"Média":>8}')
# for i, v in enumerate(turma):
#     print(f'{i+1:<4}{v[0]:<10}{v[3]:>8}')
# while True:
#     n = input('\nQual aluno você deseja ver as notas: ').strip().capitalize()
#     for j, a in enumerate(turma):
#         if n in a[0]:
#             print(f'Nota #1: {a[1]}')
#             print(f'Nota #2: {a[2]}')
#     r = input('Deseja continuar?[S/N] ').strip().upper()
#     while r not in 'SN':
#         print('Opção inválida!')
#         r = input('Deseja continuar?[S/N] ').strip().upper()
#     match r:
#         case 'S':
#             continue
#         case 'N':
#             break
