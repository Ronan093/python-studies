d=int(input('Por quantos dias o carro foi alugado?'))
km=float(input('Quantos km foram percorridos?'))
m=(d * 60) + (km * 0.15)
print(f'O valor a pagar é: R$ {m:.2f}')
