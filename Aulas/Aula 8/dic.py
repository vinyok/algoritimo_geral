'''
dicionario é uma lista de associações compostas por chave
ÚNICA 

Sintax

dicionario = {'a': e, 'b': b}
'''

dic = {'nome': 'beto', 'banda': 'U2'}

# imprimir elemento pela chave
print(dic['nome'])

# add novo elemento
dic['album'] = 'Version 2.0'

# apagar elemento
del dic['album']

# acessar elementos. ACESSANDO TODOS
item = dic.items()

print(item)

# acessar as chaves. ACESSANDO TODAS
chaves = dic.keys ()

print(chaves)
 
# valores dentro de um dic. TODOS
valores = dic.values()
print(valores)

# outro ex.
# como passar um laço de repetição percorrer um dic.

progs = {'Yes': ['Close To Edge', 'Fragile'], 'Genesis': ['Foxtrot', 'Alpha'], 'ELP': ['Brain']}

progs ['Kings Crimson'] = ['Red', 'Discipline']

progs.items()
print(progs)

for i in progs.items():
    print(i)
    
# deletar uma key com um dic com muitos elementos    

'''
EX. PRÁTICO:

estrutura 'nome': xxxx, 'notas': [n1,n2,n3]

crie um progama que leia o nome de 5 alunos, e suas 4 notas (GERADAS ALEATORIAS)
verifique qual aluno teve a maior média e mostra no final a % de alunos aprovados e reprovados.

'''

import random

medias = 0

dicionario = {'nomes alunos': [' '], 'notas': [0,0,0,0]}

if_dic = {}
for i in range(1):
    nomes = input('Digite o nome do aluno: ')
    notas = []
    est = {}
    for j in range(4): 
        n = float(input(f'Digite a nota {j+1} do {nomes}: '))
        notas.append(n)
    medias = sum(notas) / 4
    est['notas'] = notas
    est['medias'] = medias
    if_dic[nomes] = est
    
while True:
    digite = input('Procure a média de um aluno digitando seu nome: ')
    if digite == nomes:
        print(est)
    elif digite != nomes:
        print('Nome não encontrado.')
    sair = int (input('\nDigite 0 para parar de procurar: '))
    if sair == 0:
            break


# TUPLA PODE SER UTILIZADO COMO CHAVE. 
# QUALQUER ELEMENTO IMUTÁVEL PODE SER UTILIZADO      


