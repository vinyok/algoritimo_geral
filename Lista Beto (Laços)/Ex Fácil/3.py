'''
Exercício 3 - Contagem Regressiva
Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição.
'''

n1 = int(input('Digite o valor de onde irá começar a contagem: '))

for i in range(n1, 0, -1):
    print(i)