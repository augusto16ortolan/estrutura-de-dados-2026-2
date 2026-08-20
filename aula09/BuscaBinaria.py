
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = busca_binaria(lista, 5)
print(index)

