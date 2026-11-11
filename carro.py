from veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, placa, modelo, diaria_base, portas):
        super().__init__(placa, modelo, diaria_base)
        self.__portas = 0
        self.portas = portas


@property
def portas(self):
    return self.__portas