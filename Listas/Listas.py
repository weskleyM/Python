from operator import index


lista = []
for i in range(5):
    n = int(input(f'Digite N{i+1}: '))
    lista.append(n)
print(lista)
maior = max(lista)
menor = min(lista)
print(f'O maior é: {maior} na posição: {lista.index(maior)+1}')
print(f'O menor é: {menor} na posição: {lista.index(menor)+1}')
