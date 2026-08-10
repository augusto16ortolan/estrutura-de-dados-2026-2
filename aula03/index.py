import os
from Navegador import Navegador


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("""
        ==============================
                NAVEGADOR WEB
        ==============================
        1 - Visitar página
        2 - Voltar
        3 - Avançar
        4 - Exibir página atual
        5 - Exibir histórico completo
        0 - Sair
        ==============================
        """)


def main():
    navegador = Navegador()

    while True:
        clear()
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pagina = input("Digite a página que deseja visitar: ")
            navegador.visitar(pagina)

        elif opcao == "2":
            navegador.voltar()

        elif opcao == "3":
            navegador.avancar()

        elif opcao == "4":
            print(navegador.get_pagina_atual())

        elif opcao == "5":
            navegador.exibir_historico_completo()

        elif opcao == "0":
            print("\nNavegador encerrado.")
            break

        else:
            print("\nOpção inválida.")

        input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    main()