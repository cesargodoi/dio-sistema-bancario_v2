import re


menu = """

[D] Depositar
[s] Sacar
[e] Extrato
[q] Saír

=> """

saldo = 0.0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao in "Dd":
        print(" Depósito ".center(40, "-"))

        while True:
            _valor = input("Entre com o valor do depósito: ")
            if re.findall("[a-zA-Z]", _valor):
                print("*** APENAS NÚMEROS ***")
            else:
                if "," in _valor:
                    _valor = _valor.replace(",", ".")
                if float(_valor) < 0:
                    print("*** APENAS VALORES POSITIVOS ***")
                else:
                    valor = round(float(_valor), 2)
                    saldo += valor
                    extrato += f"{' DEP '.ljust(25, '.')} R$ {valor:10.2f}"
                    break

        print(" Depósito realizado com sucesso! ".center(40, "-"))
        print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")

    elif opcao == "s":
        print("Sacar")

    elif opcao == "e":
        print(" Estrato ")

    elif opcao == "q":
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente a operação desejada"
        )
