vel = float(input('Digite uma velocidade(km/h): '))
lim = 80
if vel > lim:
    exc = vel - lim
    multa = exc * 7  # R$7.00 por cada 1km acima
    print('Você está {:.2f}km/h acima do limite!'
          '\nMulta: R${:.2f}'.format(exc, multa))
print('Dirija com cuidado!')
