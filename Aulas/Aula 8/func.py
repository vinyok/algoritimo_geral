# Melhor conceito em ling. de prog. (de acordo com o Beto)

'''
Funções !
são blocos de códigos identificados por um nome
e elese também podem receber "parâmetros"

IMPLEMENTAR EM TODOS OS EXS QUE NÃO FIZ AINDA

sintaxe básica:
        nome    posso colocar var
def     func        (a, b):
    corpo da func
    return (opcional)

'''

def soma(x, y):
    soma = x + y
    print(soma)
    # ou . é bom usar return quando for voltar no cod
    return x + y
a = int(input('Digite um num: '))
b = int(input('Digite um num: '))
soma = soma(a, b)
media = soma / 2

# PASSAGEM DE PARAMETRO DE REFERENCIA. estudar!