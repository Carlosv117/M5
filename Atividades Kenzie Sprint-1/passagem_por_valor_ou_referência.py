int_1 = 10

print(id(int_1))
# 139942949339664

print(id(int_2))
# 139942949339664

# Retorna True se ambas as variáveis estão armazenadas no mesmo local
print(int_1 is int_2)
# True

lista_1 = [10, 20, 30]
lista_1 = [10, 20, 30]

print(id(lista_1))
# 139863845450304

print(id(lista_2))
# 139863843968320

print(lista_1 is lista_2)
# False

int_1 = 1
int_2 = int_1

print(id(int_1))
# 140356426697008
print(id(int_2))
# 140356426697008

int_1 = 5

print(id(int_1))
# 140356426697136
print(id(int_2))
# 140356426697008

lista_3 = [10, 20, 30]
lista_4 = lista_3

print(id(lista_3))
# 140145503124800
print(id(lista_4))
# 140145503124800
print(lista_3 is lista_4)
# True

lista_4.append(40)
lista_3
# [10, 20, 30, 40]

lista_4
# [10, 20, 30, 40]

print(id(lista_3))
# 139906309410112
print(id(lista_4))
# 139906309410112
print(lista_3 is lista_4)
# True

lista_3 = [10, 20, 30, 40]
lista_5 = lista_3.copy()
lista_3.append(50)

print(lista_3)
#[10, 20, 30, 40, 50]
print(lista_5)
#[10, 20, 30, 40]
print(id(lista_3))
# 139786662853760
print(id(lista_5))
# 139786662853824
print(lista_3 is lista_5)
# False


def func_param(lista, numero):
    lista.append(100)
    numero = numero + 50
    print(f'Lista dentro da função: {lista}')
    # Lista dentro da função: [5, 25, 50, 100]
    print(f'Número dentro da função: {numero}')
    # Número dentro da função: 75


minha_lista = [5, 25, 50]
numero_inteiro = 25

print(f'Lista antes da chamada da função: {minha_lista}')
# Lista antes da chamada da função: [5, 25, 50]
print(f'Inteiro antes da chamada da função: {numero_inteiro}')
# Inteiro antes da chamada da função: 25
print('*' * 50)
# **************************************************
func_param(minha_lista, numero_inteiro)
print('*' * 50)
# **************************************************
print(f'Lista fora do escopo da função {minha_lista}')
# Lista fora do escopo da função [5, 25, 50, 100]
print(f'Inteiro fora do escopo da da função: {numero_inteiro}')
# Inteiro fora do escopo da da função: 25
