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
