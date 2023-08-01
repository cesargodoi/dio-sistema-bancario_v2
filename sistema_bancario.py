import re


menu = """

[D] Depositar
[S] Sacar
[e] Extrato
[q] Saír

=> """

saldo = 0.0
LIMITE = 500.0
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
                print("*** APENAS NÚMEROS ***".center(40))
            else:
                if "," in _valor:
                    _valor = _valor.replace(",", ".")
                if float(_valor) < 0:
                    print("*** APENAS VALORES POSITIVOS ***".center(40))
                else:
                    valor = round(float(_valor), 2)
                    saldo += valor
                    extrato += f"{' DEP '.ljust(24, '.')} R$  {valor:10.2f}"
                    print(" Depósito realizado com sucesso! ".center(40, "-"))
                    print(
                        f"{' SALDO ATUAL '.ljust(24, '.')} R$  {saldo:10.2f}"
                    )
                    break

    elif opcao in "Ss":
        print(" Saque ".center(40, "-"))

        while True:
            if saldo == 0.0:
                print("*** VOCÊ NÃO POSSUI SALDO ***".center(40))
                break
            if numero_saques == LIMITE_SAQUES:
                print("*** LIMITE DIÁRIO DE SAQUES ESGOTAGO ***".center(40))
                print("*** VOLTE AMANHÃ! ***".center(40))
                break

            _valor = input("Entre com o valor do saque: ")
            if re.findall("[a-zA-Z]", _valor):
                print("*** APENAS NÚMEROS ***".center(40))
            else:
                if "," in _valor:
                    _valor = _valor.replace(",", ".")
                if float(_valor) < 0:
                    print("*** APENAS VALORES POSITIVOS ***".center(40))
                elif float(_valor) > LIMITE:
                    print(
                        f"*** LIMITE POR SAQUE: R$ {LIMITE:.2f} ***".center(40)
                    )
                elif float(_valor) > saldo:
                    print("*** SEU SALDO NÃO É SUFICIENTE ***".center(40))
                    print(
                        f"{' SALDO ATUAL '.ljust(24, '.')} R$  {saldo:10.2f}"
                    )
                else:
                    numero_saques += 1
                    valor = round(float(_valor), 2)
                    saldo -= valor
                    extrato += f"{' SAQ '.ljust(24, '.')} R$ -{valor:10.2f}"
                    print(" Saque realizado com sucesso! ".center(40, "-"))
                    print(
                        f"{' SALDO ATUAL '.ljust(24, '.')} R$  {saldo:10.2f}"
                    )
                    print(
                        "*** SAQUES RESTANTES: {} ***".format(
                            LIMITE_SAQUES - numero_saques
                        ).center(40)
                    )
                    break

    elif opcao == "e":
        print(" Estrato ")

    elif opcao == "q":
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente a operação desejada"
        )
