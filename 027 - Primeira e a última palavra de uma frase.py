# VER A PRIMEIRA E A ÚLTIMA PALAVRA DE UMA FRASE

# Entrada, digitar uma frase
frase = str(input("Digite uma frase = ")).strip()

# Split, fatia uma frase
primeiro_nome = frase.split()
segundo_nome = frase.split()

print("Prazer!\nSeu primeiro nome é = {}\nSeu último nome é = {}".format(primeiro_nome[0], segundo_nome[len(segundo_nome) - 1]))

