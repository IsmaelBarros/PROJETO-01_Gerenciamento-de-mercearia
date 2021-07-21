from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produto:
    def __init__(self, nome, preco, categoria: Categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(self, item_vendido: Produto, vendedor, comprador, quantidade_vendida, data=datetime.now().strftime("%d/%m/%Y")):
        self.item_vendido = item_vendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        self.data = data


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria: Categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Endereco:
    def __init__(self, logradouro, numero, bairro, cep, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado


class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco: Endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco


class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco: Endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
