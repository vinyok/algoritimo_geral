'''
19. 

Solicite nomes at´e que o usu´ario digite ”sair”. Armazene em uma lista e imprima.

'''

lista = []

while True:
    nomes = str (input('Digite um nome: '))
    sair = str (input('Caso deseje parar digite: "SAIR" ')).upper()
    lista.append(nomes)
    if sair == 'SAIR':
        break
print(lista)
    