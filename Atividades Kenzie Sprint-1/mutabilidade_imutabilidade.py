# main.py
# nome = 'python'
# nome[0] = 'P'
# Traceback (most recent call last):
# File "main.py", line 2, in
#     nome[0] = 'P'
# TypeError: 'str' object does not support item assignment

# main.py
import copy
x = 10
print(id(x))
# 139624443447888

x = x + 10
print(id(x))
# 139624443448208

# main.py
minha_lista = [1, 2, 3]
print(minha_lista)
# [1, 2, 3]

print(id(minha_lista))
# 140470422469568

minha_lista[0] = 7
print(minha_lista)
# [7, 2, 3]
print(id(minha_lista))
# 140470422469568

minha_lista_2 = [1, 2, 3]
print(id(minha_lista_2))
# 140470422469696

minha_lista_2 += [4]
print(id(minha_lista_2))
# 140470422469696

# main.py


def func_param(lista, numero):
    lista.append(100)
    numero = numero + 50
    print(f'Lista dentro da função: {lista}')
    print(f'Número dentro da função: {numero}')


minha_lista = [5, 25, 50]
numero_inteiro = 25

minha_lista_copia = minha_lista

print(f'Lista antes da chamada da função: {minha_lista}')
print(f'Inteiro antes da chamada da função: {numero_inteiro}')
print('*' * 50)
func_param(minha_lista_copia, numero_inteiro)
print('*' * 50)
print(f'Lista fora do escopo da função {minha_lista}')
print(f'Inteiro fora do escopo da da função: {numero_inteiro}')

print(f'Lista cópia após a função ter sido invocada: {minha_lista_copia}')

# main.py
# Lista antes da chamada da função: [5, 25, 50]
# Inteiro antes da chamada da função: 25
# **************************************************
# Lista dentro da função: [5, 25, 50, 100]
# Número dentro da função: 75
# **************************************************
# Lista fora do escopo da função [5, 25, 50, 100]
# Inteiro fora do escopo da da função: 25
# Lista cópia após a função ter sido invocada: [5, 25, 50, 100]

# main.py


def func_param(lista, numero):
    lista.append(100)
    numero = numero + 50
    print(f'Lista dentro da função: {lista}')
    print(f'Número dentro da função: {numero}')


minha_lista = [5, 25, 50]
numero_inteiro = 25

minha_lista_copia = minha_lista.copy()

print(f'Lista antes da chamada da função: {minha_lista}')
print(f'Inteiro antes da chamada da função: {numero_inteiro}')
print('*' * 50)
func_param(minha_lista_copia, numero_inteiro)
print('*' * 50)
print(f'Lista fora do escopo da função {minha_lista}')
print(f'Inteiro fora do escopo da da função: {numero_inteiro}')

print(f'Lista cópia após a função ter sido invocada: {minha_lista_copia}')

# main.py
# Lista antes da chamada da função: [5, 25, 50]
# Inteiro antes da chamada da função: 25
# **************************************************
# Lista dentro da função: [5, 25, 50, 100]
# Número dentro da função: 75
# **************************************************
# Lista fora do escopo da função [5, 25, 50]
# Inteiro fora do escopo da da função: 25
# Lista cópia após a função ter sido invocada: [5, 25, 50, 100]

# main.py
minha_lista = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]

minha_lista_copia = minha_lista.copy()

# Alterando os elementos dentro de minha_lista_copia
minha_lista_copia[0] = 10
minha_lista_copia[3][0] = 'A'

print(minha_lista_copia)
# [10, 2, 3, ['A', 'b', 'c'], 4, 5, 6]

print(minha_lista)
# [1, 2, 3, ['A', 'b', 'c'], 4, 5, 6]

# main.py

minha_lista = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]

minha_lista_copia = copy.deepcopy(minha_lista)
minha_lista_copia[3][0] = 'A'

minha_lista_copia
[1, 2, 3, ['A', 'b', 'c'], 4, 5, 6]

minha_lista
[1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]
