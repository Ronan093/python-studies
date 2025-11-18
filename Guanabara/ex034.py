salario = float(input('Digite seu sálario R$:'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Calculando o reajuste...')
    print(f'Seu novo salário com aumento de 15% é R$: {novo:.2f}')
else:
    novo = salario + (salario * 10 / 100)
    print('Calculando o reajuste...')
    print(f'Seu novo salário com aumento de 10% é R$: {novo:.2f}')
