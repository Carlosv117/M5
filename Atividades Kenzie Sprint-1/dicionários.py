meu_dicionario = {'chave': 'valor'}
print(meu_dicionario)
print(type(meu_dicionario))
# {'chave': 'valor'}
# <class 'dict'>

meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# Podemos também passar uma lista contendo tuplas, representando chave e valor:
meu_dicionario = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# Se um dos iteráveis, tiver mais elementos que o outro, ele será ignorado
lista_1 = ['primeiro', 'segundo', 'terceiro', 'quarto']
lista_2 = [1, 2, 1]
meu_dicionario = dict(zip(lista_1, lista_2))
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 1}

meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
# Para acessarmos o elemento com valor 2, podemos fazer da seguinte maneira:
print(meu_dicionario['segundo'])
# 2

print(meu_dicionario['quarto'])
# Traceback (most recent call last):
#  File "main.py", line 202, in <module>
#    print(meu_dicionario['quarto'])
# KeyError: 'quarto'

# Acessando elemento existente com get():
print(meu_dicionario.get('segundo'))
# 2

# Acessando elemento inexistente com get():
print(meu_dicionario.get('quarto'))
# None

# Se quisermos podemos personalizar a mensagem do erro, ao invés de ser None.
print(meu_dicionario.get('quarto', 'Chave não encontrada'))
# 'Chave não encontrada'

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
print(meu_dicionario.keys())
# dict_keys(['primeiro', 'segundo', 'terceiro'])

print(meu_dicionario.values())
# dict_values([1, 2, 3])

# E se quisermos todos os dados, chave e valor,
# podemos utilizar a função items()
print(meu_dicionario.items())
# dict_items([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])

meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# Para adicionar a chave quarto com o valor 4, basta fazer o seguinte:
meu_dicionario['quarto'] = 4
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3, 'quarto': 4}

# Se o elemento já existir, ele será atualizado:
meu_dicionario['quarto'] = 5
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3, 'quarto': 5}

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
print(meu_dicionario)

meu_dicionario.update({'quarto': 4})
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3, 'quarto': 4}

meu_dicionario.update({'quarto': 5})
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3, 'quarto': 5}

meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
del meu_dicionario['primeiro']
print(meu_dicionario)
# {'segundo': 2, 'terceiro': 3}

# Utilizando o pop()
meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
print(meu_dicionario.pop('primeiro'))
# 1
print(meu_dicionario)
# {'segundo': 2, 'terceiro': 3}

# Utilizando o popitem()
meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
print(meu_dicionario.popitem())
# ('terceiro', 3)
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2}

meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)
meu_dicionario.clear()
print(meu_dicionario)
# {}
