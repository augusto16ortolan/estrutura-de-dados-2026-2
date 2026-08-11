from Fila import Fila

class Hospital:

    def __init__(self):
        self._fila_prioridade = Fila()
        self._fila_normal = Fila()
        self._quantidade_prioridade_atendido = 0

    def cadastrar_paciente(self, nome, tipo_prioridade):
        if tipo_prioridade == 1:
            self._fila_prioridade.enqueue(nome)
            return 

        self._fila_normal.enqueue(nome)

    def atender_paciente(self):
        if not self._fila_prioridade.is_empty() and (self._quantidade_prioridade_atendido < 3 or self._fila_normal.is_empty()):
            self._quantidade_prioridade_atendido += 1
            return self._fila_prioridade.dequeue()

        if not self._fila_normal.is_empty():
            self._quantidade_prioridade_atendido = 0
            return self._fila_normal.dequeue()

        return None

    def exibir_order_atendimento(self):
        quantidade_em_prioridade = self._fila_prioridade.size()
        quantidade_em_normal = self._fila_normal.size()

        print("====== ORDEM DE ATENDIMENTO ======")

        contador = 1
        for paciente in self._fila_prioridade.get_lista_de_valores():
            print(f"Paciente {contador}: {paciente}")
            contador += 1

        for paciente in self._fila_normal.get_lista_de_valores():
            print(f"Paciente {contador}: {paciente}")
            contador += 1

    def exibir_quantidade_em_fila(self):
        quantidade_em_prioridade = self._fila_prioridade.size()
        quantidade_em_normal = self._fila_normal.size()
        quantidade_total = quantidade_em_prioridade + quantidade_em_normal

        print(f""""
            ===== QUANTIDADE DAS FILAS ====

            Fila de Prioridades = {quantidade_em_prioridade}
            Fila normal = {quantidade_em_normal}

            Total de pacientes em fila = {quantidade_total}    
        """)