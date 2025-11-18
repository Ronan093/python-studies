print('Seja bem vindo. Vamos descobrir a área da sua parede e quantos litros de tinta você vai precisar para pinta-la!')
a=float(input('Digite altura:'))
l=float(input('Digite largura:'))
ar=a*l
print(f'Sua parede possui: {ar:.2f}m²')
li=(a*l) /2
print(f'Serão necessários {li:.2f}l de tinta.')
