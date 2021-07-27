import controller


def menu():

    while True:
        print('================= Menu Principal ===============')

        try:
            local = int(input(
                'Digite 1 para acessar ( Categorias )\n'
                'Digite 2 para acessar ( Estoque )\n'
                'Digite 3 para acessar ( Fornecedor )\n'
                'Digite 4 para acessar ( Cliente )\n'
                'Digite 5 para acessar ( Funcionário )\n'
                'Digite 6 para acessar ( Vendas )\n'
                'Digite 7 para ver os produto mais vendidos\n'
                'Digite 8 para sair\n\n'
                'Opção escolhida : '
            ))
        except ValueError:
            print('\n')
            print('Digite um numero válido\n')
            continue

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para cadastrar uma categoria\n'
                        'Digite 2 para remover uma categoria\n'
                        'Digite 3 para alterar uma categoria\n'
                        'Digite 4 para mostrar as categorias cadastradas\n'
                        'Digite 5 para sair\n\n'
                        'Opcao escolhida : '))
                    print('\n')

                except ValueError:
                    print('\n')
                    print('Digite um numero válido.\n')
                    continue

                if decisao == 1:
                    categoria = input(
                        'Digite a categoria que deseja cadastrar\n')
                    cat.cadastrar_categoria(categoria)

                elif decisao == 2:
                    categoria = input(
                        'Digite uma categoria para ser removida\n')
                    cat.remover_categoria(categoria)

                elif decisao == 3:
                    categoria_alterar = input(
                        'Digite a categoria que será alterada\n')
                    categoria_alterada = input(
                        'Digite uma categoria nova que deseja cadastrar\n')
                    cat.alterar_categoria(
                        categoria_alterar, categoria_alterada)

                elif decisao == 4:
                    cat.mostrar_categoria()

                elif decisao == 5:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 2:
            estoque = controller.ControllerEstoque()
            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para cadastrar um produto\n'
                        'Digite 2 para remover um produto\n'
                        'Digite 3 para alterar um produto\n'
                        'Digite 4 para mostrar os produtos no estoque\n'
                        'Digite 5 para sair\n\n'
                        'Opcao escolhida : '
                    ))
                except ValueError:
                    print('\n')
                    print('Digite um número válido\n')
                    continue

                if decisao == 1:
                    nome = input(
                        'Digite o nome do produto que deseja cadastrar\n')
                    preco = input(
                        'Digite o preço do produto\n')
                    categoria = input(
                        'Digite a categoria do produto\n')
                    quantidade = input(
                        'Digite a quantidade de produtos que deseja cadastrar no estoque\n')

                    estoque.cadastrar_produto(
                        nome, preco, categoria, quantidade)

                elif decisao == 2:
                    nome = input(
                        'Digite o nome no produto que será removido\n')
                    estoque.remover_produto(nome)

                elif decisao == 3:
                    produto_alterar = input(
                        'Digite o nome do produto que será alterado\n')
                    produto_alterada = input(
                        'Digite o nome do novo produto\n')
                    preco = input(
                        'Digite o novo preço do produto\n')
                    categoria = input(
                        'Digite a nova categoria do produto\n')
                    quantidade = input(
                        'Digite a nova quantidade do produto\n')

                    estoque.alterar_produto(
                        produto_alterar, produto_alterada, preco, categoria, quantidade)

                elif decisao == 4:
                    estoque.mostrar_estoque()

                elif decisao == 5:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 3:
            fornecedor = controller.ControllerFornecedor()
            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para cadastrar um fornecedor\n'
                        'Digite 2 para remover um fornecedor\n'
                        'Digite 3 para alterar um fornecedor\n'
                        'Digite 4 para mostrar os fornecedores\n'
                        'Digite 5 para sair\n\n'
                        'Opcao escolhida : \n'
                    ))
                except ValueError:
                    print('\n')
                    print('Digite um número válido\n')
                    continue

                if decisao == 1:
                    nome = input(
                        'Digite o nome do fornecedor que deseja cadastrar\n')
                    cnpj = input(
                        'Digite o cnpj do fornecedor\n')
                    telefone = input(
                        'Digite o telefone do fornecedor\n')
                    categoria = input(
                        'Digite a categoria do fornecedor\n')

                    fornecedor.cadastrar_fornecedor(
                        nome, cnpj, telefone, categoria)

                elif decisao == 2:
                    nome = input(
                        'Digite o nome do fornecedor que será removido\n')
                    fornecedor.remover_fornecedor(nome)

                elif decisao == 3:
                    fornec_alterar = input(
                        'Digite o nome do fornecedor que será alterado\n')
                    fornec_alterada = input(
                        'Digite o nome do novo fornecedor\n')
                    cnpj = input(
                        'Digite o cnpj do fornecedor\n')
                    telefone = input(
                        'Digite o telefone do fornecedor\n')
                    categoria = input(
                        'Digite a categoria do fornecedor\n')

                    fornecedor.alterar_fornecedor(
                        fornec_alterar, fornec_alterada, cnpj, telefone, categoria,)

                elif decisao == 4:
                    fornecedor.mostrar_fornecedor()

                elif decisao == 5:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 4:
            cliente = controller.ControllerCliente()
            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para cadastrar um cliente\n'
                        'Digite 2 para remover um cliente\n'
                        'Digite 3 para alterar um cliente\n'
                        'Digite 4 para mostrar os clientes\n'
                        'Digite 5 para sair\n\n'
                        'Opcao escolhida : \n'
                    ))
                except ValueError:
                    print('\n')
                    print('Digite um número válido\n')
                    continue

                if decisao == 1:
                    nome = input(
                        'Digite o nome do cliente que deseja cadastrar\n')
                    telefone = input(
                        'Digite o telefone do cliente\n')
                    cpf = input(
                        'Digite o cpf do cliente\n')
                    email = input(
                        'Digite o email do cliente\n')
                    logradouro = input(
                        'Digite o logradouro do cliente\n')
                    numero = input(
                        'Digite o numero do cliente\n')
                    bairro = input(
                        'Digite o bairro do cliente\n')
                    cep = input(
                        'Digite o cep do cliente\n')
                    cidade = input(
                        'Digite a cidade do cliente\n')
                    estado = input(
                        'Digite o estado do cliente\n')

                    cliente.cadastrar_cliente(
                        nome, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado)

                elif decisao == 2:
                    nome = input(
                        'Digite o nome do cliente que será removido\n')
                    cliente.remover_cliente(nome)

                elif decisao == 3:
                    cliente_alterar = input(
                        'Digite o nome do cliente que será alterado\n')
                    cliente_alterada = input(
                        'Digite o nome do novo cliente\n')
                    telefone = input(
                        'Digite o telefone do cliente\n')
                    cpf = input(
                        'Digite o cpf do cliente\n')
                    logradouro = input(
                        'Digite o nome da rua do cliente\n')
                    numero = input(
                        'Digite o numero da residência\n')
                    bairro = input(
                        'Digite o bairro\n')
                    cep = input(
                        'Digite o cep\n')
                    cidade = input(
                        'Digite a cidade\n')
                    estado = input(
                        'Digite o estado\n')

                    cliente.alterar_cliente(
                        cliente_alterar, cliente_alterada, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado)

                elif decisao == 4:
                    cliente.mostrar_cliente()

                elif decisao == 5:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 5:

            funcionario = controller.ControllerFuncionario()

            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para cadastrar um funcionario\n'
                        'Digite 2 para remover um funcionario\n'
                        'Digite 3 para alterar um funcionario\n'
                        'Digite 4 para mostrar os funcionario\n'
                        'Digite 5 para sair\n\n'
                        'Opcao escolhida : \n'
                    ))
                except ValueError:
                    print('\n')
                    print('Digite um número válido\n')
                    continue

                if decisao == 1:
                    clt = input(
                        'Digite o registro da CLT do funcionario que deseja cadastrar\n')
                    nome = input(
                        'Digite o nome do funcionario que deseja cadastrar\n')
                    telefone = input(
                        'Digite o telefone do funcionario\n')
                    cpf = input(
                        'Digite o cpf do funcionario\n')
                    email = input(
                        'Digite o email do funcionario\n')
                    logradouro = input(
                        'Digite o logradouro do funcionario\n')
                    numero = input(
                        'Digite o numero do funcionario\n')
                    bairro = input(
                        'Digite o bairro do funcionario\n')
                    cep = input(
                        'Digite o cep do funcionario\n')
                    cidade = input(
                        'Digite a cidade do funcionario\n')
                    estado = input(
                        'Digite o estado do funcionario\n')

                    funcionario.cadastrar_funcionario(
                        clt, nome, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado)

                elif decisao == 2:
                    nome = input(
                        'Digite o nome do funcionario que será removido\n')
                    funcionario.remover_funcionario(nome)

                elif decisao == 3:
                    funcionario_alterar = input(
                        'Digite o nome do funcionario que será alterado\n')
                    funcionario_alterada = input(
                        'Digite o nome do novo funcionario\n')
                    clt = input(
                        'Digite o registro CLT do funcionario\n')
                    telefone = input(
                        'Digite o telefone do funcionario\n')
                    cpf = input(
                        'Digite o cpf do funcionario\n')
                    email = input(
                        'Digite o email do funcionario\n')
                    logradouro = input(
                        'Digite o nome da rua do funcionario\n')
                    numero = input(
                        'Digite o numero da residência\n')
                    bairro = input(
                        'Digite o bairro\n')
                    cep = input(
                        'Digite o cep\n')
                    cidade = input(
                        'Digite a cidade\n')
                    estado = input(
                        'Digite o estado\n')

                    funcionario.alterar_funcionario(
                        funcionario_alterar, funcionario_alterada, clt, telefone, cpf, email, logradouro, numero, bairro, cep, cidade, estado)

                elif decisao == 4:
                    funcionario.mostrar_funcionario()

                elif decisao == 5:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 6:
            vendas = controller.ControllerVenda()
            while True:
                try:
                    decisao = int(input(
                        'Digite 1 para realizar uma venda\n'
                        'Digite 2 para ver o relatório de vendas\n'
                        'Digite 3 para mostrar as vendas\n'
                        'Digite 4 para sair\n\n'
                        'Opcao escolhida : \n'
                    ))
                except ValueError:
                    print('\n')
                    print('Digite um número válido\n')
                    continue

                if decisao == 1:
                    nome = input(
                        'Digite o nome do produto que foi vendido\n')
                    vendedor = input(
                        'Digite o vendedor que fez a venda\n')
                    comprador = input(
                        'informe o comprador\n')
                    quantidade_vendida = input(
                        'Digite a quantidade deste produto que foi vendida\n')

                    vendas.cadastrar_venda(
                        nome, vendedor, comprador, quantidade_vendida)

                elif decisao == 2:
                    vendas.relatorio_vendas()

                elif decisao == 3:
                    data_inicio = input(
                        'Digite a data de inicio da pesquisa (dd/mm/yyy) : \n')
                    data_termino = input(
                        'Digite a data de termino da pesquisa (dd/mm/yyy) : \n')

                    vendas.mostrar_vendas(data_inicio, data_termino)

                elif decisao == 4:
                    break

                else:
                    print('Esta opção não é válida.')

        elif local == 7:
            vendas = controller.ControllerVenda()
            vendas.relatorio_vendas()

        elif local == 8:
            break

        else:
            print('Opção inválida')
