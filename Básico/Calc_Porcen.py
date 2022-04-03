# Desconto em porcentagem
valor = float(input('Digite um valor: R$'))
pc = int(input('Digite o valor do desconto(%): '))
desc = valor - (valor * pc / 100)
print('Valor real R${:.2f}, com desconto de {}% R${:.2f}'.format(valor, pc, desc))

# Aumento em porcentagem
salario = float(input('\nDigite um valor: R$'))
x = int(input('Digite o valor do aumento(%): '))
aumento = salario + (salario * x / 100)
print('Salário de R${:.2f}, com aumento de {}% fica R${:.2f}'.format(salario, x, aumento))

# Exercicio - Aluguel de carros
km = float(input('\nDigite KM rodados: '))
dia = int(input('Digite a qtd de dias alugados: '))
calcKM = km * 0.15  # R$0,15 por km
calcD = dia * 60  # R$60,00 por dia
total = calcD + calcKM
print('O total a receber por {:.2f}km rodados e {} dias alugados é R${:.2f}'.format(km, dia, total))
