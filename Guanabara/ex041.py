from datetime import date
atual =  date.today().year
print('Calculadora da CNN')
nasc = int(input('Digite o ano de nascimento do atleta:'))
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')