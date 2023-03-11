#Aluno: Daniel Alves de Sousa
#Professor: Leandro Rodrigues da Silva Souza

"""

6) Exercício 

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 

descrito, exiba a saudação apropriada. Ex. 

Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

#Pedir para o usuário digitar o horário atual!
hora = input('Digite o seu horário atual no  formato. (hh:mm): ')

#Separação da string hora em uma lista de 2 termos, cujo o 1º sempre será 'hh' e o 2º 'mm'.
x = hora.split(':')
h = x[0]
m = x[1]

if (int(h) < 0 or int(h) > 24) or (int(m) < 0 or int(m) > 59):
    print(f'O horário digitado {hora} está incorreto! Executa o programa novamente colocando um horário válido.')

#Código de verificação para saber se o horário informado é de manhã, tarde ou noite.
else:
    if int(h) >= 0 and int(h) <= 11:
        print('Bom dia!')
    elif int(h) >= 12 and int(h) <=17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
        