from datetime import datetime


class Funcionario:
    funcao = "Funcionário"

    def __init__(self, nome_completo: str, cpf, salario: int = 3000) -> None:
        self.nome_completo = nome_completo.title().strip()
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f'<{self.funcao}: {self.nome_completo}>'
