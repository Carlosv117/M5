import os

resposta = input("Digite o nome do seu pet: ")
print(f"O nome do seu pet é {resposta}")

while True:
    resposta = input("Digite o nome do seu pet: ")
    print(f"O nome do seu pet é {resposta}")

    print("\nDigite quit para sair do sistema")
    escolha_final = input()

    if escolha_final == "quit":
        break


while True:
    # Podemos começar já limpando a tela
    os.system("clear")

    resposta = input("Digite o nome do seu pet: ")
    print(f"O nome do seu pet é {resposta}")

    print("\nDigite quit para sair do sistema")
    escolha_final = input()

    if escolha_final == "quit":
        break

    # Se o usuário não digitar "quit",
    # o loop reiniciará e a limpeza de tela
    # ocorrerá novamente.


def pet_name_screen():
    while True:
        os.system("clear")

        resposta = input("Digite o nome do seu pet: ")
        print(f"O nome do seu pet é {resposta}")

        print("\nDigite v para voltar a tela anterior")
        escolha_final = input()

        if escolha_final == "v":
            break


def welcome_screen():
    while True:
        os.system("clear")

        print(f"O que deseja fazer ?")
        print(f"A. Contar o nome do meu pet")
        print(f"B. Finalizar o sistema")

        resposta = input("Digite a opção: ")

        if resposta.upper() == "A":
            pet_name_screen()
        elif resposta.upper() == "B":
            print("Até logo!")
            break
        else:
            print("Digite uma opção válida (A ou B)\n")


welcome_screen()


# main.py
...


def welcome_screen():
    # Ao chamar a função, a tela é limpa uma única vez
    # inicialmente
    os.system("clear")
    while True:
        print(f"O que deseja fazer ?")
        print(f"A. Contar o nome do meu pet")
        print(f"B. Finalizar o sistema")

        resposta = input("Digite a opção: ")

        if resposta.upper() == "A":
            pet_name_screen()
        elif resposta.upper() == "B":
            print("Até logo!")
            break
        else:
            # Aqui, limpamos a tela e printamos nossa mensagem
            # de aviso, que será seguida de uma nova iteração
            # do loop, que não está mais limpando a tela
            # toda vez
            os.system("clear")
            print("Digite uma opção válida (A ou B)\n")


welcome_screen()
