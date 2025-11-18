from time import sleep
v = float(input('Digite a velocidade:'))
if v > 80:
    print('Você ultrapassou o limite de velocidade.')
    print('CALCULANDO MULTA...')
    sleep(2)
    multa = (v - 80) * 7
    print(f'Valor a pagar R$: {multa:.2f}')
else:
    print('Você está dentro do limite de velocidade. Boa viagem!')
