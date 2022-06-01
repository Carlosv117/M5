carrinho_de_compras = ["Banana", "Pera", "Tomate"]

for item in carrinho_de_compras:
    print(item)

# Banana
# Pera
# Tomate

string = 'Kenzie'

for letra in string:
    print(letra)
# K
# e
# n
# z
# i
# e

pessoa = {"nome": "José da Silva", "idade": 36, "sexo": "masculino"}
# o método items nos retorna uma tupla que
# pode ser desconstruida em chave e valor, veremos com mais calma futuramente
for chave, valor in pessoa.items():
    print(chave, ":", valor)
# nome José da Silva
# idade 36
# sexo masculino

# Se iterarmos somente pelo dicionário, sem a função built-in
# o loop será feito apenas pelas chaves:
for item in pessoa:
    print(item)
# nome
# idade
# sexo

for i in range(4):
    print(i)
# 0
# 1
# 2
# 3

for _ in range(3):
    print('Olá Kenzie')
# Olá Kenzie
# Olá Kenzie
# Olá Kenzie

contador = 0
while contador <= 5:
    print(f'Contando: {contador}')
    contador += 1

print('Fim da contagem')
# Contando: 0
# Contando: 1
# Contando: 2
# Contando: 3
# Contando: 4
# Contando: 5
# Fim da contagem

carrinho_de_compras = ["Banana", "Pera", "Tomate"]
# Podemos desconstruir a tupla em indice e item
for indice, item in enumerate(carrinho_de_compras):
    print(indice, item)
# 0, Banana
# 1, Pera
# 2, Tomate

for numero in range(5):
    print(numero)
# 0
# 1
# 2
# 3
# 4

for numero in range(10):
    if numero == 3:
        break
    print(numero)
# 0
# 1
# 2

for numero in range(10):
    if numero in [4, 5, 6, 7, 8]:
        continue
    print(numero)
# 0
# 1
# 2
# 3
# 9

numero = 0
while numero <= 5:
    numero += 1
    if numero == 2 or numero == 3:
        continue
    print(numero)
# 1
# 4
# 5
# 6

for item in range(10):
    pass


def funcao():
    pass
