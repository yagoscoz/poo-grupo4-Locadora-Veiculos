from Classes.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placa, modelo, diaria_base, cilindradas):
        super().__init__(placa, modelo, diaria_base)
        self.__cilindradas = cilindradas


@property
def cilindradas(self):
    return self.__cilindradas


@cilindradas.setter
def cilindradas(self, valor):
    if valor <= 0:
        raise ValueError("As cilindradas devem ser maiores que zero.")
    self.__cilindradas = valor


def empinar(self):
    return f"A {self.modelo} está empinando! (só no filme) "


def calcular_tarifa(self, dias):
    return self.diaria_base * 0.9 * dias


def __str__(self):
    return f"[Moto] {super().__str__()} | {self.__cilindradas} cc"