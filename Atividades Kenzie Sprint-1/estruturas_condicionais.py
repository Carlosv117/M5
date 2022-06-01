x = 1
y = 2
print(x > y)
# False

print(x != y)
# True

print(2 > 1 and 5 < 3)
# False

print(2 > 1 or 5 < 3)
# True

print(not(0 == 0))
# False

# A função input serve para capturarmos os
# dados inseridos pelo usuário. O valor inserido
# sempre virá como uma string.
entrada = input("Digite a nota: ")

# convertemos nossa string para float
nota = float(entrada)

# verificamos se a nota é maior ou igual a 8
if nota >= 8.0:
    # dizemos que o aluno foi aprovado caso sua nota seja 8 ou superior
    print(f'Sua média é {nota}, logo, você está aprovado')

# se a nota for menor que 8, o programa diz que o aluno está reprovado
if nota < 8.0:
    print(f'Sua média é {nota}, logo, você não está aprovado')

# or

entrada = input("Digite a nota: ")
nota = float(entrada)
if nota >= 8.0:
    print(f'Sua média é {nota}, logo, você está aprovado')
else:
    # se a nota for menor do que 8, esse bloco será executado
    print(f'Sua média é {nota}, logo, você não está aprovado')

# or

entrada = input("Digite a nota: ")
nota = float(entrada)
if nota >= 8.0:
    print(f'Sua média é {nota}, logo, você está aprovado')
elif nota >= 4.0 and nota <= 6.0:
    print(f'Sua nota é {nota}, portanto você está de recuperação')
elif nota > 6 and nota < 8:
    print(
        f'Sua nota é {nota}, você está aprovado, porém com ressalvas, fique atento')
else:
    print(f'Sua média é {nota}, logo, você não está aprovado')
