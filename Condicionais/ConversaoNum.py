# Recebe um número inteiro e retorna convertido em Binário ou Octal ou Hexadecimal
num = int(input('Digite um número: '))

print('=' * 30)
print('[1] Converter {} para Binário\n'
      '[2] Converter {} para Octal\n'
      '[3] Converter {} para Hexa'.format(num, num, num))
print('=' * 30)

opcao = int(input('Escolha uma das opções acima: '))

if opcao == 1:
    print('\nO número {} em binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\nO número {} em octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\nO número {} em hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('\nOpção inválida')
