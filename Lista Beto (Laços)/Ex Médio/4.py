'''
Exercício 4: Triângulo Numérico Invertido

Faça um programa que, utilizando laços, imprima o seguinte padrão numérico invertido
baseado no número inteiro informado pelo usuário.

Exemplo:

Entrada: 5

Saída:
12345
1234
123
12
1
'''
nf = int(input('Digite o valor final do triângulo: ')) +1

for i in range(nf, 0, -1):
    for j in range(1, i):
        print (j, end=' ')
    print(' ')
