from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=' * 15)
print(f'O computador escolheu: {itens[pc]}')
print(f'O jogador escolheu: {itens[j]}')
print('-=' * 15)
if pc == 0:     #PC JOGOU PEDRA
   if j == 0:
       print('EMPATE')
   elif j == 1:
       print('jogador venceu!')
   elif j == 2:
       print('computador venceu!')
   else:
       print('comando inválido')
elif pc == 1:   #PC JOGOU PAPEL
    if j == 0:
        print('computador venceu!')
    elif j == 1:
        print('EMPATE!')
    elif j == 2:
        print('Jogador venceu!')
    else:
        print('comando inválido')

elif pc == 2:   #PC JOGOU TESOURA
    if j == 0:
        print('Jogador venceu!')
    elif j == 1:
        print('computador venceu!')
    elif j == 2:
        print('EMPATE!')
    else:
        print('comando inválido')




