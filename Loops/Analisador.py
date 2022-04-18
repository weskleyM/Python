maior, menor, mulher, homem, cont, media = 0, 0, 0, 0, 0, 0
idoso, jovem = '', ''

for i in range(3):
    print('---- {}º Pessoa ----'.format(i+1))
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    if i == 0:
        maior = idade
        menor = idade
        idoso = nome
        jovem = nome
        cont += 1
        media = idade
        if sexo == 'M':
            homem += 1
        elif sexo == 'F':
            mulher += 1
    else:
        if idade > maior:
            maior = idade
            idoso = nome
        elif idade < menor:
            menor = idade
            jovem = nome
        if sexo == 'M':
            homem += 1
        elif sexo == 'F':
            mulher += 1
        cont += 1
        media += idade
media //= cont

print('\nA média entre as idades é: {}'.format(media))
print('O mais velho tem {} anos e se chama {}'.format(maior, idoso))
print('O mais novo tem {} anos e se chama {}'.format(menor, jovem))
print('Foram cadastrados {} Mulheres e {} Homens'.format(mulher, homem))
