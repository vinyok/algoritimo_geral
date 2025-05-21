'''
Sistema de eleição

ler 1000 votos para escolher 1 de 3 candidatos

podem votar em nulo também

(mostrar a quantidade de votos do 1 candidato e a %)
(mostrar a quantidade de votos do 2 candidato e a %)
(mostrar a quantidade de votos do 3 candidato e a %)
(mostrar a quantidade de votos nulos e a %)

no final, apresentar qual foi o canditado com o maior e menor número de votos.

'''
import random
nulos = 0
c1, c2, c3 = 0, 0, 0

voto = print(('Vote nos candidatos: (1) (2) (3) . Vote (0) para nulo. '))

for i in range (1000):
    x = random.randint(0, 3)
    if x == 0:
        nulos += 1
    elif x == 1:
        c1 += 1
    elif x == 2:
        c2 += 1
    elif x == 3:
        c3 += 1
print(f'A quantidade de votos do candidato 1 foi de: {c1}, do c2 foi de: {c2}, do c3: {c3} e de nulos foram de: {nulos}')
        



