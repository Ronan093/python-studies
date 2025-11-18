import random
n1= str(input('Digite o nome do primeiro aluno:'))
n2= str(input('Digite o segundo aluno:'))
n3= str(input('Digite o terceiro aluno:'))
n4= str(input('Digite o quarto aluno:'))
lista =[n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem do sorteio será: {lista}')


