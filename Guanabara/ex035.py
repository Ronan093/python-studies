a = float(input('Digite a primeira medida do triângulo:'))
b = float(input('Digite a segunda medida do triângulo:'))
c = float(input('Digite a terceira medida do triangulo:'))
if a >= b+c or b >= a+c or c >= a+b:
    print('As medidas \033[1;31mNÃO FORMAM\033[m um triângulo')
else:
    print('As medidas \033[1;32mFORMAM\033[m um triângulo')
