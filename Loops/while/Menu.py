op = 1

n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))

while 0 < op < 6:
    print('\n[1] SOMAR\n'
        '[2] SUBTRAIR\n'
        '[3] MULTIPLICAR\n'
        '[4] DIVIDIR\n'
        '[5] NOVOS\n'
        '[0] SAIR\n')
    op = int(input('Escolha uma das opções acima: '))
    
    if op == 1:
        soma = n1 + n2
        print('\n{} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        sub = n1 - n2
        print('\n{} - {} = {}'.format(n1, n2, sub))
    elif op == 3:
        mult = n1 * n2
        print('\n{} x {} = {}'.format(n1, n2, mult))
    elif op == 4:
        div = n1 / n2
        print('\n{} / {} = {}'.format(n1, n2, div))
    elif op == 5:
        n1 = int(input('Digite N1: '))
        n2 = int(input('Digite N2: '))
