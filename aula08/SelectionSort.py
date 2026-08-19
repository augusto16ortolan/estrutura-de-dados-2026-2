# sempre busca o menor valor e adiciona no final da parte ordenada

def sort(lista):
    quantidade_de_itens = len(lista)

    contador_de_processos = 0
    for i in range(quantidade_de_itens):
        menor_valor = i # define o indice do menor dado conhecido

        for j in range(i + 1, quantidade_de_itens):

            if lista[j] < lista[menor_valor]:
                menor_valor = j

        lista[i], lista[menor_valor] = lista[menor_valor], lista[i]
        contador_de_processos += 1
        print(f"Troca {contador_de_processos} - {lista[i], lista[menor_valor]}")

numeros = [5, 2, 4, 7, 6, 1, 3]
sort(numeros)
print(numeros)