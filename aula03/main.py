from Pilha import Pilha

pilha1 = Pilha() # []
pilha1.push(1) # [1]
pilha1.push("A") # [A, 1]
pilha1.push("Augusto") # [Augusto, A, 1]
pilha1.push(2)
pilha1.push("B")
pilha1.pop()
pilha1.pop()
pilha1.pop()
pilha1.push(4836473)
print(pilha1.peek())