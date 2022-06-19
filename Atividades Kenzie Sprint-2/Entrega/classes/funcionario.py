from datetime import datetime
import re


class Funcionario:

    funcao = "Funcionário"

    def __init__(self, nome_completo: str, cpf: str, salario: int = 3000):

        self.nome_completo = re.sub(
            " {2,}", " ", nome_completo).strip(" ").title()
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):

        return f"<{self.funcao}: {self.nome_completo}>"
