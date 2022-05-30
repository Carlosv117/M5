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