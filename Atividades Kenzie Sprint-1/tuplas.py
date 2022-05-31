minha_tupla = (10, 20, 30)
print(minha_tupla)
# (10, 20, 30)

tupla_elemento = (10,)
print(tupla_elemento)
# (10,)

tupla_vazia = ()
print(tupla_vazia)
# ()

tupla_tuple = tuple('Teste')
print(tupla_tuple)
# ('T', 'e', 's', 't', 'e')

minha_tupla = (10, 20, 30,)
print(minha_tupla[2])
# 30

# Verificando seu tamanho
minha_tupla = (10, 20, 30,)
print(len(minha_tupla))
# 3

# Verificando se a tupla contém determinado elemento
print(30 in minha_tupla)
# True

# Verificando o numero de aparições de um elemento
print(minha_tupla.count(10))
# 1

print(minha_tupla.count(40))
# 0

# Verificando o índice de um elemento a partir de seu valor
minha_tupla = ('João', 'José', 'Maria', 'Joana', 'João',)
print(minha_tupla.index('João'))
# 0
# Observe que é retornado o índice do primeiro elemento encontrado

minha_tupla = ('João', 'José', 'Maria', 'Joana', 'João',)
minha_tupla[0] = 'Pedro'

# Traceback (most recent call last):
# File "main.py", line 2, in <module>
# minha_tupla[0] = 'Pedro'
# TypeError: 'tuple' object does not support item assignment
