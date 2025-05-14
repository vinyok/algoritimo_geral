'''
Listas > são coleções heterogêneas de objetos, podem ser de qualquer tipo

As listas em Python são mutáveis, podendo alterar a qualquer momento. Podem ser fateadas

'''

# Sintase
# Indíce começa com 0

lista = ['A', 'B', 'C', 'ifms', 2025, 3.14]

# imprimindo as listas
# 1 .
print(lista)
print('')
# 2 .
for i in range(6):
    print(lista[i])
print('')
# 3 .
for i in lista:
    print(i)
print('')
# acessar / inserir
print(lista[-1])
print('')


# adicionar
lista [2] = 'beto'
lista.append('U2')


# remover
lista[2] = ''

lista.remove('U2')

# Ordernar
# lista.sort()

# Inventer a lista
lista.reverse()

# Contador
print(len(lista))


for i, item in enumerate(lista):
    print(f'O item de indice {i} tem o valor {item}')

# Enumerate retorna uma tupla de dois elementos a cada iteração: de um número sequencial e item da sequência


# PESQUISAS 
'''
Estudar FUNÇÕES

Pesquisar: Insert e Pop (Funções). Tipos de ordenação 
'''