import os 

def mostrar_dados(user):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Nome: ', user['nome'])
    print('Cpf: ', user['cpf'])
    
    print(
    f"Endereço: Rua {user['endereco']['rua']}, "
    f"Bairro {user['endereco']['bairro']}, "
    f"Cidade {user['endereco']['cidade']}, "
    f"Número {user['endereco']['numero']}"
    )
    
    print('E-mail: ', user['email'])
    print('Telefone: ', user['telefone'])
    input('\nPressione algo para voltar...')
      
        