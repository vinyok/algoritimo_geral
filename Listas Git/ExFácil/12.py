'''
12. 
Leia 5 n´umeros do usu´ario e verifique se cada um deles ´e maior que 10.


'''

for i in range(5):
    numeros = int (input ('Digite um número: '))
    if numeros > 10:
        print(f'{numeros} é maior do que 10.') 
    elif numeros == 10:
        print(f'{numeros} é igual à 10.') 
    else:
        numeros < 10
        print(f'{numeros} é menor do que 10.') 
        