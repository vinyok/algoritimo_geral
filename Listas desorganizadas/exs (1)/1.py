'''

Exercício 1 - Soma dos números inteiros
Faça um programa usando laços que some todos os números inteiros de 1 até n fornecido
pelo usuário.
Exemplo:
Entrada: 5
Saída: 15

'''
soma = 0
num = int(input('Digite o valor do número: '))
if num <= 0:
    print('Valor inválido. O valor deve ser um número inteiro positivo. ')
    
else:
    for i in range(1, num + 1):
        soma = i + soma
    print(soma)

