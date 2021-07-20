from Models import Categoria, Produto, Estoque, Venda, Fornecedor, Endereco, Pessoa, Funcionario
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

import os


class ControllerCategoria:

    def cadastrar_categoria(self, nova_categoria):
        try:
            categorias = DaoCategoria.ler()
            existe = False

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

            with open('categoria.txt', 'w') as arq:
                for cat in categorias:
                    arq.writelines(cat.categoria)
                    arq.writelines('\n')

    def alterar_categoria(self, categoria_alterar, categoria_alterada):
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

        with open('categorias.txt', 'w') as arq:
            for i in categorias:
                arq.writelines(i.categoria)
                arq.writelines('\n')

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
        prod_em_estoque = list(
            filter(lambda estoque: estoque.produto.nome == nome_prod, estoque))

        if cat:
            if len(prod_em_estoque) == 0:
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

        with open('estoque.txt', 'w') as arq:
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

                    with open('estoque.txt', 'w') as arq:
                        for est in estoque:
                            arq.writelines(est.produto.nome + '|' + est.produto.preco +
                                           '|' + est.produto.categoria.categoria + '|' + est.quantidade)
                            arq.writelines('\n')
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

        arq = open('estoque.txt', 'w')
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


#a = ControllerVenda()
# a.relatorio_vendas()
# a.cadastrar_venda('abacaxi', 'Aldebário José', 'Cleonilso', 10)
# a.cadastrar_venda('abacaxi', 'Aldebário José', 'Jeocidio', 15)
# a.cadastrar_venda('abacaxi', 'Aldebário José', 'Cleopatra', 5)
# a.cadastrar_venda('iphone', 'Arnaldo j jr', 'Serafim', 1)
# a.cadastrar_venda('iphone', 'Cristaldo', 'Amaral', 2)

#b = ControllerCategoria()
# b.cadastrarCategoria('frutas')

#x = ControllerEstoque()
#x.cadastrar_produto('abacaxi', 4.99, 'frutas', 100)
# x.mostrarEstoque()
#x.alterarProduto('smartphone', 'iphone', '900', 'portatil', '10')
# x.removerProduto('cerveja')
# cat1 = Categoria('portatil')
# DaoCategoria.salvar(cat1)
# p1 = Produto('smartphone', '1900', cat1)
# DaoEstoque.salvar(p1, 10)
# x.cadastrarProduto(p1, 10)
