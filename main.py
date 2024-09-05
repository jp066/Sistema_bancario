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
    def __init__(self, agencia, saldo, cliente, historico):
        self.__agencia = agencia
        self.__numero = 0
        self.__saldo = saldo
        self.__cliente = cliente  # recebe um objeto da classe Cliente
        self.__historico = historico  # instancia da classe Historico, serve para armazenar as transações da conta na classe Conta

    def gerar_agencia(self):
        agencia = randint(1000, 2000)
        return agencia  # randint(1000, 2000)

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
        
        
    @property
    def cliente(self):
        return self.__cliente
        
        
    @property
    def historico(self):
        return self.__historico


# definindo os métodos de alteração dos atributos privados
    def mostrar_extrato(self, saldo, *, extrato): # tem como parâmetro obrigatório o saldo e o extrato é opcional
        print("\nExtrato:")
        for item in extrato: # percorre a lista de transações
            print(item) 
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        return float(saldo) # retorna o saldo como float


    @staticmethod
    def criar_conta(cliente, saldo, historico):
        agencia = Conta.agencia # chama o método de classe agencia
        numero = randint(1, 1000)
        conta = Conta(agencia, saldo, cliente, historico)
        print('-'*30)
        print("Conta criada com sucesso")
        print(f'''Sua conta é:
            agencia: {agencia}
            numero: {numero}''')
        return conta
    # nesse método, o saldo é passado como argumento, pois é o saldo inicial da conta


    def sacar(self, *, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
        if valor <= saldo:
            if numero_saques < LIMITE_SAQUES:
                if valor <= limite:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor}")
                    numero_saques += 1
                    print(f'o numero de saques é {numero_saques}')
                    print("Saque efetuado com sucesso")
                else:
                    print("Valor de saque acima do limite")
            else:
                print("Limite de saques atingido")
        else:
            print("Saldo insuficiente")
            
        return saldo, extrato, numero_saques


    def depositar(self, saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            print(f"Saldo atualizado: R$ {saldo}")
            extrato.append(f"Depósito: R$ {valor}")
            print("Depósito efetuado com sucesso")
        else:
            print("Valor inválido")

        return saldo


class ContaCorrente(ABC):
    def __init__(self, limite, limite_saques):
        self.limite = limite
        self.limite_saques = limite_saques


class Historico:
    def __init__(self):
       self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


#agencia = '1234'
#saldo = 1000.0
#cliente = Cliente('nome', 'cpf', 'data_nascimento', 'endereco')
#historico = Historico()
## Criando a instância da classe Conta com os argumentos necessários
#conta = Conta(agencia, saldo, cliente, historico)
#print(conta.inverter_agencia())