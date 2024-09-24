menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[a] Novo saldo
=> """

saldo = 0
limite = 100
extrato = ""
numero_saques = 2
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do seu saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Função para calcular o novo saldo
def calcular_novo_saldo(saldo_atual, deposito):
    return saldo_atual + deposito

# Solicitar o saldo atual da conta
saldo_atual = float(input("Digite o saldo atual da conta: R$ "))

# Solicitar o valor do depósito
deposito = float(input("Digite o valor do depósito: R$ "))

# Calcular o novo saldo
novo_saldo = calcular_novo_saldo(saldo_atual, deposito)

# Exibir o novo saldo
print(f"O novo saldo após o depósito é: R$ {novo_saldo:.2f}")
