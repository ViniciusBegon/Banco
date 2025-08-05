import hashlib
import getpass  
import uuid
import re
from validate_docbr import CPF
cpf_validar = CPF()

#criptografar senha
def gerar_hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

#criar email
def criar_email():
    while True:
        email = input('Digite seu email: ')
        if '@' and '.' in email:
            return email
        else:
            print('Formato de email errado, tente novamente. ')
            
#criar senha
def criar_senha():
    while True:
        senha = getpass.getpass('Digite uma senha:')
        if len(senha) < 8:
            print('Senha muito curta, tente novamente')
            continue
        confirm_senha = input('Confirme sua senha:')
        if senha != confirm_senha:
            print('Senhas não coincidem, tente novamente.')
            continue
        else:
            break
    print('Senha cadastrada com sucesso!')
    return gerar_hash_senha(senha)

#criar cpf
def criar_cpf():
    while True:
        try:
            cpf_entrada = input('Digite seu CPF:\n').strip()
            cpf_limpo  = re.sub(r'\D', '', cpf_entrada)
            if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
                raise ValueError('CPF deve conter apenas 11 dígitos numéricos.')

            if cpf_validar.validate(cpf_limpo):
                return cpf_limpo
            else:
                print('CPF inválido, tente novamente.')

        except ValueError as e:
            print(f'Erro: {e}')

        except Exception as e:
            print(f'Erro inesperado ao validar CPF: {e}')
            
#criar um id para usuario
def gerar_id_user():
    return str(uuid.uuid4())
