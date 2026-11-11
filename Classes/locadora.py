class Locadora:
    def __init__(self, nome):
        self.__nome = nome
        self.__veiculos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def veiculos(self):
        return list(self.__veiculos)

    def cadastrar(self, veiculo):
        if self.buscar(veiculo.placa):
            raise ValueError("Já existe um veículo com essa placa.")
        self.__veiculos.append(veiculo)

    def buscar(self, placa):
        for veiculo in self.__veiculos:
            if veiculo.placa.upper() == placa.upper():
                return veiculo
        return None

    def listar(self):
        if not self.__veiculos:
            return "Nenhum veículo cadastrado."
        return "\n".join(str(v) for v in self.__veiculos)

    def calcular_tarifas(self, dias):

        linhas = []
        for veiculo in self.__veiculos:
            valor = veiculo.calcular_tarifa(dias)
            linhas.append(f"{veiculo.modelo} ({type(veiculo).__name__}): "
                          f"R$ {valor:.2f} por {dias} dia(s)")
        return "\n".join(linhas) if linhas else "Nenhum veículo cadastrado."

    def __str__(self):
        return f"Locadora {self.__nome} - {len(self.__veiculos)} veículo(s)"
