from Models import Categoria, Produto, Estoque, Venda, Fornecedor, Endereco, Pessoa, Funcionario
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

import os
import sys


class ControllerCategoria:

    def cadastrar_categoria(self, nova_categoria):
        try:
            categorias = DaoCategoria.ler()
            existe = False

            if categorias is None:
                DaoCategoria.salvar(Categoria(nova_categoria))
                sys.exit('Primeira categoria cadastrada com sucesso.')

            for cat in categorias:
                if nova_categoria == cat.categoria:
                    existe = True

            if not existe:
                DaoCategoria.salvar(Categoria(nova_categoria))
                print('categoria cadastrada com sucesso.')
            else:
                print('A categoria que deseja cadastrar já existe.')
        except Exception as err:
            print(err)

    def remover_categoria(self, categoria_remover):
        try:
            categorias = DaoCategoria.ler()

            cat_lista = list(
                filter(lambda categorias: categorias.categoria == categoria_remover, categorias))

            if len(cat_lista) <= 0:
                print('Esta categoria não existe para ser removida.')
            else:
                for i in range(len(categorias)):
                    if categorias[i].categoria == cat_lista[0].categoria:
                        del categorias[i]
                        print(f'Categoria {cat_lista[0].categoria} excluida')
                        break

                with open('categorias.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                    for cat in categorias:
                        arq.writelines(cat.categoria)
                        arq.writelines('\n')
        except Exception as err:
            print(err)

    def alterar_categoria(self, categoria_alterar, categoria_alterada):
        try:
            categorias = DaoCategoria.ler()

            cat = list(filter(lambda categorias: categorias.categoria ==
                              categoria_alterar, categorias))

            if cat:
                cat_existentes = list(filter(
                    lambda categorias: categorias.categoria == categoria_alterada, categorias))

                if not cat_existentes:
                    categorias = list(map(lambda categorias: Categoria(categoria_alterada) if(
                        categorias.categoria == categoria_alterar) else(categorias), categorias))
                else:
                    print('A categoria que deseja alterar já existe.')
            else:
                print('A categoria que deseja alterar não existe')

            with open('categorias.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                for i in categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        except Exception as err:
            print(err)

    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        if not categorias:
            print('Categoria vazia')
        else:
            for cat in categorias:
                print(f'Categoria: {cat.categoria}')


class ControllerEstoque:

    def cadastrar_produto(self, nome_prod, preco_prod, categoria_prod, quantidade):
        estoque = DaoEstoque.ler()
        categoria = DaoCategoria.ler()

        cat = list(filter(lambda estoque: estoque.categoria ==
                          categoria_prod, categoria))

        if cat:
            if not estoque:
                DaoEstoque.salvar(
                    Produto(nome_prod, preco_prod, Categoria(categoria_prod)), quantidade)
                sys.exit('Primeiro produto cadastrado com sucesso')

            prod_em_estoque = list(
                filter(lambda estoque: estoque.produto.nome == nome_prod, estoque))

            if not prod_em_estoque:
                DaoEstoque.salvar(
                    Produto(nome_prod, preco_prod, Categoria(categoria_prod)), quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')

    def remover_produto(self, nome):
        estoque = DaoEstoque.ler()
        prod = list(
            filter(lambda estoque: estoque.produto.nome == nome, estoque))
        if prod:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == nome:
                    del estoque[i]
                    break
            print('O produto foi removido com sucesso.')
        else:
            print('O produto que deseja remover não existe')

        with open('estoque.txt', 'w', encoding='UTF-8', errors='replace') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                               i.produto.categoria.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterar_produto(self, nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        estoque = DaoEstoque.ler()

        cat = list(filter(
            lambda estoque: estoque.produto.categoria.categoria == nova_categoria, estoque))

        if cat:
            prod_em_estoque = list(
                filter(lambda estoque: estoque.produto.nome == nome_alterar, estoque))
            if prod_em_estoque:
                prod_existente = list(
                    filter(lambda estoque: estoque.produto.nome == novo_nome, estoque))
                if not prod_existente:
                    estoque = list(
                        map(
                            lambda estoque: Estoque(
                                Produto(novo_nome, novo_preco, Categoria(
                                    nova_categoria)), nova_quantidade)
                            if(estoque.produto.nome == nome_alterar) else(estoque), estoque))

                    with open('estoque.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                        for est in estoque:
                            arq.writelines(est.produto.nome + '|' + str(est.produto.preco) +
                                           '|' + est.produto.categoria.categoria + '|' + str(est.quantidade))
                            arq.writelines('\n')
                        print('O produto foi alterado com sucesso.')
                else:
                    print('Produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe.')
        else:
            print('A categoria informada não existe')

    def mostrar_estoque(self):
        estoque = DaoEstoque.ler()

        if not estoque:
            print('Estoque vazio')
        else:
            print('==========Produtos==========')
            for i in estoque:
                print(
                    f'Nome: {i.produto.nome}\n'
                    f'Preco: {i.produto.preco}\n'
                    f'Categoria: {i.produto.categoria.categoria}\n'
                    f'Quantidade: {i.quantidade}'
                )
                print('--------------------')


class ControllerVenda:

    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidadeVendida):

        estoque = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in estoque:
            if existe == False:
                if i.produto.nome == nome_produto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - \
                            int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, Categoria(
                            i.produto.categoria.categoria)), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * \
                            float(i.produto.preco)

                        DaoVenda.salvar(vendido)
            temp.append(Estoque(Produto(i.produto.nome, i.produto.preco, Categoria(
                i.produto.categoria.categoria)), i.quantidade))

        arq = open('estoque.txt', 'w', encoding='UTF-8', errors='replace')
        arq.writelines('')

        for i in temp:
            with open('estoque.txt', 'a', encoding='UTF-8', errors='replace') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco +
                               "|" + i.produto.categoria.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

        if not existe:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra

    def relatorio_vendas(self):
        vendas = DaoVenda.ler()
        produtos = []

        for i in vendas:
            nome = i.itemVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if tamanho:
                produtos = list(map(lambda x: {'produto': nome,
                                               'quantidade': int(x['quantidade']) + int(quantidade)}
                                    if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome,
                                 'quantidade': quantidade})

        ordenado = sorted(
            produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Este são os produto mais vendidos')

        a = 1
        for i in ordenado:
            print(f"==========Produto [{a}]==========")
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrar_vendas(self, data_ini, data_fin):
        vendas = DaoVenda.ler()

        data_inicio = datetime.strptime(data_ini, '%d/%m/%Y')
        data_termino = datetime.strptime(data_fin, '%d/%m/%Y')

        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= data_inicio
                                          and datetime.strptime(x.data, '%d/%m/%Y') <= data_termino, vendas))

        count = 1
        total = 0
        for i in vendas_selecionadas:
            print(f"==========Produto [{count}]==========")
            print(f"Nome: {i.itemVendido.nome}\n"
                  f"Preço: R${i.itemVendido.preco}\n"
                  f"Categoria: {i.itemVendido.categoria.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade Vendida: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += float(i.itemVendido.preco) * int(i.quantidadeVendida)
            count += 1

        print(f"Total vendido : R${total:.2f}")


class ControllerFornecedor:

    def cadastrar_fornecedor(self, nome_fornec, cnpj, telefone, categoria):
        fornecedores = DaoFornecedor.ler()
        categorias = DaoCategoria.ler()

        cat_existente = list(filter(lambda x: x.categoria ==
                                    categoria, categorias))

        if cat_existente:
            if not fornecedores:
                DaoFornecedor.salvar(Fornecedor(
                    nome_fornec, cnpj, telefone, Categoria(categoria)))
                sys.exit('Primeiro fornecedor foi cadastrado com sucesso.')

        fornec_existente = list(filter(lambda x: x.nome ==
                                       nome_fornec, fornecedores))

        cnpj_existente = list(filter(lambda x: x.cnpj ==
                                     cnpj, fornecedores))

        telefone_existente = list(filter(lambda x: x.telefone ==
                                         telefone, fornecedores))

        if not fornec_existente:
            if not cnpj_existente:
                if not telefone_existente:
                    if cat_existente:
                        DaoFornecedor.salvar(Fornecedor(
                            nome_fornec, cnpj, telefone, Categoria(categoria)))
                        print('O fornecedor foi cadastrado com sucesso.')
                    else:
                        print(
                            'A categoria informada não existe, é necessário cadastrá-la antes')
                else:
                    print('Telefone já existente')
            else:
                print('cnpj já existente')
        else:
            print(
                'O fornecedor que desejar cadastrar já se encontra no nosso banco de dados')

    def alterar_fornecedor(self, nome_alterar, nome_novo, cnpj, telefone, categoria):
        fornecedores = DaoFornecedor.ler()
        categorias = DaoCategoria.ler()

        cat = list(
            filter(lambda x: x.categoria == categoria, categorias))

        if cat:
            fornec_cadastrado = list(
                filter(lambda x: x.nome == nome_alterar, fornecedores))
            if fornec_cadastrado:
                fornec_existente = list(
                    filter(lambda x: x.nome == nome_novo, fornecedores))
                if not fornec_existente:
                    fornecedores = list(
                        map(
                            lambda x: Fornecedor(nome_novo, cnpj, telefone, Categoria(
                                categoria)) if(x.nome == nome_alterar) else(x), fornecedores))

                    with open('fornecedor.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                        for fornecedor in fornecedores:
                            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj +
                                           '|' + fornecedor.telefone + '|' + fornecedor.categoria.categoria)
                            arq.writelines('\n')
                        print('O fornecedor foi alterado com sucesso.')
                else:
                    print('Fornecedor já cadastrado')
            else:
                print('O fornecedor que deseja alterar não existe.')
        else:
            print('A categoria informada não existe')


class ControllerCliente:
    pass


class ControllerFuncionario:
    pass


a = ControllerFornecedor()
a.alterar_fornecedor('OrangeCo Ltda', 'FruitsCo Ltda',
                     '10774927000144', '977111343', 'frutas')

#a = ControllerCategoria()
# a.cadastrar_categoria('games')

# a = ControllerFornecedor()
# a.cadastrar_fornecedor('CerealWorld Company', '99974927000144',
#                        '966611343', 'cereais')
