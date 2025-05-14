'''
Exercício 4 - Números Pares até N
Crie um programa que imprima todos os números pares até o número fornecido pelo usuário usando laços
'''
numfinal = int(input('Digite o número final: '))

for n in range(0, numfinal + 1):
    if n % 2 == 0:
        print(n)