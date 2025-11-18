n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2) / 2
print(f'Média: {m}')
if m < 5.0:
    print('\033[1;31mREPROVADO')
elif 5.0 <= m < 7.0:
    print('\033[1;33mRECUPERAÇÃO')
elif m >= 7.0:
    print('\033[1;32mAPROVADO')