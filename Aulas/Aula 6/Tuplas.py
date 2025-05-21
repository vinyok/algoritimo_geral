'''
Tuplas são semelhantes a listas, porem são IMUTÁVEIS!
não pode acrescentar, apagar ou fazer atribuição.
'''
# sintase

# Os parenteses são opcionais caso use VIRGÚLA. 

tupla = (1, 2, 3, 4)

print(tupla[2])

# pode usar uma tupla em uma lista
lista = [1, 2, 3, (2, 3, 4)]

# converter tuplas em lista
nova_lista = list(tupla)

# converter lista em tupla
nova_tupla = tuple(lista)

'''
PESQUISAS:
Sequências para conhecer: set, frozenset

'''
tupla.count()
print(tupla)