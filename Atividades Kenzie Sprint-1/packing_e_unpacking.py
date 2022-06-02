# Acessando valores por indexação
tabuada_5 = [n for n in range(1, 51) if n % 5 == 0]
print(tabuada_5[0])
# 5
print(tabuada_5[1:4])
# [10, 15, 20]

# Acessando valores por descompactação
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = tabuada_5
print(v1)
# 5

# Pegando o primeiro, segundo e compactando o restante
primeiro, segundo, *restante = tabuada_5

print(primeiro)
# 5
print(restante)
# [15, 20, 25, 30, 35, 40, 45, 50]

# Pegando os 2 últimos
*restante, penultimo, último = tabuada_5

# Pegando o primeiro e o ultimo e empacotando o restante
primeiro, *restante, último = tabuada_5


def exibir(*args):
    return f'O tipo de args é {type(args)} e os valores são: {args}'


resultado = exibir(10, True, 9.5, None, 'Carro')
print(resultado)
# O tipo de args é <class 'tuple'> e os valores são:
# (10, True, 9.5, None, 'Carro')

frutas_tropicais = ['Abacaxi', 'Açaí', 'Acerola', 'Caju']
frutas_invernais = ['Abacate', 'Morango', 'Kiwi', 'Maçã']

# Adicionando elementos a uma nova_lista usando asterisco
frutas_atualizadas = [*frutas_tropicais, 'Banana']
print(frutas_atualizadas)
# ['Abacaxi', 'Açaí', 'Acerola', 'Caju', 'Banana']

# Ou juntando duas listas
frutas_atualizadas = [*frutas_tropicais, *frutas_invernais]
print(frutas_atualizadas)
# ['Abacaxi', 'Açaí', 'Acerola', 'Caju', 'Abacate', 'Morango', 'Kiwi', 'Maçã']


def frutas(*frutas):
    print('Acessando frutas:')
    for fruta in frutas:
        print(f'A fruta da vez é: {fruta}')


frutas('Abacaxi', 'Banana', 'Maçã')
# Acessando frutas:
# A fruta da vez é: Abacaxi
# A fruta da vez é: Banana
# A fruta da vez é: Maçã


def pessoa(**kwargs):
    print(f'O tipo de kwargs é {type(kwargs)}')
    for chave, valor in kwargs.items():
        print(f'Chave: {chave} - Valor: {valor}')


pessoa(nome='José', idade=38, profissao='programador')
# O tipo de kwargs é <class 'dict'>
# Chave: nome - Valor: José
# Chave: idade - Valor: 38
# Chave: profissao - Valor: programador

pessoa = {'nome': 'José', 'idade': 38}

pessoa_atualizada = {**pessoa, 'profissao': 'programador'}
print(pessoa_atualizada)
# {'nome': 'José', 'idade': 38, 'profissao': 'programador'}

pessoa_atualizada = {**pessoa, 'nome': 'José da Silva'}
print(pessoa_atualizada)
# {'nome': 'José da Silva', 'idade': 38}

pessoa = {'nome': 'José', 'idade': 38}
outras_informacoes = {'profissao': 'programador'}

pessoa_atualizada = {**pessoa, **outras_informacoes}
print(pessoa_atualizada)
# {'nome': 'José', 'idade': 38, 'profissao': 'programador'}
