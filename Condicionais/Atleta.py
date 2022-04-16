from datetime import date

hoje = date.today().year
ano = int(input('Ano de nascimento: '))
idade = hoje - ano
print('O atleta tem {} anos'.format(idade))
if 3 <= idade <= 9:
    c = 'Mirim'    
    print('Está classificado como {}'.format(c))
elif idade <= 14:
    c = 'Infantil'
    print('Está classificado como {}'.format(c))
elif idade <= 19:
    c = 'Junior'
    print('Está classificado como {}'.format(c))
elif idade <= 25:
    c = 'Sênior'
    print('Está classificado como {}'.format(c))
elif idade > 25:
    c = 'Master'
    print('Está classificado como {}'.format(c))
else:
    print('O atleta tem {} ano(s), ainda não pode competir!'.format(idade))
