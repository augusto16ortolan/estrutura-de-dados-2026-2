# faz a comparacao entre vizinhos e troca se necessário

def sort(lista):
    quantidade_de_dados = len(lista)

    for i in range(quantidade_de_dados):

        fez_substituicao = False

        for j in range(0, quantidade_de_dados - i - 1):

            if lista[j] > lista[j + 1]:
                print(f"Troca: {lista[j], lista[j + 1]}")
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # aqui fazemos a troca de posicao do index
                fez_substituicao = True

        if not fez_substituicao:
            break    


numeros = [5, 2, 4, 7, 6, 1, 3]
sort(numeros)
print(numeros)