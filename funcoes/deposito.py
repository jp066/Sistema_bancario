def depositar(self):
    valor_deposito = float(input("Digite o valor do depósito: "))
    if valor_deposito > 0:
        self.saldo += valor_deposito
        self.lista_extrato.append(f"Depósito: R$ {valor_deposito}")
        print("Depósito efetuado com sucesso", f"R$ {valor_deposito}")
    else:
        print("Valor inválido")