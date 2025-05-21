'''
6.

Solicite 5 numeros ao usuario e armazene em uma lista. Em seguida, imprima o maior e o menor numero

'''

nums = []

for i in range (5):
    usuario_num = int(input('Digite um número: '))
    nums.append(usuario_num)
print('Maior número: ', max(nums))
print('Menor número: ', min(nums))