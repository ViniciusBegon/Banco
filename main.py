import os
from core.funcoes.autenticar_user import autenticar_user
from core.funcoes import create_user

def App():

    def menu_nao_autenticado():

        while True:
            print('_' * 26)
            print('Bem vindo ao Banco Green')
            print('_' * 26)
            print('\nSelecione a opção correspondente:')
            print('\n1 - Entrar na sua conta')
            print('2 - Cadastrar-se no banco')
            print('3 - Sair')
            select_option = input('\n: ')
            if select_option == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                autenticar_user() 
            elif select_option == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                create_user()  # chama a função
            elif select_option == '3':
                print('Você está saindo!')
                break
            else:
                print('Opção invalida, tente novamente')
                continue

    
    menu_nao_autenticado()
       

if __name__ == '__main__':
    App()