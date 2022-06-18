import re
from funcionarios import Funcionario
from empresa import Empresa


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


# gerente_1 = Gerente(" bill    gates ", "32132186712", 10000)
# print(gerente_1.__dict__)
# # {
# #  'nome_completo': 'Bill Gates',
# #  'cpf': '32132186712',
# #  'salario': 10000,
# #  'admissao': '27-05-2022',
# #  'funcionarios': []
# # }

# print(len(gerente_1))
# # 0

# empresa_1 = Empresa("  kenzie    brasil ", "12345678910124")
# funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
# gerente_2 = Gerente("steve  kerr ", "76532186123")
# # Contratando funcionários
# empresa_1.contratar_funcionario(funcionario_1)
# empresa_1.contratar_funcionario(gerente_1)
# empresa_1.contratar_funcionario(gerente_2)
# # Empresa diferente
# empresa_2 = Empresa(" golden state warriors  ", "12345678910111")
# funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
# empresa_2.contratar_funcionario(funcionario_3)

# resposta = gerente_1.adicionar_funcionario(funcionario_1)
# print(resposta)
# # True
# resposta = gerente_1.adicionar_funcionario(funcionario_1)
# print(resposta)
# # False
# resposta = gerente_1.adicionar_funcionario(gerente_2)
# print(resposta)
# # False
# resposta = gerente_1.adicionar_funcionario(funcionario_3)
# print(resposta)
# # False
# print(f'FUNCIONARIOS: {len(gerente_1)}')
# # FUNCIONARIOS: 1
