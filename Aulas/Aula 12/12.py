'''

map = transformar
filter = filto de condição
reduce = reduz um iteravel a um unico valor

SINTAXE
reduce(func, array)


'''

from functools import reduce
from random import randint

numeros = [randint(1,50) for _ in range(10)]
# x é o valor acumulador, começa com 0 e vai subindo

soma_total = reduce(lambda x, y: x + y, numeros)
print(soma_total)
print(max(numeros))
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)


'''
calcular a media dos quadrados dos numeros pares de uma lista
'''

pares = list(filter(lambda x: x % 2 == 0, numeros)), list(map(lambda x: x ** 2, numeros))
print(pares)

oficial = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))

print(oficial)