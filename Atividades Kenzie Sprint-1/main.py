# main.py
# Isso é um comentário de uma linha
"""
Isso é
um comentário
de várias linhas
"""

"""
Os tipos de dados mais comuns em python são:

1. Strings (str)
2. Inteiros (int)
3. Decimais (float)
4. Booleanos (bool)
5. Listas (list)
6. Dicionários (dict)
7. Vazios (NoneType)
"""
# Declarando variáveis
minha_string = "2"

# Verificando o tipo de uma variável
print(type(minha_string))  # output: <class 'str'>

meu_inteiro = 123
print(type(meu_inteiro))  # output: <class 'int'>

meu_decimal = 3.1415
print(type(meu_decimal))  # output: <class 'float'>

meu_booleano = True
print(type(meu_booleano))  # output: <class 'bool'>

minha_lista = [1, 2, 3]
print(type(minha_lista))  # output: <class 'list'>

meu_dicionario = {"chave": "valor"}
print(type(meu_dicionario))  # output: <class 'dict'>

meu_vazio = None
print(type(meu_vazio))  # output: <class 'NoneType'>

meu_numero = 1
print(type(meu_numero))
# output: <class 'int'>

# soma = meu_numero + minha_string
# output: TypeError: unsupported operand type(s) for +: 'int' and 'str'


def minha_funcao():
    meu_valor = 1234
    return meu_valor


print(minha_funcao())
# output: 1234

print(type(minha_funcao))
# output: <class 'function'>

string = "Monty Python"
# Acessando a palavra "Monty"
string[0:5]
"Monty"
# Como queremos desde o inicio da string, podemos omitir o 0
string[:5]
"Monty"

# Acessando a palavra "Python"
string[6:12]
'Python'
# Como queremos até o fim da string, podemos omitir o 12,
# que representa o ultimo indice da string
string[6:]
'Python'

string = "Monty Python"
# Para acessarmos toda a string, podemos fazer o seguinte:
string[0:12]
'Monty Python'
# Ou simplesmente omitir o inicio e fim
string[:]
'Monty Python'

# Agora, vamos acessar toda a string e vamos dar um passo 2, vejamos:
string[0:12:2]
'MnyPto'
# omitindo inicio e fim, equivale a:
string[::2]
'MnyPto'

# Traz o tamanho de determinados tipos de objeto
string = "Monty Python"
len(string)
12

# Muda o primeiro caractere da string para maiúscula e o restante para minúscula.
string = "mOnTy pYtHon"
string.capitalize()
'Monty python'

# Retorna o número de ocorrências de uma determinada sub-string da string.
string = "Monty Python"
string.count("Python")
1
string.count('o')
2

# Retorna uma lista de palavras de uma string, com um separador opcional para ser
# usado como delimitador. Se nada for passado, como padrão o delimitador será " ".
string = "Monty Python"
string.split()
['Monty', 'Python']
string = "Monty+Python"
string.split('+')
['Monty', 'Python']

# Verifica se a string possui algum conteúdo alfanumérico (letra ou número)
string = "!@#$%"
string.isalnum()
False

# Verifica se a string possui apenas conteúdo alfabético
string = "Monty Python"
string.isalpha()
True

# Verifica se todas as letras de uma string são minúsculas
string = "Monty Python"
string.islower()
False

# Verifica se todas as letras de uma string são maiúsculas
string = "MONTY PYTHON"
string.isupper()
True

# Verifica se a string começa com uma sub-string
string = "Monty Python"
string.startswith("Mon")
True

# Verifica se a string termina com uma sub-string
string.endswith('hon')
True

# Substitui uma determinada sub-string por outra
string = "Monty Python"
string.replace('Monty', 'Kenzie')
'Kenzie Python'

# Retorna uma cópia da string trocando todas as letras para minúsculo
string = "Monty Python"
string.lower()
'monty python'

# Ao contrário do lower, o upper troca todas as letras para maiúsculo
string = "Monty Python"
string.upper()
'MONTY PYTHON'

# Esse método inverte o case de cada letra da string (minúsculo / maiúsculo)
string = "Monty Python"
string.swapcase()
'mONTY pYTHON'

# Esse método converte para maiúsculo a primeira letra de cada palavra da string
string = "monty python"
string.title()
'Monty Python'

# Centraliza a string e preenche o espaço restante com o character especificado
string = 'Kenzie'
string.center(20, '*')
'*******Kenzie*******'

# Podemos criar uma lista com sintaxe literal []:
minha_lista = [3, "abacate", 9.7, [4, 5, 6], (3, "j")]
print(minha_lista[3])
# [4,5,6]

# Utilizando a função list() para trabalhar com lista:
minha_lista = list("abc")
print(minha_lista)
# ['a', 'b', 'c']

minha_lista = list(123)
print(minha_lista)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable

# Para criarmos um valor de 0 a 5:
minha_lista = list(range(6))
print(minha_lista)
# output: [0, 1, 2, 3, 4, 5]

# Para criarmos um valor no intervalo de 15 a 20:
minha_lista = list(range(15, 21))
print(minha_lista)
# output: [15, 16, 17, 18, 19, 20]

# Para criarmos um valor no intervalo de 15 a 20 com um passo de 2:
minha_lista = list(range(15, 21, 2))
print(minha_lista)
# output: [15, 17, 19]

# Primeiramente vamos criar um lista:
minha_lista = ['1', '2', '3']
print(minha_lista)
# output: ['1', '2', '3']

# Vamos alterar o segundo elemento para a palavra 'teste':
minha_lista[1] = 'teste'
print(minha_lista)
# output: ['1', 'teste', '3']

minha_lista = ['1', 'teste', '3']

# Acessando o primeiro elemento:
print(minha_lista[0])
# output: 1

# Para acessarmos o último elemento, temos duas maneiras:
print(minha_lista[2])
print(minha_lista[-1])
# output: 3

# Acessando um intervalo do começo da lista até o indice 2
# Lembrando que o limite (nesse caso indice 2) não é considerado no fatiamento:
print(minha_lista[0:2])
# output: ['1', 'teste']

# Acessando o intervalo entre o início e o indice 3 com o passo de 2:
print(minha_lista[0:3:2])
# output: ['1', '3']

# Acessando toda lista com o passo de 2:
print(minha_lista[::2])
# output: ['1', '3']

minha_lista = [1, 2, 3]
print(len(minha_lista))
# output: 3

minha_lista = [1, 2, 3]
minha_lista.append(4)
print(minha_lista)
# output: [1, 2, 3, 4]

minha_lista = [1, 2, 3]
minha_lista.clear()
print(minha_lista)
# output: []

minha_lista = [1, 2, 3]
lista_copia = minha_lista.copy()
print(lista_copia)
# output: [1, 2, 3]

# Repare que o id dos objetos são distintos.
print(id(minha_lista))
print(id(lista_copia))
# output: 140216992200256
# output: 140216992200192

minha_lista = [1, 2, 3]
lista_copia = minha_lista

# Repare que o id dos objetos são os mesmos
print(id(minha_lista))
print(id(lista_copia))
# output: 140216992669120
# output: 140216992669120

# Se fizermos uma alteração na lista cópia, isso se refletirá na primeira lista
lista_copia[0] = 'teste'
print(minha_lista)
print(lista_copia)
# output: ['teste', 2, 3]
# output: ['teste', 2, 3]

minha_lista = ["hi", "hello", "olá"]
print(f'O retorno do método sorted é uma nova listagem: {sorted(minha_lista)}')
# O retorno do método sorted é uma nova listagem: ['hello', 'hi', 'olá']
print(f'Percebam que a lista original não foi modificada: {minha_lista}')
# Percebam que a lista original não foi modificada: ['hi', 'hello', 'olá']

minha_lista = ["hi", "hello", "olá"]
print(f'O retorno do método sort é {minha_lista.sort()}')
# O retorno do método sort é None
print(f'Utilizando sort, a lista original foi modificada = {minha_lista}')
# Utilizando sort, a lista original foi modificada = ['hello', 'hi', 'olá']

minha_lista = [1, 2, 3]
print(sorted(minha_lista, reverse=True))
# [3, 2, 1]

minha_lista = ['melão', 'abacaxi', 'jabuticaba']
minha_lista.sort(key=len, reverse=True)
print(minha_lista)
# ['jabuticaba', 'abacaxi', 'melão']

minha_lista = [1, 2, 3, 4, 1, 2, 1]
print(minha_lista.count(1))
# 3

# O método extend() adiciona os itens de um iterável ao final da lista
minha_lista = [1, 2, 3]
minha_lista.extend([4, 5, 6])
print(minha_lista)
# output: [1, 2, 3, 4, 5, 6]

# Utilizando método append adicionamos o objeto inteiro ao final da lista
minha_lista = [1, 2, 3]
minha_lista.append([4, 5, 6])
print(minha_lista)
# output:  [1, 2, 3, [4, 5, 6]]

minha_lista = [1, 2, 3]
print(minha_lista.index(2))
# 1

minha_lista = [1, 2, 3, 4, 5, 6]
print(minha_lista.pop())
# 6
print(minha_lista)
# [1, 2, 3, 4, 5]
print(minha_lista.pop(3))
# 4
print(minha_lista)
# [1, 2, 3, 5]

lista_1 = ['1', '2', '3', '1']
lista_1.remove('1')
print(lista_1)
# ['2', '3', '1']
