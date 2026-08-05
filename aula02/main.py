from Produto import Produto
from Fornecedor import Fornecedor

try:
    produto1 = Produto("Notebook", 10, -2500.00, Fornecedor("Acer", "0000000000000"), "21212")
    produto2 = Produto("Celular", 25, 4000.00, Fornecedor("Apple", "6666666666666"), "21212")

    nomeProduto1 = "Notebook"
    quantidadeProduto1 = 10

    produto1.vender(12)
    produto1.vender(8)

    print(produto1)
    print(produto2)

    # print(produto1.fornecedor.razaoSocial)
except ValueError as e:
    error_message = str(e)
    print(f"The error message is: {error_message}")



