'''

calcular o produto dos numeros pares apos multiplicar por 2


'''
from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10)]

resultado = map(lambda x: x ** 2, numeros * 2)

print(resultado)