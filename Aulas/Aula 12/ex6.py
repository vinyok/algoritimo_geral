'''

calcular a soma dos cubos dos numeros que sao menores que a media da lista


'''
from random import randint
from functools import reduce

lista = [5, 10, 15]

resultado = reduce(lambda x, y: x + y, map(lambda x: x ** 3, filter(lambda x: x < reduce(lambda x, y: x + y, lista) / len(lista), lista)))

print(resultado)