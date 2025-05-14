'''
Exercício 1: Contagem de Vogais em uma Frase

Crie um programa usando laços que receba uma frase do usuário e retorne quantas vogais
há nessa frase.
'''

frase = str(input('Digite uma frase: ')).lower()
vogais = 'aeiou'
contador = 0

for letra in frase:
    if letra in vogais:
        contador = contador + 1
print(f' O número de vogais é: {contador}')