import re
from funcionarios import Funcionario


class Empresa:
    def __init__(self, nome: str, cnpj: str, contratados: list = []):
        self.nome = re.sub(" {2,}", " ", nome).strip(" ").title()
        self.cnpj = cnpj
        self.contratados = contratados

    def __len__(self):
        return f"{len(self.contratados)} funcionario(s) contratado(s)"

    def contratar_funcionario(self, funcionario):
        email = f"{funcionario.nome_completo}@{self.nome}.com"
        empresa = self.nome

        esta_contratado = [
            empregado for empregado in self.contratados if empregado.cpf == funcionario.cpf]
        if(esta_contratado):
            return "Este CPF já está cadastrado"

        self.contratados.append({email: email, empresa: empresa})

    def gerar_holerite(self, funcionario):
        ...


empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
print(empresa_1.__dict__)
# {'nome': 'Kenzie Brasil', 'cnpj': 12345678910124, 'contratados': []}

# print(len(empresa_1))
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
