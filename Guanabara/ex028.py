from random import randint
from time import sleep
pc = randint(0,5)#pc sorteia
print('***' *19)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('***' *19)
player = int(input('Em que número eu pensei?'))#player tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if player == pc:
    print(f'Parabéns! Eu pensei no número {player}. Você é fera!')
else:
    print(f'Não foi dessa vez. Eu pensei no número {pc}. Tente de novo!')



