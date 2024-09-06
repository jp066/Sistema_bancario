from abc import ABC, abstractmethod
from random import randint

menu = """
--------------------------------
[nu]\t Novo usuário
[nc]\t Nova conta
[lc]\t Listar contas
[d]\t Depositar
[s]\t Sacar
[e]\t Extrato
[q]\t Sair
--------------------------------
=> """

class Conta:
    def __init__(self, saldo, cliente):
        self.__agencia = self.gerar_agencia()
        self.__numero = self.gerar_numero_conta()
        self.__saldo = saldo
        self.__cliente = cliente  # recebe um objeto da classe Cliente
        self.__historico = Historico() # recebe um objeto da classe Historico


    def gerar_agencia(self):
        agencia = randint(1000, 2000)
        return agencia  # randint(1000, 2000)

    def gerar_numero_conta(self):
        return randint(10000, 99999)

    def inverter_agencia(self):
        agencia = self.gerar_agencia()
        return str(agencia)[::-1]


# definindo os métodos de acesso aos atributos privados
    @property
    def agencia(self):
        return self.__agencia
        
        
    @property
    def numero(self):
        return self.__numero
        
        
    @property
    def saldo(self):
        return self.__saldo
    
    
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Valor inválido")
        
        
    @property
    def cliente(self):
        return self.__cliente
        
        
    @property
    def historico(self):
        return self.__historico


# definindo os métodos de alteração dos atributos privados
    def mostrar_extrato(self):
        print("\nExtrato:")
        for item in self.__historico.transacoes:
            print(item)
        print(f"\nSaldo atual: R$ {self.__saldo:.2f}")



    @classmethod
    def criar_conta(cls, cliente):
        numero = randint(1, 1000) # gera um número aleatório para a conta
        conta = cls(saldo=0.0, cliente=cliente) # cria um objeto da classe Conta
        return conta
    
    # esse método é um método de classe, pois ele não precisa de uma instância da classe para ser chamado
    # a função dele é criar uma nova conta, então ele recebe como parâmetro um objeto da classe Cliente e um número aleatório


    def sacar(self, valor: float) -> bool:
        if valor <= self.__saldo:
            saque = Saque(valor)
            saque.registrar(self)
            return True
        else:
            print("Saldo insuficiente!")
            return False

    # Método de depositar
    def depositar(self, valor: float) -> bool:
        deposito = Deposito(valor)
        deposito.registrar(self)
        return True


class ContaCorrente(Conta):
    def __init__(self, saldo, cliente, limite, limite_saques):
        super().__init__(saldo, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saques



class Historico:
    def __init__(self):
        self.__transacoes = [] # cria uma lista vazia para armazenar as transações
        
    @property
    def transacoes(self):
        return self.__transacoes
    
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao) # adiciona a transação à lista de transações
        
        
    def imprimir(self):
        print("\nHistórico:")
        for transacao in self.transacoes:
            print(transacao)


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = float(valor)
        
    @property
    def valor(self):
        return self.__valor
    
    
    def registrar(self, conta):
        conta.saldo += self.valor # incrementa o saldo da conta com o valor do depósito
        conta.historico.transacoes.append(f"Depósito: R$ {self.valor}") # adiciona a transação ao histórico da conta
        print("Depósito efetuado com sucesso")
        
        
    def __str__(self):
        return f"Depósito: R$ {self.valor}"


class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = float(valor)
        
        
    @property
    def valor(self):
        return self.__valor

    
    def registrar(self, conta):
        if conta.saldo >= self.valor: # verifica se o saldo da conta é maior ou igual ao valor do saque
            conta.saldo -= self.valor # decrementa o saldo da conta com o valor do saque
            conta.historico.transacoes.append(f"Saque: R$ {self.valor}")
        else:
            print("Saldo insuficiente")
            
            
    def __str__(self):
        return f"Saque: R$ {self.valor}"



class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


# Criando uma conta
minha_conta = Conta(100.0, cliente=Cliente(nome="Fulano", cpf="123.456.789-00", data_nascimento="01/01/2000", endereco="Rua A, 123"))

# Realizando um depósito
deposito = Deposito(50.0)
deposito.registrar(minha_conta)
minha_conta.mostrar_extrato(saldo=minha_conta.saldo, extrato=minha_conta.historico.transacoes)

# Realizando um saque
saque = Saque(30.0)
saque.registrar(minha_conta)
minha_conta.mostrar_extrato(saldo=minha_conta.saldo, extrato=minha_conta.historico.transacoes)

# Exibindo o histórico de transações
minha_conta.historico.imprimir()
