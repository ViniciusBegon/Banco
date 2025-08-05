import os
import json
from app.dados_usuario import mostrar_dados
from operacoes import transferir,sacar,depositar

caminho_db = 'data/users.json'

def menu_user_autenticado(user):
    

    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
    
        with open(caminho_db, 'r') as f:
                    user_list = json.load(f)
        
        for u in user_list:
            if u["id"] == user["id"]:
                usuario_auth = u
                
        print('Bem vindo a sua conta!')
        print('SALDO ATUAL')
        print(f'R$ {usuario_auth['saldo']}')
        print('1 - Depositar')
        print('2 - Transferir')
        print('3 - Sacar')
        print('\nConfigurações:')
        print('4 - Meus dados')
        print('5 - Trocar senha')
        print('6 - Sair da conta')
        
        select_option_auth = input('\n: ')
        
        if select_option_auth == '1':
            depositar(usuario_auth)
        elif select_option_auth == '2':
            transferir(usuario_auth)
        elif select_option_auth == '3':
            sacar(usuario_auth)
        elif select_option_auth == '4':
            mostrar_dados(usuario_auth)
        elif select_option_auth == '5':
            ...
        elif select_option_auth == '6':
            print('Você está saindo!')
            break
        else:
            print('Opção invalida, tente novamente')
            continue
        