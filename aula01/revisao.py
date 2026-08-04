import random

'''
print("Hello World") #debugar = verificar linha a linha o nosso código

nome = "Augusto"
idade = 25
altura = 1.66
vivo = True

print(type(nome))
'''

#idade = int(input("Digite a sua idade: "));
#print(idade)

# operadores aritmeticos
# + soma
# - subtracao
# * multiplicacao
# / divisao
# // divisao inteira
# % resto
# ** potencia

# resultado = 11 % 2
# print(resultado)

# operadores relacionais
# igualdade ==
# diferenca !=
# maior >
# menor <
# maior igual >= 
# menor igual <=

# estruturas condicionais
# if elif else

# operadores lógicos (and, or, not)
'''
nota = 7

if nota >= 3 or nota < 7:
    print("Exame")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

idade = 17

if not idade >= 18:
    print("Menor de idade")
else:
    print("Maior de idade")
'''    

# While
''' 
contador = 0

while contador < 10:
    print(contador)
    contador += 1

    if contador == 5:
        break
''' 

# for
''' 
for numero in range(1, 10):
    print(numero)


# listas
listaDeNomes = ["Maria", "Lucas"]
listaDeNomes.append("Augusto")
listaDeNomes.append("Joao")

for nome in listaDeNomes:
    print(nome)
''' 

# funcoes
'''
def somaNumeros(numero1, numero2):
    return numero1 + numero2

print(somaNumeros(5, 5))
'''

# manipulacao de textos
'''
nome = "Augusto"
idade = 25
print("Meu nome é " + nome + ", tenho " + str(idade) + " anos")
print(f"Meu nome é {nome}, tenho {str(idade)} anos")
'''

# tratamento de erros

try:
    idade = 5 + "5"
except:
    print("Ocorreu um erro ao declarar a variavel idade")


# importacao de modulos
sorteio = random.randint(1, 56)
print(sorteio)