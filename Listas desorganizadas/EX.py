# 1 A) - DADO UM NÚMERO VERIFIQUE SE ELE É MAIOR QUE 10

n1 = float(input("Digite o valor do número: "))
print("O valor do número digitado foi: ", n1)

if n1 >= 10: (print ('O valor digitado é maior ou igual a 10'))
else: (print('O valor digitado é menor que 10'))

# B) - DADO UM NÚMERO VERIFIQUE SE ELE ESTÁ NO INTERVALO DE 100 A 1000

num1 = float(input("Digite o valor do número: "))
print("O valor do número digitado foi: ", num1)

if 100 < num1 < 1000: (print("O valor está entre 100 a 1000"))
else: print("O valor digitado não está entre 100 e 1000")

# C) - DADO UM NÚMERO INFORME EM QUAL INTERVALO ELE SE ENCONTRA
# intervalo A : 0 a 20
# intervalo B : -5 a -1
# intervalo C : 21 a 60
# intervalo D : -100 a 15

numero1 = float(input("Digite o valor do número: "))
print("O valor do número digitado foi: ", numero1)                                       

if 0 <= numero1 < 20: (print("O valor se escontra no intervalo A"))
elif -5 <= numero1 < -1: (print("O valor se escontra no intervalo B"))
elif 21 <= numero1 < 60: (print("O valor se escontra no intervalo C"))
elif -100 <= numero1 < 15: (print("O valor se escontra no intervalo D"))

# D) CALCULAR A ÁREA DE UMA CIRCUNFÊRENCIA E MOSTRÁ-LA. O VALOR DO RAIO NÃO PODE SER NEGATIVO

raio = float(input('Digite o valor do raio: '))
print("O valor do raio digitado foi: ", raio) 
 
if raio <= 0: (print("Valor inválido. O raio não pode ser negativo ou zero."))
else:
    raio = (raio * raio) * 3.14 
    print(('O valor da área é: '), raio)

# E) CALCULAR O VALOR DO SALÁRIO LIQUÍDO DE UM PROGAMADOR, DADO O NÚMERO DE FUNÇÕES CRIADAS,
# O VALOR DE CADA FUNÇÃO, O PERCENTUAL DE DESCONTO DO INSS É 8% SOBRE O SALÁRIO BRUTO
# DEVERÁ SER INFORMADO: O NOME DO FUNC, SALARIO BRUTO E SALARIO LIQ. VALIDAR OS VALORES DE ENTRADA.

nome = str(input("Digite o primeiro e o ultimo nome: "))

salario_bruto = float (input("Digite o salário bruto: "))
if salario_bruto <= 0:
    print("Valor inválido. O salário não pode ser negativo ou zero.")
else:
    print(nome,", O valor do salário digitado foi: R$",salario_bruto)

    salario_liq =  salario_bruto - (salario_bruto * 0.08)
    print(f"O valor do salário líquido é: R$ {salario_liq}")

# F) LER DOIS VALORES MAIOR DO QUE ZERO PARA AS VÁRIAVEIS A e B, EFETUAR A TROCA DOS
# CONTEÚDOS DE FORMA QUE A VÁRIAVEL A PASSE A TER O CONTÉUDO DA VAR B e VICE-VERSA
# UTILIZE 1 VÁRIAVEL AUX PARA RESOLVER.

a = float((input("Digite o valor de A: ")))
b = float((input("Digite o valor de B: ")))
aux = float

if a <= 0 or b <= 0:
    print('O valor digitado é inválido. A e B devem ser maior do que zero.')
else:
    print("Os valores digitados foram:",a, "e", b)
    
    aux = a
    a = b
    b = a
    
    print('Os valores com a troca de conteúdo ficaram: B =',aux,"e A =",b)
    
# G) DETERMINAR SE UM ALUNO ESTÁ OU NÃO APROVADO, CONHECIDAS AS NOTAS DOS 4 BIMESTRES
# SENDO A MÉDIA DE APROVAÇÃO 6.

nota1 = float((input("Digite da nota do primeiro bimestre: ")))
nota2 = float((input("Digite da nota do segundo bimestre: ")))
nota3 = float((input("Digite da nota do terceiro bimestre: ")))
nota4 = float((input("Digite da nota do quarto bimestre: ")))
media = int(nota1 + nota2 + nota3 + nota4) / 4

if media < 6:
    print('O aluno não atingiu a média necessária de 6. A média do aluno foi de: ', media)
else:
    print("O aluno está aprovado. Sua média foi de: ", media)
    
# H) DADA TRÊS MEDIDAS INFORMAR A MAIOR
m1 = float(input('Digite o valor da primeira medida: '))    
m2 = float(input('Digite o valor da segunda medida: '))    
m3 = float(input('Digite o valor da terceira medida: '))
maior_medida = float(max (m1, m2, m3))

print('A medida de maior valor é: ', maior_medida)
    
# DETERMINAR SE UM NÚMERO É IMPAR OU PAR

numero = int(input('Digite o valor do número: '))


if numero % 2 == 0:
    print('O número digitado é par.')
else:
    print('O número digitado é impar.')
    
# TENDO COMO DADOS DE ENTRADA A ALTURA E O SEXO DA PESSOA, CALCULAR SEU PESO IDEIAL
# UTILIZANDO A SEGUINTE FORMÚLA: 
# - PARA HOMENS: (72,7 * H) - 58 ;
# - PARA MULHERES: (62,1 * H) - 44,7 ;

altura = float (input('Digite sua altura: '))
print ('A altura digitada foi: ', altura)

sexo = str (input('Digite o seu sexo: '))
masculino = str
homem = str
mulher = str
feminino = str
peso_ideal = float

if sexo == masculino or homem:
    peso_ideal = (72.7 * altura) - 58
    print('O seu peso ideal é de: ', peso_ideal)
elif sexo == feminino or mulher:
    (62.1 * altura) - 44.7
    print('O seu peso ideal é de: ', peso_ideal)
    
# DETERMINAR AS RAÍZES REAIS DE UMA EQUAÇÃO DO 2 GRAU
# (Ax2+Bx+C=0)
















# DETERMINAR DENTRE 4 NÚMEROS A SOMA DOS PARES

numero01 = float(input('Digite o valor do primeiro número: '))
numero02 = float(input('Digite o valor do segundo número: '))
numero03 = float(input('Digite o valor do terceiro número: '))
numero04 = float(input('Digite o valor do quarto número: '))
soma_dos_pares = float
par_1 = float
par_2 = float
par_3 = float
par_4 = float

if numero01 % 2 == 0:
    par_1 = numero01
else: 
    par_1 = 0
        
if numero02 % 2 == 0:
    par_2 = numero02
else:
    par_2 = 0 
    
if numero03 % 2 == 0:
    par_3 = numero03
else:
    par_3 = 0
    
if numero04 % 2 == 0:
    par_4 = numero04
else:
    par_4 = 0

soma_dos_pares = (par_1 + par_2 + par_3 + par_4)
print('A soma dos números pares é de: ', soma_dos_pares)

# OBTER, DENTRO DE 5 NÚMEROS A MÉDIA DOS ÍMPARES

# pegando os valores dos 5 números

numero001 = float(input('Digite o valor do primeiro número: '))
numero002 = float(input('Digite o valor do segundo número: '))
numero003 = float(input('Digite o valor do terceiro número: '))
numero004 = float(input('Digite o valor do quarto número: '))
numero005 = float(input('Digite o valor do quinto número: '))

# pegando os valores apenas dos ímpares

impar1 = float
impar2 = float
impar3 = float
impar4 = float
impar5 = float
media_impar = float

if numero001 % 2 > 0:
    impar1 = numero001

if numero002 % 2 > 0:
    impar2 = numero002

if numero003 % 2 > 0:
    impar3 = numero003

if numero004 % 2 > 0:
    impar4 = numero004

if numero005 % 2 > 0:
    impar5 = numero005

media_impar = (impar1 + impar2 + impar3 + impar4 + impar5) / 5
print (f'A média dos números ímpares é de : {media_impar}')









