from Classes.locadora import Locadora
from Classes.carro import Carro
from Classes.moto import Moto
from Classes.caminhao import Caminhao


def ler_numero(texto, tipo=float):
    while True:
        try:
            return tipo(input(texto))
        except ValueError:
            print("Valor inválido. Tente novamente.")


def cadastrar_veiculo(locadora):
    print("\n1-Carro  2-Moto  3-Caminhão")
    tipo = input("Tipo: ").strip()
    placa = input("Placa: ").strip()
    modelo = input("Modelo: ").strip()
    diaria = ler_numero("Diária base (R$): ")
    if tipo == "1":
        veiculo = Carro(placa, modelo, diaria, ler_numero("Portas: ", int))
    elif tipo == "2":
        veiculo = Moto(placa, modelo, diaria, ler_numero("Cilindradas: ", int))
    elif tipo == "3":
        veiculo = Caminhao(placa, modelo, diaria, ler_numero("Capacidade (t): "))
    else:
        print("Tipo inválido.")
        return
    locadora.cadastrar(veiculo)
    print("Veículo cadastrado com sucesso!")


def main():
    locadora = Locadora("G4 : Locadora do quadrizal")
    while True:
        print(f"\n=== {locadora.nome} ===")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Buscar por placa")
        print("4 - Calcular tarifas")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_veiculo(locadora)
        elif opcao == "2":
            print(locadora.listar())
        elif opcao == "3":
            veiculo = locadora.buscar(input("Placa: ").strip())
            print(veiculo if veiculo else "Veículo não encontrado.")
        elif opcao == "4":
            print(locadora.calcular_tarifas(ler_numero("Dias: ", int)))
        elif opcao == "0":
            print("Encerrando. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()