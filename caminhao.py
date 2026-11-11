from veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, diaria_base, capacidade_toneladas):
        super().__init__(placa, modelo, diaria_base)
        self.__capacidade = 0
        self.capacidade_toneladas = capacidade_toneladas


@property
def capacidade_toneladas(self):
    return self.__capacidade