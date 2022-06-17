# Objetos de classe

class VeiculoAutomotor:
    cor = "branca"

    def get_cor(self):
        print("A cor do veiculo é", self.cor)


print(VeiculoAutomotor.cor)
print(VeiculoAutomotor.get_cor)
print(VeiculoAutomotor.__doc__)


veiculo = VeiculoAutomotor()
print(veiculo.cor)

print(VeiculoAutomotor.get_cor)
print(veiculo.get_cor)

veiculo.get_cor()

# Método __init__


class VeiculoAutomotorRodas:
    cor = "branca"

    def __init__(self, rodas):
        self.rodas = rodas

    def get_cor(self):
        print("A cor do veiculo é", self.cor)


veiculo = VeiculoAutomotorRodas(4)

print(veiculo.rodas)
