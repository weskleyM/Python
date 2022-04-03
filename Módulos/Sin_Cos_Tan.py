from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {}º é: {:.2f}\n'
      'O cosseno de {}º é: {:.2f}\n'
      'A tangente de {}º é: {:.2f}'.format(angulo, seno, angulo, cosseno, angulo, tangente))
