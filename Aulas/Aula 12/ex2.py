'''
Encontrar o maior numero impar apos elevar ao cubo

'''
from functools import reduce
from random import randint

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]

resultado = reduce(lambda x, y: x if x > y else y, map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, numeros)))
print(resultado)