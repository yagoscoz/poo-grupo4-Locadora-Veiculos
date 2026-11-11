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