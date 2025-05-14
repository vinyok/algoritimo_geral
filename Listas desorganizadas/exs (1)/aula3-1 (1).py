'''
1 - Ler dois números, onde o primeiro vai ser o ínicio do laço e o segundo será o fim.
validar os números de entrada

'''

n1 = int(input('Digite o valor de n1: '))
n2 = int(input('Digite o valor de n2: '))

if n1 < n2:
    aux = n1
    n1 = n2
    n2 = aux
    
for a in range(n2, n1 + 1):
        print (a)

'''''
2 -
    *
   **
  ***
 ****
*****
'''

for i in range(6):
    for j in range(1, i):
        print(j, end=' ')
    print(' ')
    
    
for um in range(1, 6):
    for m in range (um, 6):
        print(um, end=' ')
    print (' ')



