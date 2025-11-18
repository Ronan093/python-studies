print('Bem vindo a calculadora de parcelas!')
valor = float(input(f'Qual é o valor do imóvel R$:'))
salario = float(input('Qual é o seu salário R$:'))
tempo = int(input('Em quantos anos deseja pagar?'))
prestacao = (valor /tempo) / 12
from time import sleep
print('Calculando valor da prestação...')
sleep(2)
print(f'O valor da parcela é R$: {prestacao:.2f}')
if prestacao > salario * 30/100:
    print('Crédito \033[1;31mnegado\033[m. O valor da parcela excede 30% do seu salário')
else:
    print('Crédito \033[1;32mconcedido\033[m. Parabéns!')

