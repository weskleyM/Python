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
