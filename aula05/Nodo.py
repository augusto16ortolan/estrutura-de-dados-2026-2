
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

nodo1 = Nodo("Augusto")
nodo2 = Nodo("Joao")
nodo1.proximo = nodo2
nodo3 = Nodo("Maria")
nodo2.proximo = nodo3
nodo4 = Nodo("Lucas")
nodo3.proximo = nodo4

# item = nodo1

# while True:
#     if item.proximo == None:
#         print(item.valor)
#         break

#     print(item.valor)
#     item = item.proximo

atual = nodo1

while atual != None:
    print(atual.valor)
    atual = atual.proximo