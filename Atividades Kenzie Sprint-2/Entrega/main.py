from classes.funcionario import Funcionario
from classes.empresa import Empresa
from classes.gerente import Gerente

if __name__ == "__main__":

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_4 = Funcionario("klay mota thompson ", "92478965434")
    gerente_3 = Gerente("elon musk", "12342186574")
    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
    # Contratação do funcionário
    empresa_1.contratar_funcionario(funcionario_1)

    resposta = empresa_1.promocao(gerente_3)
    print(resposta)
    # False
    resposta = empresa_1.promocao(funcionario_4)
    print(resposta)
    # False
    print(funcionario_1.funcao)
    # Funcionário
    resposta = empresa_1.promocao(funcionario_1)
    print(resposta.funcao)
    # Gerente

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_4 = Funcionario("klay mota thompson ", "92478965434")
    gerente_1 = Gerente(" bill    gates ", "32132186712")
    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")

    # Contratação dos funcionários
    empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(gerente_1)

    # Adicionar funcionário ao gerente
    gerente_1.adicionar_funcionario(funcionario_1)

    resposta = gerente_1.aumento_salarial(funcionario_4, empresa_1)
    print(resposta)
    # False
    print(funcionario_1.salario)
    # 3000
    resposta = gerente_1.aumento_salarial(funcionario_1, empresa_1)
    print(resposta.funcao)
    # Funcionário
    print(resposta.salario)
    # 3300

    # Aqui vamos setar um valor alto para teste
    funcionario_1.salario = 7500
    print(funcionario_1.salario)
    # 7500
    resposta = gerente_1.aumento_salarial(funcionario_1, empresa_1)
    print(resposta.funcao)
    # Gerente
    print(resposta.salario)
    # 8250
