
class Fornecedor:
    def __init__(self, razaoSocial, cnpj):
        self.razaoSocial = razaoSocial
        self.cnpj = cnpj

    def __str__(self):
        return f"Fornecedor: {self.razaoSocial} e CNPJ: {self.cnpj}"