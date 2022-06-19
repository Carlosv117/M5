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

        if(self.funcionarios.count(funcionario) > 0 or funcionario.funcao == "Gerente" or funcionario.empresa != self.empresa):
            return False

        self.funcionarios.append(funcionario)
        return True

    def aumento_salarial(self, funcionario: Funcionario, empresa):
        if isinstance(funcionario, Funcionario) == False or funcionario not in self.funcionarios:
            return False
        added_salary = (10 * funcionario.salario) / 100.0
        new_sallary = int(funcionario.salario) + int(added_salary)
        funcionario.salario = new_sallary
        if new_sallary >= 8000:
            Empresa.promocao(empresa, funcionario)
        return True
