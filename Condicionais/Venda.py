# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valor = float(input('digite o valor a ser pago: (R$)'))
print('=' * 40)
print('''[1] À vista em dinheiro
[2] À vista no cartão
[3] Parcelado em 2x
[4] Parcelado em 3x ou mais''')
print('=' * 40)
op = int(input('\nSelecione uma das opções acima: '))

if op == 1:
    vistaD = valor - valor * 10 / 100
    print('\nTotal dinheiro à vista com 10% de desconto: R${:.2f}'.format(vistaD))
elif op == 2:
    vistaC = valor - valor * 5 / 100
    print('\nTotal cartão à vista com 5% de desconto: R${:.2f}'.format(vistaC))
elif op == 3:
    parc_2 = valor / 2
    print('\nParcelado em 2x sem juros: R${:.2f}'.format(parc_2))
    print('Total a prazo: R${:.2f}'.format(parc_2*2))
elif op == 4:
    n = int(input('Número de parcelas: '))
    aux = (valor / n)
    parc_N = aux + aux * 20 / 100
    print('\nParcelado em {}x com 20% de juros: R${:.2f}'.format(n, parc_N))
    print('Total a prazo: R${:.2f}'.format(parc_N*n))
else:
    print('\nOpção inválida!')
