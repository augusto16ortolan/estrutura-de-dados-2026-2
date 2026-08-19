# a cada dado que recebemos, já colocamos no correto

def sort(lista):
    for i in range(1, len(lista)):

        valor_atual = lista[i]

        valor_anterior = i - 1

        while valor_anterior >= 0 and lista[valor_anterior] > valor_atual:
            lista[valor_anterior + 1] = lista[valor_anterior]
            valor_anterior -= 1

        lista[valor_anterior + 1] = valor_atual

numeros = [5, 2, 4, 7, 6, 1, 3]
print(numeros)
sort(numeros)
print(numeros)
