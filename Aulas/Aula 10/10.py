'''
Lambda function


sintaxe:

lambda argumentos: expressão


usar quando é bem curto o codigo
'''

dobro = lambda x: x * 2

print('Exemplo - 1 Dobro de 5: ', dobro(5))

soma = lambda x, y: x + y

print('A soma foi: ', soma(3, 4))

hipotenusa = lambda c1, c2: (c1 ** 2 + c2 ** 2) ** 0.5

print('A hipotenusa é: ', hipotenusa(3, 4))


'''
FUNÇÕES FODAS:

filter, map

'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = list(filter(lambda x: x % 2 == 0, numeros))
print('Ex 3 - Numeros pares: ', pares)

quadrado = list(map(lambda x: x ** 2 ,numeros))

# sorted (pessoas, key = lambda x: x[1])
pessoas = [('Ana', 19) ('Joao', 30), ('Maria', 20)]


import random


'''
COMPREENSÃO DE LISTA ESTUDAR
'''


a = [random.randit(20, 100) for _ in range(100)]

maior_60 = []
a.append(maior_60)
print(maior_60)
