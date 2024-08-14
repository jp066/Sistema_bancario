from .listar_contas import listar_contas


def sacar(self, saldo, valor, limite, numero_saques, limite_saques, **extrato): # a função deve receber os argumentos apenas por nome
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo insuficiente!")
        
        
        
