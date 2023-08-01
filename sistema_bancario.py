import re


titulo = " iBANK - MENU ".center(40, "_")
menu = f"""
{titulo}

 [D] Depositar
 [S] Sacar
 [E] Extrato
 [Q] Saír

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
            _valor = input("Entre com o valor [Q=Sair]: ")
            if _valor == "":
                ...
            elif _valor in "Qq":
                break
            elif re.findall("[a-zA-Z]", _valor):
                print("*** APENAS NÚMEROS ***".center(40))
            else:
                if "," in _valor:
                    _valor = _valor.replace(",", ".")
                if float(_valor) < 0:
                    print("*** APENAS VALORES POSITIVOS ***".center(40))
                else:
                    valor = round(float(_valor), 2)
                    saldo += valor
                    extrato += f"{' DEP '.ljust(25, '.')} R$ {valor:10.2f}\n"
                    print(" Depósito realizado com sucesso! ".center(40, "-"))
                    print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")
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

            _valor = input("Entre com o valor [Q=Sair]: ")
            if _valor == "":
                ...
            elif _valor in "Qq":
                break
            elif re.findall("[a-zA-Z]", _valor):
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
                    print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")
                else:
                    numero_saques += 1
                    valor = round((float(_valor) * -1), 2)
                    saldo += valor
                    extrato += f"{' SAQ '.ljust(25, '.')} R$ {valor:10.2f}\n"
                    print(" Saque realizado com sucesso! ".center(40, "-"))
                    print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")
                    print(
                        "*** SAQUES RESTANTES: {} ***".format(
                            LIMITE_SAQUES - numero_saques
                        ).center(40)
                    )
                    break

    elif opcao in "Ee":
        print(" Extrato ".center(40, "-"))
        print(extrato)
        print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")

    elif opcao in "Qq":
        print(" Obrigado por usar nossos serviços! ".center(40))
        break

    else:
        print("*** OPERAÇÃO INVÁLIDA ***".center(40))
        print(" Selecione uma operação válida ".center(40))
