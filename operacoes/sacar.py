import os
import json
caminho_db = 'data/users.json'  

def sacar(user):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    id_user = user["id"]
    while True:
        try:
            valor_deposito = int(input('Qual valor deseja sacar?\n'))
            break
        except ValueError:
            print('Formato errado, digite apenas numeros.')
            
    
    
    try:
        with open(caminho_db, 'r') as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = []

    for u in usuarios:
        if u["id"] == id_user:
            u["saldo"]-= valor_deposito

    with open(caminho_db, 'w') as f:
        json.dump(usuarios, f, indent=4)
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Saque de R$ {valor_deposito:.2f} realizado com sucesso!")
    input('Pressione algo para continuar...')