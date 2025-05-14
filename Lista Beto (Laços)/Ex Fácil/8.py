'''
Exercício 8 - Série Incremental
Faça um programa que imprima a seguinte série incremental, com base num valor n:
Exemplo:
Entrada: 5
Saída:
1
12
123
1234
12345
'''

num = int(input('Digite o número final: '))

for i in range(num + 2):
    for j in range(1, i):
        print(j, end=' ')
    print(' ')