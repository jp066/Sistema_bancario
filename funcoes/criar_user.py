def criar_user(): # Utilizando os parâmetros nome e cpf
    while True:
        usuarios = []

        nome_user = input("Digite o nome: ")
        cpf_user = input("Digite o CPF: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        endereco = {
            'logradouro': str(logradouro), # Convertendo para string
            'numero': str(numero) # Convertendo para string
        } # 
        print('-'*30)
        print("Usuário criado com sucesso!")
        print('-'*30)
        print(f"Nome fornecido: {nome_user}")  
        print(f"CPF fornecido: {cpf_user[:3]}.{cpf_user[3:6]}.{cpf_user[6:9]}-{cpf_user[9:]}")
        print(f"Endereço fornecido: {endereco['logradouro']}, {endereco['numero']}") # Utilizando os parâmetros de endereço
        print('-'*30)

        usuario = {
            'nome': nome_user,
            'cpf': cpf_user,
            'endereco': endereco
        }
        

        usuarios.append(usuario)
        print(usuarios)
        
        escolha = int(input("Deseja cadastrar outro usuário? [1] Sim [0] Não: "))
        
        if escolha == 0:
            break
        elif escolha == 1:
            criar_user()
        
        
        verificar_cpf = False
        
        for usuario in usuarios:
            cpf_lista = usuario['cpf']
            cpf = cpf_lista
        if cpf == cpf:
            print("CPF já cadastrado!")
            break
        else:
            criar_user()
            

        return nome_user, cpf_user, endereco



# teste
print("Cadastro de usuário")
criar_user()