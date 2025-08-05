#import python 
import json
import os
from validate_docbr import CPF

#import interno
from core.funcoes.verificadores import criar_cpf, criar_email, criar_senha, gerar_id_user
from core.classes import Usuario


caminho_db = 'data/users.json'  

#funções


def create_user():
    nome = input('Digite seu nome:\n')
    cpf = criar_cpf()
    telefone = input('Digite seu telefone: ')
    print('Seu endereço:')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')
    numero_rua = input('Número: ')
    endereco = {
        'cidade': cidade,
        'bairro': bairro,
        'rua': rua,
        'numero': numero_rua
    
    }
    email = criar_email()
    senha = criar_senha()
    id_usuario = gerar_id_user()
    
   
    #Criando objeto usuário
    creating_user = Usuario(id_usuario, nome, cpf, senha, endereco, email, telefone)
    new_user = creating_user.to_dict()
    
    #verifica se existe a passta, caso contrairo cria
    os.makedirs('data', exist_ok=True)

    try:
        with open(caminho_db, 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    dados.append(new_user)

    with open(caminho_db, 'w') as f:
        json.dump(dados, f, indent=4)
        
    print('\nUsuario criado com sucesso!')
    input('Pressione algo para continuar...')    
    
    os.system('cls' if os.name == 'nt' else 'clear')


