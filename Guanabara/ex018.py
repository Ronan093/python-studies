import math
num = float(input('Digite o ângulo:'))
s=math.sin(math.radians(num))
c=math.cos(math.radians(num))
t=math.tan(math.radians(num))
print(f'Para o Valor: {num} temos:\nSeno: {s:.2f}\nCosse: {c:.2f}\nTangente: {t:.2f}')


