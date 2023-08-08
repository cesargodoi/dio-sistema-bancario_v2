import re


LG = 80
LIMITE = 500.0
LIMITE_SAQUES = 3

titulo = " iBANK - MENU ".center(LG, "_")
menu = f"""
{titulo}

 [D]   Depositar
 [S]   Sacar
 [E]   Extrato
 [LU]  Listar Usuários
 [CU]  Cadastrar Usuário
 [LC]  Listar Contas
 [CC]  Criar Conta Corrente
 [Q]   Saír

=> """

saldo = 0.0
extrato = ""
numero_saques = 0
usuarios = [
    {
        "nome": "João Pires Correia",
        "nascimento": "12/03/1998",
        "cpf": "24374653672",
        "endereco": "R. Arlindo Gama, 395 - Campo Belo - São Paulo/SP",
    },
    {
        "nome": "Merlindo Alfonso Penna",
        "nascimento": "24/05/1983",
        "cpf": "24353442672",
        "endereco": "Av. Chavier Pinto, 12 - Santana - São Paulo/SP",
    },
]
contas_corrente = [
    {"agencia": "0001", "numero_conta": 1, "usuario": "24374653672"},
    {"agencia": "0001", "numero_conta": 2, "usuario": "24353442672"},
]


# funções
def deposito(saldo, extrato):
    print(" Depósito ".center(LG, "-"))
    while True:
        _valor = input("Entre com o valor [Q=Sair]: ")
        if _valor == "":
            ...
        elif _valor in "Qq":
            break
        elif re.findall("[a-zA-Z]", _valor):
            print("*** APENAS NÚMEROS ***".center(LG))
        else:
            if "," in _valor:
                _valor = _valor.replace(",", ".")
            if float(_valor) < 0:
                print("*** APENAS VALORES POSITIVOS ***".center(LG))
            else:
                valor = round(float(_valor), 2)
                saldo += valor
                extrato += f"{' DEP '.ljust(LG - 15, '.')} R$ {valor:10.2f}\n"
                print(" Depósito realizado com sucesso! ".center(LG, "-"))
                print(
                    f"{' SALDO ATUAL '.ljust(LG - 15, '.')} R$ {saldo:10.2f}"
                )
                break
    return saldo, extrato


def saque(*, saldo, extrato, numero_saques):
    print(" Saque ".center(LG, "-"))
    while True:
        if saldo == 0.0:
            print("*** VOCÊ NÃO POSSUI SALDO ***".center(LG))
            break
        if numero_saques == LIMITE_SAQUES:
            print("*** LIMITE DIÁRIO DE SAQUES ESGOTAGO ***".center(LG))
            print("*** VOLTE AMANHÃ! ***".center(LG))
            break

        _valor = input("Entre com o valor [Q=Sair]: ")
        if _valor == "":
            ...
        elif _valor in "Qq":
            break
        elif re.findall("[a-zA-Z]", _valor):
            print("*** APENAS NÚMEROS ***".center(LG))
        else:
            if "," in _valor:
                _valor = _valor.replace(",", ".")
            if float(_valor) < 0:
                print("*** APENAS VALORES POSITIVOS ***".center(LG))
            elif float(_valor) > LIMITE:
                print(f"*** LIMITE POR SAQUE: R$ {LIMITE:.2f} ***".center(LG))
            elif float(_valor) > saldo:
                print("*** SEU SALDO NÃO É SUFICIENTE ***".center(LG))
                print(f"{' SALDO ATUAL '.ljust(25, '.')} R$ {saldo:10.2f}")
            else:
                numero_saques += 1
                valor = round((float(_valor) * -1), 2)
                saldo += valor
                extrato += f"{' SAQ '.ljust(LG - 15, '.')} R$ {valor:10.2f}\n"
                print(" Saque realizado com sucesso! ".center(LG, "-"))
                print(
                    f"{' SALDO ATUAL '.ljust(LG - 15, '.')} R$ {saldo:10.2f}"
                )
                print(
                    "*** SAQUES RESTANTES: {} ***".format(
                        LIMITE_SAQUES - numero_saques
                    ).center(LG)
                )
                break
    return saldo, extrato, numero_saques


def ver_extrato(saldo, *, extrato):
    print(" Extrato ".center(LG, "-"))
    print(extrato)
    print(f"{' SALDO ATUAL '.ljust(LG - 15, '.')} R$ {saldo:10.2f}")


def get_usuario(num):
    usuario = usuarios[int(num) - 1]
    print(" Usuário ".center(LG, "-"))
    print(f"\n Nome :       {usuario['nome']}")
    print(f" Nascimento : {usuario['nascimento']}")
    print(f" CPF :        {usuario['cpf']}")
    print(f" Endereço :   {usuario['endereco']}")
    print()
    input(" Tecle qualquer tecla para sair ")


def listar_usuarios(usuarios):
    print(" Lista de Usuários ".center(LG, "-"))
    print(f" #   {'NOME'.ljust(LG - 18)} CPF")
    for n, usuario in enumerate(usuarios):
        row = " {} {} {}".format(
            str(n + 1).ljust(3), usuario["nome"].ljust(LG - 18), usuario["cpf"]
        )
        print(row)

    while True:
        num = input("\n Entre com o # para detalhes [S=Sair]: ")

        if num in "Ss":
            break
        elif re.findall(r"\d", num):
            get_usuario(num)
            listar_usuarios(usuarios)
            break
        else:
            print("*** # INVÁLIDO ***".center(LG))


def get_cpf():
    while True:
        cpf = "".join(re.findall(r"\d", input(" CPF: ")))
        if len(cpf) > 11:
            print("*** CPF INVÁLIDO (>11 DIGITOS) ***".center(LG))
        elif cpf in [usuario["cpf"] for usuario in usuarios]:
            print("*** CPF JÁ EXISTE ***".center(LG))
        else:
            return cpf


def cadastrar_usuario(usuarios):
    print(" Cadastrar Usuário ".center(LG, "-"))
    print("Entre com as informações abaixo.")
    nome = input(" Nome: ")
    nascimento = input(" Nascimento [DD/MM/YYYY]: ")
    cpf = get_cpf()
    logradouro = input(" Logradouro: ")
    numero = input(" Número: ")
    bairro = input(" Bairro: ")
    cidade = input(" Cidade: ")
    uf = input(" UF: ")
    usuario = dict(
        nome=nome,
        nascimento=nascimento,
        cpf=cpf,
        endereco=f"{logradouro}, {numero} - {bairro} - {cidade}/{uf.upper()}",
    )
    usuarios.append(usuario)
    print(" Usuário cadastrado com sucesso! ".center(LG, "-"))


def listar_contas(contas_corrente, usuarios):
    print(" Lista de Contas Corrente ".center(LG, "-"))
    print(f" #   AGENCIA  {'NÚMERO'.ljust(LG - 27)} USUÁRIO")
    for n, conta in enumerate(contas_corrente):
        row = " {} {} {} {}".format(
            str(n + 1).ljust(3),
            conta["agencia"].ljust(8),
            str(conta["numero_conta"]).ljust(LG - 27),
            conta["usuario"],
        )
        print(row)


def get_cpf_usuario():
    while True:
        cpf = "".join(
            re.findall(r"\d", input(" Entre com o CPF do Usuário: "))
        )
        if len(cpf) > 11:
            print("*** CPF INVÁLIDO (>11 DIGITOS) ***".center(LG))
        elif cpf not in [usuario["cpf"] for usuario in usuarios]:
            print("*** CPF NÃO EXISTE NO BANCO DE DADOS ***".center(LG))
        else:
            return cpf


def cadastrar_conta(contas_corrente, usuarios):
    print(" Criar Nova Conta ".center(LG, "-"))
    agencia = "0001"
    numero_conta = max([cc["numero_conta"] for cc in contas_corrente]) + 1
    usuario = get_cpf_usuario()
    nova_conta = dict(
        agencia=agencia, numero_conta=numero_conta, usuario=usuario
    )
    contas_corrente.append(nova_conta)
    print(" Conta Corrente Criada com Sucesso!".center(LG, "-"))
    nome = [usr["nome"] for usr in usuarios if usr["cpf"] == usuario][0]
    print(f" Agencia: {agencia}  C.Corrente: {numero_conta}  Usuário: {nome}")


# loop principal
while True:
    opcao = input(menu)

    if opcao in "Dd":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao in "Ss":
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            extrato=extrato,
            numero_saques=numero_saques,
        )

    elif opcao in "Ee":
        ver_extrato(saldo, extrato=extrato)

    elif opcao in "LUlu":
        listar_usuarios(usuarios)

    elif opcao in "CUcu":
        cadastrar_usuario(usuarios)

    elif opcao in "LClc":
        listar_contas(contas_corrente, usuarios)

    elif opcao in "CCcc":
        cadastrar_conta(contas_corrente, usuarios)

    elif opcao in "Qq":
        print(" Obrigado por usar nossos serviços! ".center(LG))
        break

    else:
        print("*** OPERAÇÃO INVÁLIDA ***".center(LG))
        print(" Selecione uma operação válida ".center(LG))
