dist = float(input('Qual é a distância da viagem em KM?'))
if dist <= 200:
    print('calculando...')
    pre = dist * 0.50
    print(f'A passagem custará R$: {pre:.2f}')
else:
    print('calculando...')
    pre = dist * 0.45
    print(f'A passagem custará R$: {pre:.2f}')

