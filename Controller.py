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
                sys.exit('Primeira categoria cadastrada com sucesso.\n')

            for cat in categorias:
                if nova_categoria == cat.categoria:
                    existe = True

            if not existe:
                DaoCategoria.salvar(Categoria(nova_categoria))
                print('categoria cadastrada com sucesso.\n')
            else:
                print('A categoria que deseja cadastrar já existe.\n')
        except Exception as err:
            print(err)

    def remover_categoria(self, categoria_remover):
        try:
            categorias = DaoCategoria.ler()

            cat_lista = list(
                filter(lambda categorias: categorias.categoria == categoria_remover, categorias))

            if len(cat_lista) <= 0:
                print('Esta categoria não existe para ser removida.\n')
            else:
                for i in range(len(categorias)):
                    if categorias[i].categoria == cat_lista[0].categoria:
                        del categorias[i]
                        print(
                            f"Categoria '{cat_lista[0].categoria}' foi excluida.\n")
                        break

                with open('categorias.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                    for cat in categorias:
                        arq.writelines(cat.categoria)
                        arq.writelines('\n')

            if estoque:
                estoque = DaoEstoque.ler()

                estoque = list(
                    map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, Categoria("Sem estoque")), x.quantidade)
                        if(x.produto.categoria.categoria == categoria_remover) else(x), estoque))

                with open('estoque.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                                       i.produto.categoria.categoria + '|' + str(i.quantidade))
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
                    print('A alteração é efetuada com sucesso.\n')

                    estoque = DaoEstoque.ler()

                    estoque = list(
                        map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, Categoria(categoria_alterada)), x.quantidade)
                            if(x.produto.categoria.categoria == categoria_alterar) else(x), estoque))

                    with open('estoque.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                        for i in estoque:
                            arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                                           i.produto.categoria.categoria + '|' + str(i.quantidade))
                            arq.writelines('\n')

                else:
                    print('A categoria que deseja alterar já existe.\n')
            else:
                print('A categoria que deseja alterar não existe.\n')

            with open('categorias.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                for i in categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        except Exception as err:
            print(err)

    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        if not categorias:
            print('Categoria vazia.\n')
        else:
            for cat in categorias:
                print(f'Categoria: {cat.categoria}')
        print('\n')


class ControllerEstoque:

    def cadastrar_produto(self, nome_prod, preco_prod, categoria_prod, quantidade):
        estoque = DaoEstoque.ler()
        categoria = DaoCategoria.ler()

        cat = list(filter(lambda estoque: estoque.categoria ==
                          categoria_prod, categoria))

        if cat:
            if not estoque:
                DaoEstoque.salvar(
                    Produto(nome_prod, preco_prod, Categoria(categoria_prod)), int(quantidade))
                print('Primeiro produto cadastrado com sucesso.\n')
            else:
                prod_em_estoque = list(
                    filter(lambda estoque: estoque.produto.nome == nome_prod, estoque))

                if not prod_em_estoque:
                    DaoEstoque.salvar(
                        Produto(nome_prod, preco_prod, Categoria(categoria_prod)), int(quantidade))
                    print('Produto cadastrado com sucesso.\n')
                else:
                    print('Produto já existe em estoque.\n')
        else:
            print('Categoria inexistente.\n')

    def remover_produto(self, nome):
        estoque = DaoEstoque.ler()
        prod = list(
            filter(lambda estoque: estoque.produto.nome == nome, estoque))
        if prod:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == nome:
                    del estoque[i]
                    break
            print('O produto foi removido com sucesso.\n')
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
                        print('O produto foi alterado com sucesso.\n')
                else:
                    print('Produto já cadastrado\n')
            else:
                print('O produto que deseja alterar não existe.\n')
        else:
            print('A categoria informada não existe\n')

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
                    if int(i.quantidade) >= int(quantidadeVendida):
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

        if not vendas:
            print('Ainda não tem vendas para visualizar.\n')

        else:
            for i in vendas:
                nome = i.item_vendido.nome
                quantidade = i.quantidade_vendida
                tamanho = list(
                    filter(lambda x: x['produto'] == nome, produtos))
                if tamanho:
                    produtos = list(map(lambda x: {'produto': nome,
                                                   'quantidade': int(x['quantidade']) + int(quantidade)}
                                        if(x['produto'] == nome) else(x), produtos))
                else:
                    produtos.append({'produto': nome,
                                     'quantidade': quantidade})

            ordenado = sorted(
                produtos, key=lambda k: k['quantidade'], reverse=True)

            print('Este são os produtos mais vendidos\n')

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
            print(f"Nome: {i.item_vendido.nome}\n"
                  f"Preço: R${i.item_vendido.preco}\n"
                  f"Categoria: {i.item_vendido.categoria.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade Vendida: {i.quantidade_vendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += float(i.item_vendido.preco) * int(i.quantidade_vendida)
            count += 1

        print(f"Total vendido : R${total:.2f}\n")


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
                print('Primeiro fornecedor foi cadastrado com sucesso.\n')
            else:
                fornec_existente = list(filter(lambda x: x.nome ==
                                               nome_fornec, fornecedores))

                cnpj_existente = list(filter(lambda x: x.cnpj ==
                                             cnpj, fornecedores))

                telefone_existente = list(filter(lambda x: x.telefone ==
                                                 telefone, fornecedores))

                if not fornec_existente:
                    if not cnpj_existente:
                        if not telefone_existente:
                            DaoFornecedor.salvar(Fornecedor(
                                nome_fornec, cnpj, telefone, Categoria(categoria)))
                            print('O fornecedor foi cadastrado com sucesso.\n')
                        else:
                            print('Telefone já existente\n')
                    else:
                        print('cnpj já existente\n')
                else:
                    print(
                        'O fornecedor que desejar cadastrar já se encontra no nosso banco de dados\n')
        else:
            print(
                'A categoria informada não existe, é necessário cadastrá-la antes\n')

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

    def remover_fornecedor(self, nome):
        fornecedores = DaoFornecedor.ler()

        fornec = list(
            filter(lambda x: x.nome == nome, fornecedores))

        if fornec:
            for i in range(len(fornecedores)):
                if fornecedores[i].nome == nome:
                    del fornecedores[i]
                    print('O fornecedor foi removido com sucesso.\n')
                    break
        else:
            print('O fornecedor que deseja remover não existe\n')

        with open('fornecedor.txt', 'w', encoding='UTF-8', errors='replace') as arq:
            for i in fornecedores:
                arq.writelines(i.nome + '|' + i.cnpj + '|' +
                               i.telefone + '|' + i.categoria.categoria)
                arq.writelines('\n')

    def mostrar_fornecedor(self):
        fornecedores = DaoFornecedor.ler()

        if not fornecedores:
            print('Estoque vazio')
        else:
            print('==========Fornecedores==========')
            for i in fornecedores:
                print(
                    f'Nome: {i.nome}\n'
                    f'CNPJ: {i.cnpj}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Categoria: {i.categoria.categoria}'
                )
                print('--------------------')


class ControllerCliente:

    def cadastrar_cliente(self, nome_cliente, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado):
        clientes = DaoPessoa.ler()

        if not clientes:
            DaoPessoa.salvar(Pessoa(
                nome_cliente, telefone, cpf, email,
                Endereco(logradouro, numero, bairro, cep, cidade, estado)))
            print('Primeiro cliente foi cadastrado com sucesso.\n')

        else:
            cpf_existente = list(filter(lambda x: x.cpf == cpf, clientes))
            telefone_existente = list(
                filter(lambda x: x.telefone == telefone, clientes))
            email_existente = list(
                filter(lambda x: x.email == email, clientes))

            if not cpf_existente:
                if not email_existente:
                    if not telefone_existente:
                        DaoPessoa.salvar(Pessoa(
                            nome_cliente, telefone, cpf, email, Endereco(logradouro, numero, bairro, cep, cidade, estado)))
                        print('O cliente foi cadastrado com sucesso.\n')
                    else:
                        print('Telefone já existente\n')
                else:
                    print('email já existente\n')
            else:
                print(
                    'O cpf informado já se encontra no nosso banco de dados\n')

    def alterar_cliente(self, nome_alterar, nome_novo, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado):
        clientes = DaoPessoa.ler()

        cpf_list = list(
            filter(lambda x: x.cpf == cpf, clientes))

        if cpf_list:
            cliente_cadastrado = list(
                filter(lambda x: x.nome == nome_alterar, clientes))
            if cliente_cadastrado:
                cliente_existente = list(
                    filter(lambda x: x.nome == nome_novo, clientes))
                if not cliente_existente:
                    clientes = list(
                        map(
                            lambda x: Pessoa(nome_novo, telefone, cpf, email, Endereco(
                                logradouro, numero, bairro, cep, cidade, estado)) if(x.nome == nome_alterar) else(x), clientes))

                    with open('clientes.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                        for cliente in clientes:
                            arq.writelines(cliente.nome + '|' + cliente.telefone + '|' + cliente.cpf + '|' + cliente.email + '|' + cliente.endereco.logradouro + '|' +
                                           cliente.endereco.numero + '|' + cliente.endereco.bairro + '|' + cliente.endereco.cep + '|' + cliente.endereco.cidade + '|' + cliente.endereco.estado)
                            arq.writelines('\n')
                        print('O cliente foi alterado com sucesso.')
                else:
                    print('Fornecedor já cadastrado')
            else:
                print('O cliente que deseja alterar não existe.')
        else:
            print('O cpf informado não existe no nosso cadastro')

    def remover_cliente(self, nome):
        clientes = DaoPessoa.ler()

        cl = list(
            filter(lambda x: x.nome == nome, clientes))

        if cl:
            for i in range(len(clientes)):
                if clientes[i].nome == nome:
                    del clientes[i]
                    print('O cliente foi removido com sucesso.\n')
                    break
        else:
            print('O cliente que deseja remover não existe\n')

        with open('clientes.txt', 'w', encoding='UTF-8', errors='replace') as arq:
            for cliente in clientes:
                arq.writelines(cliente.nome + '|' + cliente.telefone + '|' + cliente.cpf + '|' + cliente.email + '|' + cliente.endereco.logradouro + '|' +
                               cliente.endereco.numero + '|' + cliente.endereco.bairro + '|' + cliente.endereco.cep + '|' + cliente.endereco.cidade + '|' + cliente.endereco.estado)
                arq.writelines('\n')

    def mostrar_cliente(self):
        clientes = DaoPessoa.ler()

        if not clientes:
            print('Não há clientes cadastrados\n')
        else:
            print('==========Clientes==========')
            for i in clientes:
                print(
                    f'Nome:     {i.nome}\n'
                    f'CPF:      {i.cpf}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Email:    {i.email}\n'
                    f'Rua:      {i.endereco.logradouro}\n'
                    f'Numero:   {i.endereco.numero}\n'
                    f'Bairro:   {i.endereco.bairro}\n'
                    f'Cep:      {i.endereco.cep}\n'
                    f'Cidade:   {i.endereco.cidade}\n'
                    f'Estado:   {i.endereco.estado}\n'
                )
                print('--------------------')


class ControllerFuncionario:

    def cadastrar_funcionario(self, clt, nome_func, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado):
        funcionarios = DaoFuncionario.ler()

        if not funcionarios:
            DaoFuncionario.salvar(Funcionario(
                clt, nome_func, telefone, cpf, email,
                Endereco(logradouro, numero, bairro, cep, cidade, estado)))
            print('Primeiro funcionário foi cadastrado com sucesso.\n')

        else:
            cpf_existente = list(filter(lambda x: x.cpf == cpf, funcionarios))
            clt_existente = list(filter(lambda x: x.clt == clt, funcionarios))
            telefone_existente = list(
                filter(lambda x: x.telefone == telefone, funcionarios))
            email_existente = list(
                filter(lambda x: x.email == email, funcionarios))

            if not cpf_existente:
                if not clt_existente:
                    if not email_existente:
                        if not telefone_existente:
                            DaoFuncionario.salvar(Funcionario(
                                clt, nome_func, telefone, cpf, email, Endereco(logradouro, numero, bairro, cep, cidade, estado)))
                            print('O funcionário foi cadastrado com sucesso.')
                        else:
                            print('Telefone já existente')
                    else:
                        print('email já existente')
                else:
                    print('O registro da clt já existe')
            else:
                print(
                    'O cpf informado já se encontra no nosso banco de dados')

    def alterar_funcionario(self, nome_alterar, nome_novo, clt, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado):
        funcionarios = DaoFuncionario.ler()

        cpf_list = list(
            filter(lambda x: x.cpf == cpf, funcionarios))

        if cpf_list:
            funcionario_cadastrado = list(
                filter(lambda x: x.nome == nome_alterar, funcionarios))
            if funcionario_cadastrado:
                funcionario_existente = list(
                    filter(lambda x: x.nome == nome_novo, funcionarios))
                if not funcionario_existente:
                    funcionarios = list(
                        map(
                            lambda x: Funcionario(clt, nome_novo, telefone, cpf, email, Endereco(
                                logradouro, numero, bairro, cep, cidade, estado)) if(x.nome == nome_alterar) else(x), funcionarios))

                    with open('funcionarios.txt', 'w', encoding='UTF-8', errors='replace') as arq:
                        for funcionario in funcionarios:
                            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + '|' + funcionario.email + '|' + funcionario.endereco.logradouro + '|' +
                                           funcionario.endereco.numero + '|' + funcionario.endereco.bairro + '|' + funcionario.endereco.cep + '|' + funcionario.endereco.cidade + '|' + funcionario.endereco.estado)
                            arq.writelines('\n')
                        print('O funcionario foi alterado com sucesso.')
                else:
                    print('Funcionario já cadastrado')
            else:
                print('O funcionario que deseja alterar não existe.')
        else:
            print('O cpf informado não existe no nosso cadastro')

    def remover_funcionario(self, nome):

        funcionarios = DaoFuncionario.ler()

        func = list(
            filter(lambda x: x.nome == nome, funcionarios))

        if func:
            for i in range(len(funcionarios)):
                if funcionarios[i].nome == nome:
                    del funcionarios[i]
                    print('O funcionário foi removido com sucesso.')
                    break
        else:
            print('O funcionário que deseja remover não existe')

        with open('funcionarios.txt', 'w', encoding='UTF-8', errors='replace') as arq:
            for funcionario in funcionarios:
                arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + '|' + funcionario.email + '|' + funcionario.endereco.logradouro + '|' +
                               funcionario.endereco.numero + '|' + funcionario.endereco.bairro + '|' + funcionario.endereco.cep + '|' + funcionario.endereco.cidade + '|' + funcionario.endereco.estado)
                arq.writelines('\n')

    def mostrar_funcionario(self):
        funcionarios = DaoFuncionario.ler()

        if not funcionarios:
            print('Não há funcionarios cadastrados\n')
        else:
            print('==========Funcionários==========')
            for i in funcionarios:
                print(
                    f'Nome:     {i.nome}\n'
                    f'CLT:     {i.clt}\n'
                    f'CPF:      {i.cpf}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Email:    {i.email}\n'
                    f'Rua:      {i.endereco.logradouro}\n'
                    f'Numero:   {i.endereco.numero}\n'
                    f'Bairro:   {i.endereco.bairro}\n'
                    f'Cep:      {i.endereco.cep}\n'
                    f'Cidade:   {i.endereco.cidade}\n'
                    f'Estado:   {i.endereco.estado}\n'
                )
                print('--------------------')
