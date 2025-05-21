'''
21. 


Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros
pares usando remove.

'''

lista = []
pares = 0

for i in range (5):
    nms_user = int (input('Digite um número: '))
    lista.append(nms_user)
    
    
for n in lista[:]:
    if n % 2 == 0:
        lista.remove(n)
print(lista)
        