import os
from Hospital import Hospital

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Erro: digite um número inteiro válido.")

def ler_tipo_prioridade():
    while True:
        try:
            tipo_prioridade = ler_inteiro("Digite o tipo de prioridade (0 - Normal, 1 - Prioridade): ")

            if tipo_prioridade not in [0, 1]:
                raise ValueError("Erro: prioridade inválida. Use 0 ou 1.")

            return tipo_prioridade

        except ValueError as e:
            print(str(e))

def exibir_menu():
    print("""
        ==============================
                    MENU
        ==============================
        1 - Cadastrar paciente
        2 - Atender paciente
        3 - Exibir ordem de atendimento
        4 - Exibir quantidade em fila
        5 - Sair
        ==============================
        """)

hospital = Hospital()

while True:
    try:
        limpar_terminal()
        exibir_menu()

        opcao = ler_inteiro("Digite a opção desejada: ")

        if opcao == 1:
            nome_paciente = input("Digite o nome do paciente: ").strip()

            if nome_paciente == "":
                print("Erro: o nome do paciente não pode ser vazio.")
                pausar()
                continue

            tipo_prioridade = ler_tipo_prioridade()

            hospital.cadastrar_paciente(nome_paciente, tipo_prioridade)
            print("Paciente cadastrado com sucesso.")
            pausar()

        elif opcao == 2:
            paciente_atendido = hospital.atender_paciente()

            if paciente_atendido is None:
                print("Não há pacientes na fila.")
            else:
                print(f"Paciente atendido: {paciente_atendido}")

            pausar()

        elif opcao == 3:
            hospital.exibir_order_atendimento()
            pausar()

        elif opcao == 4:
            hospital.exibir_quantidade_em_fila()
            pausar()

        elif opcao == 5:
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Erro: opção inválida.")
            pausar()

    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
        break

    except Exception as e:
        print(f"Erro inesperado: {e}")
        pausar()