idade = 10
pi = 3.14
nome = 'viny'
status = True


nota1 = int(input('digite a primeira nota do aluno: '))

print('a nota digitada foi: ', nota1)

# ler duas notas e efetuar as 4 operações mat.

nota2 = int(input('digite a segunda nota: '))

print('a nota digita foi: ', nota2)

print('O resultado da soma é: ', nota1 + nota2)
print('O resultado da sub é: ', nota1 - nota2)
print('O resultado da mult é: ', nota1 * nota2)
print('O resultado da div é: ', nota1 / nota2)

# ler as 4 notas de um aluno e calcular a média e mostrar

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
n4 = float(input('digite a quarta nota: '))

print('a nota digitada foi: ', n1)
print('a nota digitada foi: ', n2)
print('a nota digitada foi: ', n3)
print('a nota digitada foi: ', n4)

media = (n1 + n2 + n3 + n4) / 4
print('O resultado da média é: ', media)

# calcular a média ponderada: 
media_p = (n1 * 0.2 + n2 * 0.1 + n3 * 0.3 + n4 * 0.3)

#f-string
print(f'Nota 1: {n1}, Nota 2: {n2}, Nota 3: {n3}, Nota 4: {n4}')

print('A média ponderada é: ', media_p)
