lista = []

for n in range(10):
    lista.append(n * 2)

print(lista)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lista = [n * 2 for n in range(10)]
print(lista)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lista = [numero for numero in range(61) if numero % 6 == 0]
print(lista)
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

lista = [0, 3, 12, 15, 30]
nova_lista = [
    numero if numero % 5 == 0 else 'Não é múltiplo de 5' for numero in lista
]
print(nova_lista)
# [0, 'Não é múltiplo de 5', 'Não é múltiplo de 5', 15, 30]

# Exemplo dicionário que vamos construir
# {0: 'Brasil', 1: 'Argentina', 2: 'Chile'}
lista = ['Brasil', 'Argentina', 'Chile']

novo_dict_comprehension = {indice: pais for indice, pais in enumerate(lista)}
print(novo_dict_comprehension)
# {0: 'Brasil', 1: 'Argentina', 2: 'Chile'}

pessoas = {'Julian': 11, 'Myke': 38, 'Gandalf': 57, 'Johnatan': 33}
pares_dict = {key: value for (key, value) in pessoas.items() if idade > 40}
print(pares_dict)
# {'Gandalf': 57}

palavras = ["três", "pratos", "de", "trigo",
            "para", "três", "tigres", "tristes"]

palavras_unicas = {palavra for palavra in palavras}
print(palavras_unicas)
# {'de', 'três', 'tigres', 'tristes', 'trigo', 'para', 'pratos'}

palavras = ["três", "pratos", "de", "trigo",
            "para", "três", "tigres", "tristes"]

palavras_unicas = {palavra for palavra in palavras if len(palavra) > 5}
print(palavras_unicas)
# {'tigres', 'tristes', 'pratos'}
