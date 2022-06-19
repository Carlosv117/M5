import re
import os
import json
from datetime import datetime
from .funcionario import Funcionario
from .gerente import Gerente


class Empresa:

    def __init__(self, nome: str, cnpj: str, contratados: list = []):

        self.nome = re.sub(" {2,}", " ", nome).strip(" ").title()
        self.cnpj = cnpj
        self.contratados = contratados

    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self, funcionario: Funcionario):

        for func in self.contratados:
            if func.cpf == funcionario.cpf:
                return "Funcionário com esse CPF já foi contratado."
        self.contratados.append(funcionario)

        nome_email = funcionario.nome_completo.replace(" ", "")
        nome_empresa_email = self.nome.replace(" ", "")
        funcionario.email = f"{nome_email.lower()}@{nome_empresa_email.lower()}.com"

        funcionario.empresa = self.nome
        return "Funcionário contratado!"

    def gerar_holerite(self, funcionario: Funcionario):

        if funcionario in self.contratados:
            empresa = self.nome.replace(" ", "_").lower()
            empregado = {
                "nome": funcionario.nome_completo,
                "cpf": funcionario.cpf,
                "salario": funcionario.salario,
                "mes": datetime.now().strftime("%B"),
                "admissao": funcionario.admissao
            }
            funcionario_diretorio = funcionario.nome_completo.replace(
                " ", "_").lower()

            if os.path.exists(f"./Entrega/empresas/{empresa}"):
                pass
            else:
                os.mkdir(f"./Entrega/empresas/{empresa}")

            if os.path.exists(f"./Entrega/empresas/{empresa}/{funcionario_diretorio}.json"):
                return f"Funcionario já cadastrado na empresa {empresa}!"
            else:
                with open(f"./Entrega/empresas/{empresa}/{funcionario_diretorio}.json", "w") as file:
                    json.dump(empregado, file, indent=4)

            return True
        return False

    def ler_holerite(self, funcionario: Funcionario):

        empresa = self.nome.replace(" ", "_").lower()
        funcionario_nome_completo = funcionario.nome_completo.replace(
            " ", "_").lower()

        funcionario_holerite = f"./Entrega/empresas/{empresa}/{funcionario_nome_completo}.json"

        verificar_holerite = os.path.isfile(funcionario_holerite)

        if not verificar_holerite:
            return "Holerite não gerado!"

        return open(funcionario_holerite, "r").read()

    def demissao(self, funcionario: Funcionario):

        if isinstance(funcionario, Gerente):
            self.contratados.remove(funcionario)
            return "Gerente demitido!"

        elif isinstance(funcionario, Funcionario):

            for empregado in self.contratados:
                if empregado.cpf != funcionario.cpf:
                    return "Não consta esse CPF na empresa"
                else:
                    self.contratados.remove(funcionario)

            for empregados in self.contratados:
                if isinstance(empregados, Gerente):
                    if funcionario in empregados.funcionarios:
                        empregados.funcionarios.remove(funcionario)
                        return "Funcionário demitido!"

        else:
            return False

    def promocao(self, funcionario: Funcionario):
        ...
        # if isinstance(funcionario, Funcionario) == False or funcionario not in self.contratados or isinstance(funcionario, Gerente):
        #     return False
        # self.contratados.remove(funcionario)
        # if funcionario.salario > 8000:
        #     promoved_employ = Gerente(
        #         funcionario.nome, funcionario.sobrenome, funcionario.cpf, funcionario.salario)
        # else:
        #     promoved_employ = Gerente(
        #         funcionario.nome_completo, funcionario.cpf)
        # self.contratar_funcionario(promoved_employ)
        # return True

        # Empresa.demissao(self, funcionario)
        # new_manager = Gerente(funcionario.nome_completo,
        #                       funcionario.cpf, funcionario.salario)
        # self.contratar_funcionario(new_manager)
        # return new_manager
