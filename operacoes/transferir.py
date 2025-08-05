import os
import json
import re
caminho_db = 'data/users.json' 
from validate_docbr import CPF 
from core.funcoes.verificadores import gerar_hash_senha

def transferir(user):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    cpf_validar = CPF()
    
    try:
        with open(caminho_db, 'r') as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = []

    
    id_user = user["id"]
    
    while True:
        
        destino = input('Digite o CPF para qual ira transferir o valor:')
        cpf_limpo  = re.sub(r'\D', '', destino)
        if not cpf_validar(cpf_limpo):
            print('CPF inválido tente novamente!')
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        try:
            for i in usuarios:
                if i["cpf"] == cpf_limpo:
                    return
        except:
            print('Usuário não encontrado, tente novamente ou digite "s" para sair')
            continue
        break
        
        
    while True:
        try:
            valor_deposito = int(input('Qual valor deseja depositar?\n'))
            break
        except ValueError:
            print('Formato errado, digite apenas numeros.')
    
    while True:
        
        try:    
            confirmar_senha = input('Digite sua senha para confirmar a transferência:')
            senha = gerar_hash_senha(confirmar_senha)
            if senha != user['senha']:
                print('Senha incorreta, tente novamente...')
                continue
            break
        except:
            print('Realizando transferencia...')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    for u in usuarios:
        if u["id"] == id_user:
            u["saldo"]-= valor_deposito
    
    for i in usuarios:
        nome_destino = i['nome']
        if i["cpf"] == cpf_limpo:
            i["saldo"] += valor_deposito

    with open(caminho_db, 'w') as f:
        json.dump(usuarios, f, indent=4)
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Transferencia de R$ {valor_deposito:.2f} feita com sucesso para {nome_destino}!")
    input('Pressione algo para continuar...')