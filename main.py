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


saldo = 0
numero = 1
limite = 500
lista_extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas_correntes = []


def interface_menu():
    global saldo, numero_saques, lista_extrato, usuarios, numero
    
    while True:
        opcao = input(menu)
        if opcao == 'nu':
            nome = input("Digite o nome do titular: ")
            cpf = input("Digite o CPF: ")
            data_de_nascimento = input("em que ano voce nasceu? ")
            endereco = input("Digite o endereço (rua x - 123 - bairro x - XX): ")
            if not verificar_usuario(cpf=cpf): # se o usuario não existir
                criar_usuario(nome, cpf, data_de_nascimento, endereco)
            else:
                print('*'*30)
                print("Usuário já cadastrado.")
                print('*'*30)
                
        elif opcao == 'nc':
            cpf_usuario = input("Digite o CPF do usuário: ")
            conta = criar_conta(agencia=AGENCIA, numero=numero, cpf_usuario=cpf_usuario)
            conta = vincular_usuario_conta(cpf_usuario, conta)
            if conta:
                contas_correntes.append(conta)
                numero += 1
            
        elif opcao == 'd':
            if usuarios:
                print(f'ola {usuarios[0]["nome"]}')
            valor = float(input("digite o valor do deposito: "))
            saldo = depositar(saldo, valor, lista_extrato)
            
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=lista_extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            
        elif opcao == 'e':
            saldo = mostrar_extrato(saldo, extrato=lista_extrato)
            
        elif opcao == 'q':
            break
        
        elif opcao == 'lc':
            print("Contas correntes:")
            for conta in contas_correntes:
                print(f"Agência: {conta['agencia']} - Conta: {conta['numero']} - Titular {conta['cpf_usuario']}")
                
        else:
            print("Opção inválida")
            
            
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"Saldo atualizado: R$ {saldo}")
        extrato.append(f"Depósito: R$ {valor}")
        print("Depósito efetuado com sucesso")
    else:
        print("Valor inválido")
        
    return saldo


def mostrar_extrato(saldo,*, extrato):
    print("\nExtrato:")
    for item in extrato:
        print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    return saldo
        
        
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


def vincular_usuario_conta(cpf_usuario, conta):
    for usuario in usuarios:  # percorre a lista de usuarios
        if usuario['cpf'] == cpf_usuario:  # verifica se o CPF do usuário na lista é igual ao CPF fornecido
            conta['usuario'] = usuario  # adiciona o usuario a conta
            print(f'Conta vinculada ao usuário {usuario["nome"]}')
            return conta
    print("Usuário não encontrado.")
    return None


def criar_usuario(nome, cpf, data_de_nascimento, endereco):
    usuario = {
        'nome': nome,
        'cpf': cpf,
        'data_de_nascimento': data_de_nascimento,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print('-'*30)
    print("Usuário criado com sucesso")
    print(f'bem vindo {nome}!')
    
    
def verificar_usuario(*, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

# teste
print("Bem-vindo ao Banco do Python")
interface_menu()