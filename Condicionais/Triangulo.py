print('=' * 20)
print('Formar um Triângulo')
print('=' * 20)
m1 = float(input('Medida 1: '))
m2 = float(input('Medida 2: '))
m3 = float(input('Medida 3: '))
# Para formar um triângulo cada valor deve ser menor que a soma dos outros dois
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('As três medidas \033[4;32mPODEM\033[m formar um triângulo!')
    if m1 == m2 == m3:
        print('É um triângulo equilátero')
else:
    print('As três medidas \033[4;31mNÃO PODEM\033[m formar um triângulo!')
