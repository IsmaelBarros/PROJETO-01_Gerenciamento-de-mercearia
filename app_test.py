from DAO import *
from Models import *

cat1 = Categoria('bebidas')
cat2 = Categoria('frios')
cat3 = Categoria('hortifrutti')
cat4 = Categoria('carnes')

cat_dao = DaoCategoria()
# cat_dao.salvar(cat1)
# cat_dao.salvar(cat2)
# cat_dao.salvar(cat3)
# cat_dao.salvar(cat4)

print('------------------')
lista_cat = cat_dao.ler()
for cat in lista_cat:
    print(cat.categoria)
print('------------------')

prod1 = Produto('cerveja', '2.99', lista_cat[0].categoria)
print(prod1.nome, prod1.preco, prod1.categoria)
prod2 = Produto('presunto', '8.49', lista_cat[1].categoria)
print(prod2.nome, prod2.preco, prod2.categoria)

# venda1 = Venda(prod1, 'Maira', 'Ismael', '1')
# print(venda1.item_vendido.nome)
# venda2 = Venda(prod2, 'Joao', 'Jesus', '2')
# print(venda2.item_vendido.nome)


#venda_dao = DaoVenda()
# venda_dao.salvar(venda1)
# venda_dao.salvar(venda2)

# print('-------------------')
# lista_de_vendas = venda_dao.ler()
# for venda in lista_de_vendas:
#     print(venda.item_vendido.nome)
#     print(venda.item_vendido.categoria.categoria)
# print('------------------')


estoque1 = Estoque(prod1, '10')
estoque2 = Estoque(prod2, '20')

estoque_dao = DaoEstoque()
#estoque_dao.salvar(estoque1.produto, estoque1.quantidade)
#estoque_dao.salvar(estoque2.produto, estoque2.quantidade)

print('-----------------------------')
lista_estoque = estoque_dao.ler()
for estoque in lista_estoque:
    print(estoque.produto.nome)
    print(estoque.produto.preco)
    print(estoque.produto.categoria.categoria)
    print(estoque.quantidade)
    print('------------------')


fornec1 = Fornecedor('Christian', '44.345.678.00001-01', '43566578', cat1)
fornec2 = Fornecedor('Isabel', '44.345.333.00001-01', '11166578', cat3)
fornec3 = Fornecedor('jaqueline', '77.345.678.00001-01', '99566578', cat4)

fornec_dao = DaoFornecedor()
# fornec_dao.salvar(fornec1)
# fornec_dao.salvar(fornec2)
# fornec_dao.salvar(fornec3)

print('--------------------')
fornec_list = fornec_dao.ler()
for item in fornec_list:
    print(item.nome)
    print(item.cnpj)
    print(item.telefone)
    print(item.categoria.categoria)
print('--------------------')

# end1 = Endereco('Ipê Amarelo', '90', 'pq das Oliveiras',
#                 '99845210', 'sbc', 'sp')
# cliente1 = Pessoa('Marcel', '92173254', '75646464798',
#                   'marcel@google.com', end1)

# cliente2 = Pessoa('Silvio', '66663254', '88886464798',
#                   'silvio@google.com', end1)


#dao_cliente = DaoPessoa()
# dao_cliente.salvar(cliente1)
# dao_cliente.salvar(cliente2)

# print('--------------------')
# lista_clientes = dao_cliente.ler()
# for cliente in lista_clientes:
#     print(cliente.endereco.logradouro)
# print('--------------------')


# func1 = Funcionario('444555', 'Sidnelson', '87912323',
#                     '32222288876', 'sid@hotmail.com', end1)
# dao_func = DaoFuncionario()
# # dao_func.salvar(func1)

# print('--------------------')
# lista_func = dao_func.ler()
# for funcionario in lista_func:
#     print(funcionario.clt)
# print('--------------------')

end1 = Endereco('rua micatório', 660,
                'São Clemente', '07234440', 'diadema', 'sp')
dao_end = DaoEndereco()
# dao_end.salvar(end1)

print('--------------------')
list_end = dao_end.ler()
for end in list_end:
    print(end.logradouro)
print('--------------------')
