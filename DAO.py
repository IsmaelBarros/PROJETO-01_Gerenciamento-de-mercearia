from Models import *
import os


class DaoCategoria:

    db_file = 'categorias.txt'

    @classmethod
    def salvar(cls, categoria: Categoria):
        with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
            arq.writelines(categoria.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        if os.path.isfile(cls.db_file):
            with open(cls.db_file, 'r') as arq:
                cls.categorias = arq.readlines()

            if cls.categorias:
                cls.categorias = list(
                    map(lambda x: x.replace('\n', ''), cls.categorias))

                cat = []
                for i in cls.categorias:
                    cat.append(Categoria(i))

                return cat
        else:
            with open(cls.db_file, 'w') as arq:
                pass


class DaoVenda:

    db_file = 'venda.txt'

    @classmethod
    def salvar(cls, venda: Venda):
        with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
            arq.writelines(venda.item_vendido.nome + "|" + str(venda.item_vendido.preco) + "|" +
                           venda.item_vendido.categoria.categoria + "|" + venda.vendedor + "|" +
                           venda.comprador + "|" + str(venda.quantidade_vendida) + "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(cls.db_file, 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(
                Venda(Produto(i[0], i[1], Categoria(i[2])), i[3], i[4], i[5], i[6]))
        return vend


class DaoEstoque:

    db_file = 'estoque.txt'

    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
            arq.writelines(produto.nome + "|" + str(produto.preco) +
                           "|" + produto.categoria.categoria + "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        if os.path.isfile(cls.db_file):
            with open(cls.db_file, 'r') as arq:
                cls.estoque = arq.readlines()

            cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
            cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

            est = []
            for i in cls.estoque:
                est.append(
                    Estoque(Produto(i[0], i[1], Categoria(i[2])), int(i[3])))
            return est
        else:
            with open(cls.db_file, 'w') as arq:
                pass


class DaoFornecedor:

    db_file = 'fornecedor.txt'

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        if os.path.exists(cls.db_file):
            with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
                arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' +
                               fornecedor.telefone + '|' + fornecedor.categoria.categoria)
                arq.writelines('\n')
        else:
            print('Crie o arquivo fornecedor.txt')

    @classmethod
    def ler(cls):
        if os.path.isfile(cls.db_file):
            with open(cls.db_file, 'r') as arq:
                cls.fornec = arq.readlines()

            cls.fornec = list(map(lambda x: x.replace('\n', ''), cls.fornec))
            cls.fornec = list(map(lambda x: x.split('|'), cls.fornec))

            fornec = []
            for item in cls.fornec:
                fornec.append(Fornecedor(
                    item[0], item[1], item[2], Categoria(item[3])))
            return fornec
        else:
            with open(cls.db_file, 'w') as arq:
                pass


class DaoPessoa():

    db_file = 'clientes.txt'

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
            cls.pessoa = arq.writelines(pessoa.nome + '|' + pessoa.telefone + '|' + pessoa.cpf + '|' + pessoa.email + '|' +
                                        pessoa.endereco.logradouro + '|' + pessoa.endereco.numero + '|' + pessoa.endereco.bairro +
                                        '|' + pessoa.endereco.cep +
                                        '|' + pessoa.endereco.cidade + '|' + pessoa.endereco.estado)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(cls.db_file, 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        cl = []
        for cliente in cls.clientes:
            cl.append(Pessoa(cliente[0], cliente[1],
                             cliente[2], cliente[3],
                             Endereco(cliente[4], cliente[5], cliente[6], cliente[7], cliente[8], cliente[9])))
        return cl


class DaoFuncionario:

    db_file = 'funcionarios.txt'

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open(cls.db_file, 'a', encoding='UTF-8', errors='replace') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' +
                           funcionario.cpf + '|' + funcionario.email + '|' + funcionario.endereco.logradouro +
                           '|' + funcionario.endereco.numero + '|' + funcionario.endereco.bairro + '|' + funcionario.endereco.cep +
                           '|' + funcionario.endereco.cidade + '|' + funcionario.endereco.estado)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(cls.db_file, 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(
            map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        func = []
        for funcionario in cls.funcionarios:
            func.append(Funcionario(funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4],
                                    Endereco(funcionario[5], funcionario[6], funcionario[7], funcionario[8], funcionario[9], funcionario[10])))
        return func
