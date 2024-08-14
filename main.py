from funcoes.deposito import depositar
from funcoes.saque import sacar
from funcoes.extrato import extrato
from funcoes.criar_conta_corrente import criar_conta
from funcoes.criar_user import criar_usuario
from funcoes.listar_contas import listar_contas


class Banco_python:
    menu = """
    --------------------------------
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t Novo usuário
    [q]\t Sair
    --------------------------------
    => """
    
    
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.lista_extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.AGENCIA = '0001'
        self
    
    
    def interface_menu(self):
        while True:
            opcao = input(Banco_python.menu)
            if opcao == 'd':
                depositar(self)
            elif opcao == 's':
                sacar(self, saldo=1000, valor=100, limite=500, numero_saques=0, limite_saques=3)
            elif opcao == 'e':
                extrato(self)
            elif opcao == 'q':
                break
            elif opcao == 'nc':
                criar_conta(self)
            elif opcao == 'lc':
                listar_contas(self)
            elif opcao == 'nu':
                criar_usuario(self)
            else:
                print("Opção inválida")
            
        
    
    
# teste
print("Bem-vindo ao Banco do Python")
Banco_python = Banco_python() # Instanciando a classe
Banco_python.interface_menu()