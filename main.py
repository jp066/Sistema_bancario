class Banco_python:
    menu = """
    --------------------------------
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    --------------------------------
    => """
    
    
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.lista_extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
    
    
    def interface_menu(self):
        while True:
            opcao = input(Banco_python.menu)
            if opcao == 'd':
                self.depositar()
            elif opcao == 's':
                self.sacar()
            elif opcao == 'e':
                self.extrato()
            elif opcao == 'q':
                break
            else:
                print("Opção inválida")
        
        
    def depositar(self):
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            self.saldo += valor_deposito
            self.lista_extrato.append(f"Depósito: R$ {valor_deposito}")
            print("Depósito efetuado com sucesso")
        else:
            print("Valor inválido")
            
            
    def extrato(self):
        print("Extrato")
        print("Saldo: R$", self.saldo)
        print("Limite de valor por saque: R$", self.limite)
        print("Número de saques realizados: ", self.numero_saques)
        for item in self.lista_extrato:
            print(item) #
            
            
    def sacar(self):
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= self.saldo:
            if self.numero_saques < self.LIMITE_SAQUES: # Verifica se o número de saques é menor ou igual ao limite
                if valor_saque <= self.limite:
                    self.saldo -= valor_saque
                    self.lista_extrato.append(f"Saque: R$ {valor_saque}")
                    self.numero_saques += 1
                    print("Saque efetuado com sucesso")
                else:
                    print("Valor de saque acima do limite")
            else:
                print("Limite de saques atingido")
        else:
            print("Saldo insuficiente")
        
    
    
# teste
print("Bem-vindo ao Banco do Python")
Banco_python = Banco_python() # Instanciando a classe
Banco_python.interface_menu()


print(Banco_python.extrato())