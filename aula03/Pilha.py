# PascalCase = sempre a primeira letra de cada palavra será maiuscula
# cammelCase = a primeira leta da primeira palavra sera minuscula, e as primeiras letras das palavras restantes serao maiusculas
# snake_case = separa as palavras com "underline" (_)

class Pilha:

    def __init__(self):
        self._lista_de_valores = [] # valores que representarao a pilha

    def push(self, valor): # metodo de empilhar valores
        # self._lista_de_valores.append(valor) # utilizamos o metodo append (adiciona no final da lista) da lista para adicionar um valor
        self._lista_de_valores.insert(0, valor) # utilizamos o metodo insert (adiciona no inicio da lista) da lista para adicionar um valor

    def is_empty(self): # metodo para verificar se a lista de valores esta vazia
        return len(self._lista_de_valores) == 0

    def pop(self):
        # pré-condicao - deve existir dados na pilha
        if self.is_empty():
            raise IndexError("A pilha está vazia, não há dados para remover")

        # pós-condicao - remove e retorna o topo da pila (sempre cuidar como o push foi implementado para implementar o pop corretamente)
        return self._lista_de_valores.pop(0)

    def peek(self):
        # pré-condicao - deve existir dados na pilha
        if self.is_empty():
            raise IndexError("A pilha está vazia, não há dados para retornar")

        # pós-condicao - retorna o valor do topo, mantendo a pilha no mesmo estado
        # return self.__lista_de_valores[-1] 
        return self._lista_de_valores[0]

    def __len__(self):
        return len(self._lista_de_valores)
