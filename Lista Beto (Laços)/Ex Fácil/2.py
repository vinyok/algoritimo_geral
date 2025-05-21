'''
Exercício 2 - Tabela de Multiplicação
Faça um programa que exiba a tabuada de multiplicação do número fornecido pelo usuário
(de 1 a 10).
'''
num = int(input('Digite qual número deseja saber a tabuada até 10: '))
tabuada = int(1)

for i in range(1,11):
    tabuada = num * i
    print(tabuada)