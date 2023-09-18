from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria

class Protudos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    
class Estoque:
    def __init__(self, protudo : Protudos, quantidade):
        self.protudo = protudo
        self.quantidade = quantidade

class Vendas:
    def __init__(self, itensVendido : Protudos, caixa, cleinte, quantidadeItens, data = datetime.now()):
        self.itensVendido = itensVendido
        self.caixa = caixa
        self.cleinte = cleinte
        self.quantidadeItens = quantidadeItens
        self.data = data
        
class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Vendedor(Pessoa):
    def __init__(self, clt, nome, cpf, telefone, email, endereco):
        self.clt = clt
        super(Vendedor, self).__init__(nome, cpf ,telefone, email, endereco)

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
        

        
        
        
        