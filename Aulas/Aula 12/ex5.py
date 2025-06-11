'''
encontrar a media dos numeros que sao maiores que 5 apos elevar ao quadrado

'''
from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10)]

resultado = reduce(lambda x, y: x + y, filter(lambda x: x > 5, map(lambda x: x ** 2, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))