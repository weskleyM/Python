# TUDO EM MAIÚSCULO, ELIMINA ESPAÇOS EXTERNOS
frase = input('Digite algo: ').upper().strip()
# SEPARA CADA PALAVRA
separar = frase.split()
# ELIMINA ESPAÇOS INTERNOS
juntar = ''.join(separar)
inverter = ''
# INVERTE TODA FRASE
for i in range(len(juntar)-1, -1, -1):
    inverter += juntar[i]
print(inverter, end='')
# COMPARA E RETORNA O RESULTADO
if inverter == juntar:
    print('\n{} É um palíndromo'.format(juntar))
else:
    print('\n{} Não é um palíndromo'.format(juntar))
