'''
13. 
Crie uma lista com os n´umeros de 1 a 10 usando range() e imprima somente os pares.

'''

nums = []



for i in range (1,11):
    nums.append(i)
    if i % 2 == 0:    
        print (i)