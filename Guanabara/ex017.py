'''import math
#leia os catetos
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente:'))
#calcule a Hipotenusa
h=math.hypot(co,ca)
print(f'A hipotenusa mede: {h:.2f}')'''

from math import hypot
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente:'))
h= hypot(co,ca)
print(f'A hipotenusa mede: {h:.2f}')



