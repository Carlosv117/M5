def soma(num1, num2):
    return num1 + num2


print(soma(4, 5))
# 9


def calculo_imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado


print(calculo_imc(80, 1.80))
# 24.691358024691358

print(calculo_imc(1.80, 80))
# 0.00028125000000000003

print(calculo_imc(altura=1.80, peso=80))
# 24.691358024691358


"""
Funções para criar e converter estruturas de dados
"""

# conversão para booleano
x = bool(0)
print(x)
# False

# conversão de inteiro para string
x = str(400)
print(x)
# '400'

# conversão de inteiro para decimal
x = float(7)
print(x)
# 7.0

# conversão de string para inteiro
x = int("14")
print(x)
# 14


"""
Funções para processar dados
"""

# somar os elementos de um iterável
x = [1, 2, 3, 4]
print(sum(x))
# 10

# verificar se todos os elementos de um iterável são verdadeiros
x = [True, False, True]
print(all(x))
# False

# verificar se pelo menos um elemento de um iterável é verdadeiro
x = [True, False, True]
print(any(x))
# True

# retornar o valor mínimo de um iterável
x = [10, 2, 33, 44]
print(min(x))
# 2

# retornar o valor máximo de um iterável
x = [10, 2, 33, 44]
print(max(x))
# 44

# parear elementos de 2 ou mais iteráveis de mesma
# posição, gerando um objeto zip composto por tuplas
x = ["John", "Maria", "Elvis"]
y = ["25", "40", "43"]
z = zip(x, y)
print(z)
# <zip object at 0x7fb70dc56e80>

# listando as tuplas do objeto zip
print(list(z))
# [('John', '25'), ('Maria', '40'), ('Elvis', '43')]

# verificar o tamanho de um iterável
x = [1, 2, 3]
print(len(x))
# 3
