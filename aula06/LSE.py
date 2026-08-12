from Nodo import Nodo

class LSE:

    def __init__(self):
        self._head = None # sempre inicia sem dados, entao o head é nulo
        self._tail = None # sempre inicia sem dados, entao o tail é nulo
        self._quantidade_de_itens = 0 # variavel de controle para ter um acesso rápido a quantidade de itens

    def is_empty(self):
            return self._head is None and self._tail is None and self._quantidade_de_itens == 0

    def inserir_inicio(self, valor): # valor sempre será simples, e precisamos criar um nodo para inserir no inicio da LSE
        if valor is None:
            raise ValueError("Valores nulos nao podem ser adicionados")

        nodo_a_ser_inserido = Nodo(valor)

        if self.is_empty(): # verificamos se a lista está vazia, se estiver, head e tail recebem o novo nodo
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            return

        # caso nao for vazio, precisa adicionar a referencia do nodo anterior e setar o novo head
        nodo_a_ser_inserido.proximo = self._head
        self._head = nodo_a_ser_inserido       

        self._quantidade_de_itens += 1     
        

    def inserir_fim(self, valor):  # valor sempre será simples, e precisamos criar um nodo para inserir no fim da LSE
        if valor is None:
            raise ValueError("Valores nulos nao podem ser adicionados")

        nodo_a_ser_inserido = Nodo(valor)

        if self.is_empty(): # verificamos se a lista está vazia, se estiver, head e tail recebem o novo nodo
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            return

        # adicionamos a referencia no tail atual para o proximo dele ser o nodo_a_ser_inserido e mudamos a referencia do tail para o novo nodo_a_ser_inserido
        self._tail.proximo = nodo_a_ser_inserido
        self._tail = nodo_a_ser_inserido

        self._quantidade_de_itens += 1

    def remover_inicio(self): # remove o head e aponta para uma nova referencia caso tiver mais do que um dado na LSE
        pass

    def remover_fim(self): # remove o tail e aponta para uma nova referencia caso tiver mais do que um dado na LSE
        pass

    def buscar(self, valor):
        pass

    def imprimir_lista(self): # imprimir todos os dados da LSE
        if self.is_empty():
            print("Não há dados na lista")
            return

        print("===== LISTA COMPLETA =====")

        item = self._head

        while item is not None:
            print(item)
            item = item.proximo

        print("===== RESUMO =====")
        print(f"HEAD -> {self._head}")
        print(f"TAIL -> {self._tail}")

    def imprimir_lado_a_lado(self): # imprimir todos os dados um do lado do outro
        # ex: HEAD -> 10 -> 20 -> 30 -> NONE (TAIL)
        pass

    def get_quantidade_de_dados(self):
        return self._quantidade_de_itens


lse = LSE()
lse.inserir_inicio(10)
lse.inserir_inicio(20)
lse.inserir_fim(30)
lse.imprimir_lista()

    