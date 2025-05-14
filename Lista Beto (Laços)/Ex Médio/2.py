'''
Exercício 2: Número Perfeito

Faça um programa usando apenas laços que determine se um número informado pelo
usuário é um número perfeito. Um número é perfeito quando é igual à soma dos seus
divisores próprios (exceto ele mesmo).
Exemplo:

Entrada: 6

Saída: Número Perfeito
Explicação: 6 → divisores: 1, 2, 3 (soma: 1+2+3=6)
'''

num = int(input('Digite um número para descobrir se é perfeito: '))
soma = 0

for i in range(1, num):
    if num % i == 0:
        soma += i
        if soma == num:
            print (f'O número {num} é um número perfeito. ')
            break
else:
    print(f'O número {num} não é um número perfeito. ')