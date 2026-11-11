class Veiculo:
    def __init__(self, placa, modelo, diaria_base):
        self.__placa = placa
        self.__modelo = modelo
        self.__diaria_base = 0
        self.__disponivel = True
        self.diaria_base = diaria_base


@property
def placa(self):
    return self.__placa


@property
def modelo(self):
    return self.__modelo


@property
def diaria_base(self):
    return self.__diaria_base


@diaria_base.setter
def diaria_base(self, valor):
    if valor <= 0:
        raise ValueError("A diária deve ser maior que zero.")
    self.__diaria_base = valor


@property
def disponivel(self):
    return self.__disponivel


@disponivel.setter
def disponivel(self, valor):
    self.__disponivel = bool(valor)


def calcular_tarifa(self, dias):
    return self.__diaria_base * dias


def __str__(self):
    status = "Disponível" if self.__disponivel else "Alugado"
    return (f"{self.__modelo} | Placa: {self.__placa} | "
            f"" f"Diária base: R$ {self.__diaria_base:.2f} | {status}")