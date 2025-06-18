from functools import reduce



# obrigatorio o * (o args e kwargs é opcional, mas são convenções que permitam que funções recebam um número varido de parametros)
def minha_função(*args):
    for i in args:
        print(i)

minha_função (1, 2, [4, 6], [2, 4, [5, 6, 8]])


# usando laço de repetição

# recursão

def count_sublist (*args):
    count = 0
    for i in args:
        if isinstance(i, list):
            count += 1 + count_sublist(i)
        return count

print(count_sublist(minha_função))

#reduce

def count_sublist_reduce (*args):
    return reduce(lambda count, item: count + (1 if isinstance(item, list) else 0), args)

# compreensão de lista

resultado = reduce(lambda count, item: count + 1 filter(lambda item: item if isinstance(item, list) else 0))


# parametros nomeados
def soma (a, b, c):
    pass
soma(c=2, a=3, b=4)


def func_completa(param_obg, *args, **kwargs):
    print(f'Parámetro obrigatório: {param_obg}')
    print(f'Args extras: {args}')
    print(f'Kwargs extras: {kwargs}')
    
# exemplo de uso
print(func_completa('valor1', 'extra1', 'extra2', nome='vini', idade =20))

'''
FAZER UMA CALCULADORA QUE LEIA DOIS TIPOS (SOMAS, MULTI) (LER SE É MULTI OU SOMA)
LISTA DE NUMEROS
EXIBIR DETALHES SE FOR TRUE
SE FOR FALSE = MOSTRAR O RESULTADO FINAL
'''