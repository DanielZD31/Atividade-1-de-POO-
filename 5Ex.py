#Aluno: Daniel Alves de Sousa
#Professor: Leandro Rodrigues da Silva Souza

"""

5) Exercício 

Faça um programa que peça ao usuário para digitar um número inteiro,

informe se este número é par ou ímpar. Caso o usuário não digite um número

inteiro, informe que não é um número inteiro.

"""

#Usuário vai digitar um número inteiro

número = int (input('Digite um número inteiro qualquer: '))

#Fazer a divisão do número escolhido pelo usuário, se 
# o resultado dividido for igual a 1 esse número vai ser ímpar 
# se o resultado for 0 esse número é par!

resultado = número %2

#============================================================#

if resultado == 0:
    print('O número {} é Par'.format(número))
else:
    print('O número {} é Ímpar'.format(número))

#=============================================================#
numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
else:
    print('Isso não é um número inteiro')