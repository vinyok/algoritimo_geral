'''
2. Solicite ao usúario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha

'''
nomes = []

for i in range (5):
    usuario_nome = input('Digite um nome: ')
    nomes.append(usuario_nome)
print('Nomes digitados: ')
for nome in nomes:
    print(nome)

    
 