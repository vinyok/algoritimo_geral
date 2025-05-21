'''
Exercício 7 - Contar Divisores
Faça um programa que conte quantos divisores inteiros um número inteiro positivo possui
utilizando laços
'''

num = int(input('Digite o número final: '))
div = 0

for n in range(1, num +1):
    if num % n == 0:
        div = div + 1
print(div)