from Pilha import Pilha
from Historico import Historico

class Navegador:

    def __init__(self):
        self._paginas_anteriores = Pilha()
        self._paginas_futuras = Pilha()
        self._pagina_atual = None
        self._historico_completo = [] # inicia zerado, mas no futuro conterá Historico (classe)

    def visitar(self, pagina):
        # a pagina que recebemos como parametro deve setar na pagina atual
        # caso a pagina atual anterior for diferente de None, deve ser incluida da pilha das anteriors
        # deve adicionar o pagina na lista de historicos _historico_completo.append(Historico(pagina))
        pass

    def voltar(self):
        # validar se existe alguma pagina anterior
        # se existir, o topo da pagina anterior vira a pagina atual
        # e a antiga pagina atual vai para a pilha de futuras
        # adicionar novamente no historico de navegacao
        pass

    def avancar(self):
        # validar se existe alguma pagina futura
        # se existir, o topo da pagina futura vira a pagina atual
        # e a antiga pagina atual vai para a pilha de anteriores
        # adicionar novamente no historico de navegacao
        pass

    def get_pagina_atual(self):
        # devolve a pagina atual
        pass

    def exibir_historico_completo(self):
        # iterar a lista de historico e printar cada objeto historico
        pass