# APRENDA A SORTEA UMA ORDEM NUMA LISTA

# Importe a biblioteca random
import random

# Entrada dos nomes na lista
primeiro = input("Primeiro nome = ")
segundo = input("Segundo nome = ")
terceiro = input("Terceiro nome = ")
quarto = input("Quarto nome = ")

# Criando a lista 
lista = [primeiro, segundo , terceiro , quarto] 

# colocando a ordem
random.shuffle(lista)

print("A ordem de apresentação será")
print(lista)

