import re
import os
import json
from datetime import datetime
from funcionarios import Funcionario


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

        nome_emial = funcionario.nome_completo.replace(" ", "")
        nome_empresa_emial = self.nome.replace(" ", "")
        funcionario.email = f"{nome_emial.lower()}@{nome_empresa_emial.lower()}.com"

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
                pass
            else:
                with open(f"./Entrega/empresas/{empresa}/{funcionario_diretorio}.json", "w") as file:
                    json.dump(empregado, file, indent=4)

            return True
        return False


empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
print(empresa_1.__dict__)
# {'nome': 'Kenzie Brasil', 'cnpj': 12345678910124, 'contratados': []}

print(f'CONTRATADOS: {len(empresa_1)}')
# 0

funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
funcionario_2 = Funcionario("  stephen  alves curry ", "12332145665")

# CPF CORRETO
resposta = empresa_1.contratar_funcionario(funcionario_1)
empresa_1.contratar_funcionario(funcionario_2)
print(resposta)
# Funcionário contratado!
print(f'CONTRATADOS: {len(empresa_1)}')
# CONTRATADOS: 2
print(f'EMAIL: {funcionario_1.email}')
# Email: jordan_cardoso_poole@kenziebrasil.com
print(f'Empresa: {funcionario_1.empresa}')
# Empresa: Kenzie Brasil

# CPF REPETIDO
resposta = empresa_1.contratar_funcionario(funcionario_2)
print(resposta)
# Funcionário com esse CPF já foi contratado.

# Ao executar esse método deverá gerar o diretório e arquivo na pasta empresas
holerite = empresa_1.gerar_holerite(funcionario_1)
print(holerite)
# True

# Funcionario não contratado
funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
holerite = empresa_1.gerar_holerite(funcionario_3)
print(holerite)
# False
