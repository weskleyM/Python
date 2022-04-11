casa = float(input('Digite o valor da casa: R$'))  # Recebe o valor de uma casa
salario = float(input('Digite seu salário: R$'))  # Recebe o valor do salário do usuário
anos = float(input('Em quantos anos deseja pagar? '))
mensalidade = casa / (anos * 12)
pc = (salario * 30) / 100  # 30% do salário
print('Parcelas: R${:.2f} por mês'.format(mensalidade))
if mensalidade > pc:
    print('Empréstimo negado! Parcelas excedem 30% do seu salário!')
else:
    print('Empréstimo aprovado!')
