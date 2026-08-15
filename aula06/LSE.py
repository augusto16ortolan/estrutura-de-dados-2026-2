from Nodo import Nodo


class LSE:

    def __init__(self):
        self._head = None # sempre inicia sem dados, entao o head é nulo
        self._tail = None # sempre inicia sem dados, entao o tail é nulo
        self._quantidade_itens = 0 # variavel de controle para ter um acesso rápido a quantidade de itens

    def is_empty(self):
        return self._head is None and self._tail is None and self._quantidade_itens == 0

    def inserir_inicio(self, dado_a_ser_inserido): # cria um nodo para inserir no inicio da LSE
        if dado_a_ser_inserido is None:
            raise ValueError("Valores nulos não podem ser adicionados.")

        nodo_a_ser_inserido = Nodo(dado_a_ser_inserido)

        if self.is_empty(): # verificamos se a lista está vazia, se estiver, head e tail recebem o novo nodo
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            self._quantidade_itens += 1
            return

        # caso nao for vazio, precisa adicionar a referencia do nodo anterior e setar o novo head
        nodo_a_ser_inserido.proximo = self._head
        self._head = nodo_a_ser_inserido

        self._quantidade_itens += 1

    def inserir_fim(self, dado_a_ser_inserido): # cria um nodo para inserir no fim da LSE
        if dado_a_ser_inserido is None:
            raise ValueError("Valores nulos não podem ser adicionados.")

        nodo_a_ser_inserido = Nodo(dado_a_ser_inserido)

        if self.is_empty(): # verificamos se a lista está vazia, se estiver, head e tail recebem o novo nodo
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            self._quantidade_itens += 1
            return

        # adicionamos a referencia no tail atual para o proximo dele ser o nodo_a_ser_inserido e mudamos a referencia do tail para o novo nodo_a_ser_inserido
        self._tail.proximo = nodo_a_ser_inserido
        self._tail = nodo_a_ser_inserido

        self._quantidade_itens += 1

    def buscar(self, codigo): # percorre a LSE procurando uma musica pelo codigo
        if self.is_empty():
            return None

        item = self._head

        while item is not None:
            if item.valor.codigo == codigo:
                return item.valor

            item = item.proximo

        return None

    def remover(self, codigo): # remove uma musica pelo codigo
        if self.is_empty():
            return None

        if self._head.valor.codigo == codigo:
            return self.remover_inicio()

        item_anterior = self._head
        item_atual = self._head.proximo

        while item_atual is not None:
            if item_atual.valor.codigo == codigo:
                musica_removida = item_atual.valor
                item_anterior.proximo = item_atual.proximo

                if item_atual == self._tail:
                    self._tail = item_anterior

                item_atual.proximo = None
                self._quantidade_itens -= 1
                return musica_removida

            item_anterior = item_atual
            item_atual = item_atual.proximo

        return None

    def remover_inicio(self): # remove o head e aponta para uma nova referencia caso tiver mais do que um dado na LSE
        if self.is_empty():
            print("Não há músicas para remover.")
            return None

        if self._head == self._tail and self._quantidade_itens == 1:
            musica_removida = self._head.valor
            self._tail = None
            self._head = None
            self._quantidade_itens -= 1
            return musica_removida

        nodo_removido = self._head # guardamos o nodo que será removido
        self._head = nodo_removido.proximo # setamos o novo head
        nodo_removido.proximo = None # removemos a referencia do nodo removido para o proximo que é o novo head

        self._quantidade_itens -= 1

        return nodo_removido.valor

    def remover_fim(self): # remove o tail e aponta para uma nova referencia caso tiver mais do que um dado na LSE
        if self.is_empty():
            print("Não há músicas para remover.")
            return None

        if self._head == self._tail and self._quantidade_itens == 1:
            musica_removida = self._tail.valor
            self._tail = None
            self._head = None
            self._quantidade_itens -= 1
            return musica_removida

        # precisamos descobrir qual valor é o penultimo dado da lista, ou seja, o valor que tenha o .proximo == tail será o penultimo dado
        item = self._head

        while item is not None:
            if item.proximo == self._tail:
                nodo_removido = item.proximo
                item.proximo = None
                self._tail = item
                self._quantidade_itens -= 1
                return nodo_removido.valor

            item = item.proximo

        return None

    def imprimir_lista_completa(self): # imprimir todos os dados da playlist
        if self.is_empty():
            print("Não há músicas na playlist.")
            return

        print("===== PLAYLIST COMPLETA =====")

        item = self._head
        contador = 1

        while item is not None:
            print(f"{contador} - {item.valor}")
            item = item.proximo
            contador += 1

    def imprimir_lista(self): # mantem o mesmo nome usado no exemplo da aula
        self.imprimir_lista_completa()

    def imprimir_lado_a_lado(self): # imprimir todos os dados um do lado do outro
        saida = ""

        item = self._head
        while item is not None:
            if item == self._head and item == self._tail:
                saida += f"(HEAD) {item.valor} (TAIL)"
                break

            if item == self._head:
                saida += f"(HEAD) {item.valor} -> "
                item = item.proximo
                continue

            if item == self._tail:
                saida += f"{item.valor} (TAIL)"
                item = item.proximo
                continue

            saida += f"{item.valor} -> "

            item = item.proximo

        print(saida)

    def get_quantidade_de_dados(self):
        return self._quantidade_itens
