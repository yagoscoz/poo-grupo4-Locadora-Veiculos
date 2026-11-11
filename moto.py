from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placa, modelo, diaria_base, cilindradas):
        super().__init__(placa, modelo, diaria_base)
        self.__cilindradas = cilindradas


@property
def cilindradas(self):
    return self.__cilindradas