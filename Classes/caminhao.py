from Classes.veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, diaria_base, capacidade_toneladas):
        super().__init__(placa, modelo, diaria_base)
        self.__capacidade = 0
        self.capacidade_toneladas = capacidade_toneladas

    @property
    def capacidade_toneladas(self):
        return self.__capacidade

    @capacidade_toneladas.setter
    def capacidade_toneladas(self, valor):
        if valor <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self.__capacidade = valor

    def carregar(self, toneladas):
        if toneladas > self.__capacidade:
            return "Carga acima da capacidade!"
        return f"{toneladas}t carregadas com sucesso."

    def calcular_tarifa(self, dias):
        return (self.diaria_base + 15 * self.__capacidade) * dias

    def __str__(self):
        return (f"[Caminhão] {super().__str__()} | "
                f"Capacidade: {self.__capacidade}t")