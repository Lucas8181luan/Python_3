produtos =("Lápis", 1.75,
           "Borracha", 2,
           "Caderno", 15.90,
           "Estojo", 25,
           "Transferidor", 4.20,
           "Compasso", 9.99,
           "Mochila", 120.32,
           "Canetas", 22.30,
           "Livro", 34.90)

print("-" * 30)
print(f"{"LISTAGEM DE PREÇOS":^30}")
print("-" * 30)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f"{produtos[posição]:.<30}",end=" ")
    else:
        print(f"R${produtos[posição]:>7.2f}")
print("-" * 30)
