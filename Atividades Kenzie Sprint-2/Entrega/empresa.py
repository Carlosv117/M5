import re
import os
import json
from datetime import datetime
from funcionario import Funcionario
from gerente import Gerente
# import gerente


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
        empresa = re.sub(" {2,}", " ", self.nome).strip(" ").title()
        funcionario_nome_completo = re.sub(
            " {2,}", " ", funcionario.nome_completo).strip(" ").title()

        funcionario_holerite = f"./empresas/{empresa}/{funcionario_nome_completo}.json"

        verificar_holerite = os.path.isfile(funcionario_holerite)

        if not verificar_holerite:
            return "Holerite não gerado!"

        return open(funcionario_holerite, "r").read()

    def demissao(self, funcionario: Funcionario):
        if isinstance(funcionario, Gerente):
            self.contratados.remove(funcionario)
            return "Gerente demitido!"
        elif isinstance(funcionario, Funcionario):
            self.contratados.remove(funcionario)
            for empregados in self.contratados:
                if isinstance(empregados, Gerente):
                    if funcionario in empregados.funcionarios:
                        empregados.funcionarios.remove(funcionario)
            return "Funcionário demitido!"

        else:
            return False


empresa_1 = Empresa("  kenzie   brasil ", 12345678910124)
funcionario_1 = Funcionario(" jordan  cardoso poole ", 32112343215)
gerente_1 = Gerente(" bill    gates ", "32132186712")
gerente_3 = Gerente("elon musk", "12342186574")
# Adicionando funcionários
empresa_1.contratar_funcionario(funcionario_1)
empresa_1.contratar_funcionario(gerente_1)
empresa_1.contratar_funcionario(gerente_3)
# Adicionando funcionário ao gerente
gerente_1.adicionar_funcionario(funcionario_1)
# Funcionário não contratado
funcionario_4 = Funcionario("klay mota thompson ", 92478965434)

empresa_1.gerar_holerite(funcionario_1)
holerite = Empresa.ler_holerite(empresa_1, funcionario_1)
print(holerite)
# {
#  'nome': 'Jordan Cardoso Poole',
#  'cpf': 32112343215,
#  'salario': 3000,
#  'mes': 'May',
#  'admissao':
#  '27-05-2022'
# }
