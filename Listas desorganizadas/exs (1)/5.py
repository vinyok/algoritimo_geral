'''
Exercício 5 - Somatório dos Ímpares
Faça um programa que some apenas os números ímpares até um número inteiro positivo informado pelo usuário usando laços.
'''

n1 = int(input('Digite até onde será a somatória dos ímpares: '))
soma = 0

for n in range(1, n1 + 1):
    if n % 2 > 0:
        soma = n + soma
print(soma)
