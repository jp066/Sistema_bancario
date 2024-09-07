from abc import ABC, abstractmethod
from random import randint
from datetime import datetime

Imprimir_menu = """
--------------------------------
[nu]\t Novo usuário
[nc]\t Nova conta
[ncc]\t Nova conta corrente
[d]\t Depositar
[s]\t Sacar
[e]\t Extrato
[q]\t Sair
--------------------------------
=> """

class Menu:
    def __init__(self):
        self.__opcao = None
        self.usuarios = []

    @property
    def opcao(self):
        return self.__opcao

    @opcao.setter
    def opcao(self, valor):
        self.__opcao = valor

    def exibir_menu(self):
        print(Imprimir_menu)
        self.opcao = input("Escolha uma opção: ").lower()

        while True:
            if self.opcao == "nu":
                novo_usuario = Pessoa_Fisica.novo_user()
                self.usuarios.append(novo_usuario)
            elif self.opcao == "nc":
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.buscar_cliente(cpf)
                if cliente:
                    Conta.criar_conta(cliente)
                else:
                    print("Cliente não encontrado.")
            elif self.opcao == "ncc":
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.buscar_cliente(cpf)
                if cliente:
                    ContaCorrente.criar_conta(cliente)
                else:
                    print("Cliente não encontrado.")
            elif self.opcao == "d":
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.buscar_cliente(cpf)
                if cliente:
                    valor = float(input("Digite o valor a ser depositado: "))
                    if cliente.contas: # Verifica se o cliente possui contas
                        conta = cliente.contas[0] # Pega a primeira conta do cliente
                        deposito = Deposito(valor)
                        cliente.realizar_transacao(conta, deposito)
                    else:
                        print("Cliente sem contas")
                else:
                    print("Cliente não encontrado.")
            elif self.opcao == "s":
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.buscar_cliente(cpf)
                if cliente:
                    valor = float(input("Digite o valor a ser sacado: "))
                    if cliente.contas:
                        conta = cliente.contas[0]
                        saque = Saque(valor)
                        cliente.realizar_transacao(conta, saque)
                    else:
                        print("Cliente sem contas")
                else:
                    print("Cliente não encontrado.")
            elif self.opcao == "e":
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.buscar_cliente(cpf)
                if cliente and cliente.contas:
                    conta = cliente.contas[0]
                    conta.mostrar_extrato()
                else:
                    print("Cliente ou conta não encontrada.")
            elif self.opcao == "q":
                break
            else:
                print("Opção inválida")
            print(Imprimir_menu)
            self.opcao = input("Escolha uma opção: ").lower()

    def buscar_cliente(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None


class Conta:
    def __init__(self, saldo_inicial, cliente):
        self.__agencia = self.gerar_agencia()
        self.__numero = self.gerar_numero_conta()
        self.__saldo = saldo_inicial
        self.__cliente = cliente
        self.__historico = Historico()

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

    def gerar_agencia(self):
        return randint(1000, 9000)

    def gerar_numero_conta(self):
        return randint(10000, 99999)

    def mostrar_extrato(self):
        print("\nExtrato:")
        for item in self.__historico.transacoes:
            print(item)
        print(f"\nSaldo atual: R$ {self.__saldo:.2f}")

    @classmethod
    def criar_conta(cls, cliente, saldo=0):
        saldo_inicial = saldo
        nova_conta = cls(saldo_inicial, cliente)
        cliente.contas.append(nova_conta)
        print("Conta criada com sucesso")
        return nova_conta

    def sacar(self, valor: float) -> bool:
        if isinstance(self, ContaCorrente) and self.limite_saques <= 0:
            print("Limite de saques atingido!")
            return False
        elif valor <= self.__saldo:
            saque = Saque(valor)
            saque.registrar(self)
            if isinstance(self, ContaCorrente):
                self._ContaCorrente__limite_saques -= 1
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def depositar(self, valor: float) -> bool:
        deposito = Deposito(valor) # Cria um objeto do tipo Deposito
        deposito.registrar(self) # Registra o depósito na conta
        return True


class ContaCorrente(Conta):
    def __init__(self, saldo, cliente):
        super().__init__(saldo, cliente)
        self.__limite = 500.00
        self.__limite_saques = 3

    @property
    def limite(self):
        return self.__limite

    @property
    def limite_saques(self):
        return self.__limite_saques


class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

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
        conta.saldo += self.valor
        conta.historico.transacoes.append(f"Depósito: R$ {self.valor}")
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
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.transacoes.append(f"Saque: R$ {self.valor}")
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"Saque: R$ {self.valor}"


class Cliente:
    def __init__(self, contas, endereco=None):
        self.endereco = endereco
        self.contas = contas
        self.acao_realizada = False

    def adicionar_conta(self):
        conta = Conta.criar_conta(self)
        self.contas.append(conta)
        print("Conta adicionada com sucesso")
        return conta

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        if transacao in conta.historico.transacoes:
            self.acao_realizada = True
        print("Transação realizada com sucesso")


class Pessoa_Fisica(Cliente):
    @classmethod
    def novo_user(cls):
        contas = []  # Supondo que contas seja uma lista
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")

        # Validação do formato da data
        while True:
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato dd/mm/yyyy.")
                data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")

        novo_usuario = cls(contas, cpf, nome, data_nascimento)
        return novo_usuario

    def __init__(self, contas, cpf, nome, data_nascimento):
        super().__init__(contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

menu = Menu()
menu.exibir_menu()