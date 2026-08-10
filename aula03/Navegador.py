from Pilha import Pilha
from Historico import Historico

class Navegador:

    def __init__(self):
        self._paginas_anteriores = Pilha()
        self._paginas_futuras = Pilha()
        self._pagina_atual = None
        self._historico_completo = [] # inicia zerado, mas no futuro conterá Historico (classe)

    def visitar(self, pagina):
        if pagina == self._pagina_atual:
            print(f"Voce já está na página {pagina}")
            return

        if self._pagina_atual != None:
            self._paginas_anteriores.push(self._pagina_atual)

        self._pagina_atual = pagina

        print(f"Navegado para {pagina}")

        self._historico_completo.append(Historico(pagina))

    def voltar(self):
        if self._paginas_anteriores.is_empty():
            print("Não há páginas para voltar")
            return

        self._paginas_futuras.push(self._pagina_atual)
        self._pagina_atual = self._paginas_anteriores.pop()

        print(f"Voltando para {self._pagina_atual}")

        self._historico_completo.append(Historico(self._pagina_atual))

    def avancar(self):
        if self._paginas_futuras.is_empty():
            print("Não há páginas para avançar")
            return

        self._paginas_anteriores.push(self._pagina_atual)
        self._pagina_atual = self._paginas_futuras.pop()

        print(f"Avançando para {self._pagina_atual}")

        self._historico_completo.append(Historico(self._pagina_atual))

    def get_pagina_atual(self):
        return self._pagina_atual

    def exibir_historico_completo(self):
        if len(self._historico_completo) == 0:
            print("Não há histórico de navegação")
            return

        print("\n===== HISTÓRICO COMPLETO =====")

        for historico in self._historico_completo:
            if historico.site == self._pagina_atual:
                print(f"Página atual -> {historico}")
                return

            print(historico)
        