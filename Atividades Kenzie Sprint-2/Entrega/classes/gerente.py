import re
from .funcionario import Funcionario


class Gerente(Funcionario):

    funcao = "Gerente"

    def __init__(self, nome_completo: str, cpf: str, salario: int = 8000, funcionarios=[]):

        self.nome_completo = re.sub(
            " {2,}", " ", nome_completo).strip(" ").title()
        self.cpf = cpf
        self.salario = salario
        self.funcionarios = funcionarios

    def __len__(self):

        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario: Funcionario):

        if (
            funcionario.funcao == "Gerente"
        ):
            return False

        self.funcionarios.append(funcionario)
        return True

    def aumento_salarial(self, funcionario: Funcionario, empresa):

        for empregado in self.funcionarios:
            if empregado.cpf == funcionario.cpf:
                funcionario.salario = round(funcionario.salario * 1.1)
                if funcionario.salario > 8000:
                    funcionario = Gerente(
                        funcionario.nome_completo,
                        funcionario.cpf,
                        funcionario.salario
                    )
                return funcionario
        return False
