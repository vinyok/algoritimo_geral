'''
definição de recursividade(recursão):

Recursividade é uma tecnica de progamação(umas das mais utilizadas) onde uma função chama a si mesma
para resolver um problema (geralmente divisão e conquista)

Principais caracteristicas:
caso base: condição de parada que evita chamadas infinitas 
caso decursivo: onde uma função chama a si mesma com um problema menor (parametro)

OBS: uma função não pode chamar a si mesma, recursão é um looping infinito, por isso PRECISA ter o caso base.

'''
from functools import reduce

def func(x):
    # x -= 1
    if x < 0:
        return
    print(x)
    return func(x-1)

func(10)

# Ex. 1 - Fatorial de um numero

# fazer em casa. fatorial de 1000000000 usando laço de repetição e depois fazer usando recursão

n = 5

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(n)) 

'''
FIBONACCI : 1 1 2 3 5 8 13 

a sequencia funciona somando os dois ultimos valores

'''
serie_fibonacci = [1, 1]

def fibonacci(n):
    list(map(lambda: n if n > 100:
        return))
    return n + (serie_fibonacci[0, 1 +1])

print(fibonacci(serie_fibonacci)) 












'''
PESQUISAR O QUE É BUBBLE SORT. DUNÇÃO QUADRADATICA.

QUICK SORT OU MARGE SORT


ALG QUADRATICOS PARA VETORES PEQUENOS SAO OTIMOS, PARA VETORES GRANDE SAO PESSIMOS
'''