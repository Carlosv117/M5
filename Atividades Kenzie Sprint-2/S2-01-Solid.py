# SOLID

# S - Princípio da responsabilidade única

class Conta:
    def __init__(self, numero_da_conta: str):
        self.numero_da_conta = numero_da_conta

    def entregar_numero_da_conta(self):
        return self.numero_da_conta

    def salvar(self):
        # salva os dados da conta no banco de dados
        ...


""""""


class ContaDB:
    def buscar_numero_da_conta(self, _id):
        ...

    def salvar_conta(self, conta):
        ...


class Conta:
    def __init__(self, numero_da_conta: str):
        self.numero_da_conta = numero_da_conta
        self._db = ContaDB()

    def entregar_numero_da_conta(self):
        return self.numero_da_conta

    def buscar(self, _id):
        # _id recebido pela requisição
        return self._db.buscar_numero_da_conta(_id=_id)

    def salvar(self):
        self._db.salvar_conta(conta=self)


# O - Princípio Aberto-Fechado

class Desconto:
    def __init__(self, cliente, preco):
        self.cliente = cliente
        self.preco = preco

    def dar_desconto(self):
        if self.cliente == 'comum':
            return self.preco * 0.2
        elif self.cliente == 'vip':
            return self.preco * 0.4


""""""


def dar_desconto(self):
    if self.customer == 'normal':
        return self.preco * 0.2
    elif self.customer == 'vip':
        return self.preco * 0.4
    elif self.customer == 'supervip':
        return self.preco * 0.8


""""""


class Desconto:
    def __init__(self, cliente, preco):
        self.cliente = cliente
        self.preco = preco

    def dar_desconto(self):
        return self.preco * 0.2


class VIPDesconto(Desconto):
    def dar_desconto(self):
        return super().dar_desconto() * 2


class SuperVIPDesconto(VIPDesconto):
    def dar_desconto(self):
        return super().dar_desconto() * 2

# L - Princípio da substituição de Liskov


class Veiculo:
    def __init__(self, nome: str, velocidade: float):
        self.nome = nome
        self.velocidade = velocidade

    def pegar_nome(self) -> str:
        return f"Nome do veículo: {self.nome}"

    def pegar_velocidade(self) -> str:
        return f"Velocidade do veículo {self.velocidade}"

    def motor(self):
        ...

    def ligar_motor(self):
        self.motor()


class Carro(Veiculo):
    def ligar_motor(self):
        ...


class Bicicleta(Veiculo):
    def ligar_motor(self):
        ...


""""""


class Veiculo:
    def __init__(self, nome: str, velocidade: float):
        self.nome = nome
        self.velocidade = velocidade

    def pegar_nome(self) -> str:
        return f"Nome do veículo: {self.nome}"

    def pegar_velocidade(self) -> str:
        return f"Velocidade do veículo {self.velocidade}"


class VeiculoSemMotor(Veiculo):
    def iniciar_movimento(self):
        ...


class VeiculoComMotor(Veiculo):
    def motor(self):
        ...

    def ligar_motor(self):
        self.motor()


class Carro(VeiculoComMotor):
    def ligar_motor(self):
        ...


class Bicicleta(VeiculoSemMotor):
    def iniciar_movimento(self):
        ...

# I - Princípio da Segregação da Interface


class FormaGeometrica:
    def desenhar_circulo(self):
        raise NotImplementedError

    def desenhar_quadrado(self):
        raise NotImplementedError


class Circulo(FormaGeometrica):
    def desenhar_circulo(self):
        ...

    def desenhar_quadrado(self):
        ...


""""""


class FormaGeometrica:
    def desenhar(self):
        raise NotImplementedError


class Circulo(FormaGeometrica):
    def desenhar(self):
        ...


class Quadrado(FormaGeometrica):
    def desenhar(self):
        ...


# D - Princípio da Inversão de Dependência

class Lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False


class Botao:
    def __init__(self, lampada):
        self.lampada = lampada

    def acionar(self):
        if self.lampada.ligada:
            self.lampada.desligar()
        else:
            self.lampada.ligar()


""""""


class Dispositivo:
    def __init__(self):
        self.em_funcionamento = False

    def ligar(self):
        raise NaoImplementadoError

    def desligar(self):
        raise NaoImplementadoError


class Lampada(Dispositivo):
    def __init__(self):
        super().__init__()

    def ligar(self):
        self.em_funcionamento = True

    def desligar(self):
        self.em_funcionamento = False


class Botao:
    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo  # nesse exemplo, uma lampada

    def acionar(self):
        if self.dispositivo.em_funcionamento:
            self.dispositivo.desligar()
        else:
            self.dispositivo.ligar()
