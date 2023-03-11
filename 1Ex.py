#Aluno: Daniel Alves de Sousa
#Professor: Leandro Rodrigues da Silva Souza

"""

1) Exercício 

Faça um jogo para o usuário adivinhar qual

a palavra secreta.

- Você vai propor uma palavra secreta

qualquer e vai dar a possibilidade para

o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 

vai conferir se a letra digitada está

na palavra secreta.

- Se a letra digitada estiver na
palavra secreta; exiba a letra;
- Se a letra digitada não estiver
na palavra secreta; exiba *.
Faça a contagem de tentativas do seu

usuário.

"""
#variáveis da atividade: secreto, digitadas e chances
secreto = 'espinafre'
digitadas = []
chances = 3

#Esqueleto do programa com as seguintes operações realizadas dentro do jogo da palavra secreta.
while True:
    if chances <=0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Boa!!! Você acertou.')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'A letra "{letra}" Não existe na palavra secreta ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você ganhou!! A palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

            print(f'Só resta {chances} chances.')
            

