
import json
import os
from validate_docbr import CPF
from core.funcoes.verificadores import gerar_hash_senha
from app.menu_user_auth import menu_user_autenticado



caminho_db = 'data/users.json'  
validar_cpf = CPF()

def autenticar_user():
    print('-' * 16)
    print('Digite seus dados abaixo:')
    print('-' * 16)

    while True:
        # Entrada e validação cpf
        while True:
            entry_cpf = input('CPF: ').strip()
            if validar_cpf.validate(entry_cpf):
                break
            else:
                print('CPF inválido, tente novamente.')

        entry_senha = input('Digite sua Senha: ')
        senha_hash = gerar_hash_senha(entry_senha)
        cpf = entry_cpf

        try:
            with open(caminho_db, 'r') as f:
                user_list = json.load(f)

            user_auth = False
            for user in user_list:
                if user["cpf"] == cpf and user["senha"] == senha_hash:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Bem-vindo, {user['nome']}!")
                    user_auth = True
                    break

            if user_auth:
                menu_user_autenticado(user)
                return  
            else:
                print('Usuário ou senha inválidos, tente novamente.')

        except FileNotFoundError:
            print('Base de dados não encontrada.')

        except Exception as e:
            print(f'Erro inesperado: {e}')

        print()
        sim_nao = input('Deseja tentar novamente? 1 - Sim | 2 - Não: ')
        if sim_nao.strip() == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif sim_nao.strip() != '1':
            print('Opção inválida, retornando ao início.')
