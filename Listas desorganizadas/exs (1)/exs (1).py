'''
Exercício 1 - Soma dos números inteiros
Faça um programa usando laços que some todos os números inteiros de 1 até n fornecido
pelo usuário.
Exemplo:
Entrada: 5
Saída: 15
'''

numero = int(input('Digite o número até onde somar: '))

soma = 0

for i in range(1,numero + 1):
    soma = i + soma
    print(soma)



'''
Exercício 2 - Tabela de Multiplicação
Faça um programa que exiba a tabuada de multiplicação do número fornecido pelo usuário
(de 1 a 10).
'''

n1 = int(input('Digite o número que deseja ver a tabuada: '))

tabuada = 0

for n in range (1,11):
    tabuada = (n1 * n)
    print(tabuada)

'''
Exercício 3 - Contagem Regressiva
Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição.
'''


num = int(input('Digite o número que começa a contagem regressiva: '))

for a in range(num, -1, -1):
    print (a)

'''
Exercício 4 - Números Pares até N
Crie um programa que imprima todos os números pares até o número fornecido pelo
usuário usando laços.
'''

num4 = int(input('Digite o número onde termina a impressão dos pares: '))
par = 0

for quatro in range(1,num4 + 1):
    if quatro  % 2 == 0:
        print(quatro)

'''
Exercício 5 - Somatório dos Ímpares
Faça um programa que some apenas os números ímpares até um número inteiro positivo
informado pelo usuário usando laços.
'''

num5 = int(input('Digite o número onde termina a soma dos ímpares: '))
soma = 0


for cinco in range (1, num5 + 1):
    if cinco % 2 > 0:
        soma = soma + cinco
        print(soma)

