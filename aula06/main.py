import os
from LSE import LSE
from Musica import Musica


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


def ler_texto_obrigatorio(mensagem, nome_campo):
    while True:
        texto = input(mensagem).strip()

        if texto == "":
            print(f"Erro: o {nome_campo} não pode estar vazio.")
            continue

        return texto


def exibir_menu():
    print("""
==============================
       PLAYLIST DE MÚSICAS
==============================
1 - Adicionar música no início
2 - Adicionar música no final
3 - Buscar música
4 - Remover música
5 - Exibir playlist
6 - Exibir quantidade de músicas
0 - Sair
==============================
""")


def cadastrar_musica(playlist):
    codigo = ler_inteiro("Digite o código da música: ")

    if codigo <= 0:
        print("Erro: o código da música deve ser maior que zero.")
        return None

    if playlist.buscar(codigo) is not None:
        print("Erro: já existe uma música cadastrada com esse código.")
        return None

    titulo = ler_texto_obrigatorio("Digite o título da música: ", "título")
    artista = ler_texto_obrigatorio("Digite o artista da música: ", "artista")

    return Musica(codigo, titulo, artista)


def buscar_musica(playlist):
    if playlist.is_empty():
        print("Não há músicas na playlist.")
        return

    codigo = ler_inteiro("Digite o código da música: ")
    musica = playlist.buscar(codigo)

    if musica is None:
        print("Música não encontrada.")
        return

    print(f"Música encontrada: {musica}")


def remover_musica(playlist):
    if playlist.is_empty():
        print("Não há músicas para remover.")
        return

    codigo = ler_inteiro("Digite o código da música: ")
    musica_removida = playlist.remover(codigo)

    if musica_removida is None:
        print("Música não encontrada para remoção.")
        return

    print(f"Música removida: {musica_removida}")


def main():
    playlist = LSE()

    while True:
        try:
            limpar_terminal()
            exibir_menu()

            opcao = ler_inteiro("Digite a opção desejada: ")

            if opcao == 1:
                musica = cadastrar_musica(playlist)

                if musica is not None:
                    playlist.inserir_inicio(musica)
                    print("Música adicionada no início da playlist.")

                pausar()

            elif opcao == 2:
                musica = cadastrar_musica(playlist)

                if musica is not None:
                    playlist.inserir_fim(musica)
                    print("Música adicionada no final da playlist.")

                pausar()

            elif opcao == 3:
                buscar_musica(playlist)
                pausar()

            elif opcao == 4:
                remover_musica(playlist)
                pausar()

            elif opcao == 5:
                playlist.imprimir_lista_completa()
                pausar()

            elif opcao == 6:
                print(f"Quantidade de músicas na playlist: {playlist.get_quantidade_de_dados()}")
                pausar()

            elif opcao == 0:
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


if __name__ == "__main__":
    main()
