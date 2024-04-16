# 1 ()
# **
# * / // %
# + -

# APRENDA A SORTEA UM ITEM NUMA LISTA

# Importe random
import random

# Entrada, dos nomes na lista
primeiro = str(input("Primeiro nome = "))
segundo = str(input("Segundo nome = "))
terceiro = str(input("Terceiro nome = "))
quarto = str(input("Quarto nome = "))

# Criando a lista
lista = [primeiro, segundo, terceiro, quarto]

# Fazer o sorteio, usando a biblioteca random
escolhido = random.choice(lista)

print("O sorteado foi = {}".format(escolhido))
