'''
Exercício 6 - Fatorial Simples
Faça um programa que calcule o fatorial de um número inteiro positivo usando apenas
laços.
'''

n1 = int(input('Digite o valor do número que deseja saber o fatorial: '))
fat = 1

for n in range(n1, 1, -1):
    fat = n * fat
print (fat)