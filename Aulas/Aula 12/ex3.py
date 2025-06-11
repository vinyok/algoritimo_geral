'''
somar os quadrados dos numeros que são multiplos de 3

'''
from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10)]

resultado = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numeros)))

print(resultado)