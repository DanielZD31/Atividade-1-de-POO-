#Aluno: Daniel Alves de Sousa
#Professor: Leandro Rodrigues da Silva Souza

"""

7) Exercício 

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 

menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 

"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

#Solicitar que o usuário escreva seu nome inicial ou completo.
nome = input ('Digite o seu nome primeiro nome ou o nome completo: ')
nome = len(nome)

#Funções para saber se o nome do usuário é curto, normal ou muito grande.

if nome <= 4:
    print('Seu nome é curto')
elif nome == 5 or nome == 6:
    print('Seu nome é normal')
elif nome >6:
    print('Seu nome é muito grande')