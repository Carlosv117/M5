# x tal que x é par e x é maior que 4 e menor que 8
# A = { x | x é par e 4 < x < 10 }
# O conjunto acima pode ser definido dessa forma
# A = {6, 8}
#
# x tal que 2x mais um é igual a 7 e x é um inteiro
# B = { x | 2x + 1 = 7 e x é inteiro }
# O conjunto acima pode ser definido dessa forma
# B = {3}

# Definindo conjunto com chaves
meu_conjunto = {1, 2, 3, 4, 5, 6}
print(meu_conjunto)
# output: {1, 2, 3, 4, 5, 6}

# Definindo conjunto via builtin set()
meu_conjunto = set([1, 2, 3, 4, 5, 6])
print(meu_conjunto)
# output: {1, 2, 3, 4, 5, 6}

# Definindo conjunto via builtin passando range como argumento
meu_conjunto = set(range(10))
print(meu_conjunto)
# output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Adicionando um elemento
meu_conjunto = set()
meu_conjunto.add(2)
meu_conjunto.add('teste')
meu_conjunto.add((1, 2, 3))
print(meu_conjunto)
# output: {'teste', 2, (1, 2, 3)}

# Adicionando múltiplos elementos de uma vez
meu_conjunto = set()
meu_conjunto.update([1, 2, 3])
print(meu_conjunto)
# output: {1, 2, 3}

meu_conjunto = set([1, 2, 3, 1, 2, 3])
meu_conjunto.remove(2)
print(meu_conjunto)
# output: {1, 3}

# Caso o elemento não estiver presente, teremos uma exceção:
meu_conjunto.remove(4)
# Traceback (most recent call last):
# File "main.py", line 153, in <module>
meu_conjunto.remove(4)
KeyError: 4

# Utilizando discard, não temos uma exceção levantada caso o elemento não exista
meu_conjunto = set([1, 2, 3, 1, 2, 3])
meu_conjunto.discard(4)
print(meu_conjunto)
{1, 3}

meu_conjunto = set([1, 2, 3, 1, 2, 3])
print(meu_conjunto)
# output: {1, 3}

meu_conjunto.clear()
print(meu_conjunto)
# output: set()

a = {0, 3, 6, 9, 12, 15}
print(a)
# output: {0, 3, 6, 9, 12, 15}

b = {0, 5, 10, 15}
print(b)
# output: {0, 5, 10, 15}

c = a | b
print(c)
# output: {0, 3, 5, 6, 9, 10, 12, 15}

c = a.union(b)
print(c)
# output: {0, 3, 5, 6, 9, 10, 12, 15}


a = {0, 3, 6, 9, 12, 15}
print(a)
# output: {0, 3, 6, 9, 12, 15}

b = {0, 5, 10, 15}
print(b)
# output: {0, 5, 10, 15}

c = a & b
print(c)
# output: {0, 15}

c = a.intersection(b)
print(c)
# output: {0, 15}

a = {0, 3, 6, 9, 12, 15}
print(a)
# output: {0, 3, 6, 9, 12, 15}

b = {0, 5, 10, 15}
print(b)
# output: {0, 5, 10, 15}

c = a - b
print(c)
# output: {3, 6, 9, 12}

c = a.difference(b)
print(c)
# output: {3, 6, 9, 12}

# Do mesmo modo, podemos remover de b, todos os elementos de a
d = b - a
print(d)
# output: {5, 10}

a = {0, 3, 6, 9, 12, 15}
print(a)
# output: {0, 3, 6, 9, 12, 15}

b = {0, 5, 10, 15}
print(b)
# output: {0, 5, 10, 15}

c = a ^ b
print(c)
# output: {3, 5, 6, 9, 10}

c = a.symmetric_difference(b)
print(c)
# output: {3, 5, 6, 9, 10}

# Do mesmo modo, se fizeremos a difereça simétrica de b com a, teremos o mesmo
# resultado
d = b.symmetric_difference(a)
print(d)
# output: {3, 5, 6, 9, 10}

a = {0, 3, 6, 9, 12, 15}
print(a)
# output: {0, 3, 6, 9, 12, 15}

b = {0, 5, 10, 15}
print(b)
# output: {0, 5, 10, 15}

# Podemos verificar se um elemento pertence a um conjunto
print(0 in a)
# output: True

# Podemos verificar se todos os elementos de um conjunto
# estão presentes em outro conjunto, utilizando a função issubset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}

print(a.issubset(b))
# output: False

print(b.issubset(a))
# output: True
