def extrato(self):
    print("Extrato")
    print("Saldo: R$", self.saldo)
    print("Limite de valor por saque: R$", self.limite)
    print("Número de saques realizados: ", self.numero_saques)
    for item in self.lista_extrato:
        print(item) #