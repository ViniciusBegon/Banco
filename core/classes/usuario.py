

class Usuario():
    def __init__ (self,id,nome,cpf,senha,endereco,email,telefone):
        self.id_user = id
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.endereco = endereco 
        self.email = email 
        self.telefone = telefone
        self.saldo = 0

    def to_dict(self):
        return {
            "id" : self.id_user,
            "nome": self.nome,
            "cpf": self.cpf,
            "senha": self.senha,
            "endereco": self.endereco.to_dict() if hasattr(self.endereco, "to_dict") else self.endereco,
            "email": self.email,
            "telefone": self.telefone,
            "saldo" : self.saldo
        }
 