def sacar(self, /, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo insuficiente!")