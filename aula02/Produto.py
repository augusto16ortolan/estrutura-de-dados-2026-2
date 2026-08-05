
class Produto:
    proximoCodigo = 1

    def __init__(self, nome, quantidade, valor, fornecedor, codigoDeBarras):

        if nome == None:
            raise ValueError("Nome é obrigatorio")

        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")

        if valor < 0:
            raise ValueError("Valor não pode ser negativo")

        self.codigo = Produto.proximoCodigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.fornecedor = fornecedor
        self.codigoDeBarras = codigoDeBarras

        Produto.proximoCodigo += 1

    def __str__(self):
        return f"Produto {self.codigo}: {self.nome}, quantidade em estoque: {self.quantidade} e preço de venda R${self.valor}"

    def __len__(self):
        return self.quantidade

    def copy(self):
        return Produto(self.nome, self.quantidade, self.valor)

    def vender(self, quantidadeVendida):
        if quantidadeVendida > self.quantidade:
            raise ValueError("Quantidade excedida para esse produto")

        self.quantidade -= quantidadeVendida
        print(f"Venda do produto {self.nome}, quantidade da venda {quantidadeVendida} e valor da venda R${self.valor * quantidadeVendida}")
