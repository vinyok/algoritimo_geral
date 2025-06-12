'''

calcular o produto dos numeros pares apos multiplicar por 2


'''
from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10)]

resultado = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numeros)))

print(resultado)