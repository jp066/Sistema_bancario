from abc import ABC, abstractmethod

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
    def __init__(self, agencia, numero, saldo, cpf_usuario, cliente, historico):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo
        self.__cpf_usuario = cpf_usuario
        self.__cliente = cliente
        self.__historico = historico
        
        
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
    def cpf_usuario(self):
        return self.__cpf_usuario
        
        
    @property
    def cliente(self):
        return self.__cliente
        
        
    @property
    def historico(self):
        return self.__historico


    def mostrar_extrato(saldo,*, extrato):
        print("\nExtrato:")
        for item in extrato:
            print(item)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        return saldo


    def criar_conta(*, agencia, numero, cpf_usuario):
        conta = {
            'agencia': agencia,
            'numero': numero,
            'saldo': 0,
            'cpf_usuario': cpf_usuario
        }

        print('-'*30)
        print("Conta criada com sucesso")
        print(f'''Sua conta é:
            agencia: {agencia}
            numero: {numero}''')

        return conta


    def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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


    def depositar(saldo, valor, extrato, /):
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
    
    
cliente = Cliente('joao', '12345678901', '01/01/2000', 'rua x - 123 - bairro x - XX')
conta = Conta(AGENCIA, numero, saldo, cliente.cpf, cliente)


