# Compara a primeira palavra
var = input('Em qual cidade você nasceu? ').strip()
x = var.lower()
print('Esta cidade começa com "Santo"? {}'.format(x[:5] == 'santo'))

# Compara em toda cadeia
nome = input('\nDigite seu nome completo: ').strip().lower()
# y = nome.lower()
print('Seu nome tem "Silva"? {}'.format('silva' in nome))

# Busca em toda cadeia
frase = input('\nDigite uma frase: ').strip()
z = frase.lower()
print('A letra "a" aparece: {} vezes'.format(z.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(z.find('a') + 1))
print('A última letra "a" aparece na posição {}'.format(z.rfind('a') + 1))

# Busca a primeira e última palavra em uma cadeia
nome2 = input('Digite seu nome completo: ').strip().title().split()
print('Seu primeiro nome é: {}'.format(nome2[0]))
print('Seu último nome é: {}'.format(nome2[len(nome2)-1]))
