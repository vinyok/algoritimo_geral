'''
NÍVEL MÉDIO
Exercício 1: Contagem de Vogais em uma Frase
Crie um programa usando laços que receba uma frase do usuário e retorne quantas vogais
há nessa frase.
'''
frase = str(input('Digite uma frase: ')).lower()
vogs = 'aeiou'
somav = 0

for l in frase:
    if l in vogs:
        somav = somav + 1
        print (somav)