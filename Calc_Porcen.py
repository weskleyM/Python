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
