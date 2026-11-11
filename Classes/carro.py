from Classes.veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, placa, modelo, diaria_base, portas):
        super().__init__(placa, modelo, diaria_base)
        self.__portas = 0
        self.portas = portas


@property
def portas(self):
    return self.__portas


@portas.setter
def portas(self, valor):
    if valor < 2:
        raise ValueError("O carro deve ter pelo menos 2 portas.")
    self.__portas = valor


def ligar_ar_condicionado(self):
    return f"Ar-condicionado do {self.modelo} ligado. "


def calcular_tarifa(self, dias):
    return (self.diaria_base + 20) * dias


def __str__(self):
    return f"[Carro] {super().__str__()} | Portas: {self.__portas}"