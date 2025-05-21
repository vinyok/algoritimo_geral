'''

1 - var de controle 
2 - condição de parada
3 - att de var de controle

'''
# var de controle 
i = 30
# condição de parada
while i < 50:
    if i % 2 == 0:
        print(f'i = {i}')
# att da var
    i = i + 1 # incremento


# criar um laço com while que dependa da respota do usuario para continuar o laço

resp = 's'
while resp == 's':
    print ('Ainda estou repetindo...')
    while True:
        resp = input('Deseja continuar? (s) = sim / (n) = não ')
        resp = resp.lower()
        if resp == 's' or 'n':
            break
print('Terminei!!!')

