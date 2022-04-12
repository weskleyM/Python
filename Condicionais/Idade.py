# Recebe um ano de nascimento, retorna a idade e situação de alistamento militar
from datetime import date

print('='*30)
print('verifique sua situação de alistamento militar')
print('='*30)
print('[1] Homem')
print('[2] Mulher')
opcao = int(input('Escolha uma das opções acima: '))
if opcao == 1:
    ano = int(input('Digite o ano em que você nesceu: '))
    hoje = date.today().year  # recebe o ano atual do S.O.
    idade = hoje - ano

    if idade < 18:
        menor = 18 - idade
        print('\nVocê tem {} anos, ainda resta {} anos para se alistar!'.format(idade, menor))
    elif idade > 18:
        maior = idade - 18
        print('\nVocê tem {} anos, está atrasado {} ano(s) para se alistar!'.format(idade, maior))
    else:
        print('\nVocê tem {} anos, deve se alistar neste ano!'.format(idade))
elif opcao == 2:
    print('\nSeu alistamento não é obrigatório')
else:
    print('\nOpção inválida!')
