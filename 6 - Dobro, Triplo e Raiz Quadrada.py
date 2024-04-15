# 1 ()
# **
# * / // %
# + -

# UM PROGRAMA QUE LEIA UM NÚMERO, E MOSTRE SEU DOBRO, TRIPLO E RAIZ QUADRADA

# 1° Passo, Entrada do Número
numero = int(input("Digite um Número = "))

# Seu Dobro
dobro = numero * 2

# Seu Triplo
triplo = numero * 3

# Raiz Quadrada
raiz_quadrada = numero ** (1/2)

print("O dobro de {} vale = {}".format(numero, dobro))

print("O triplo de {} vale = {}".format(numero, triplo))

print("A raiz quadrada de {} e  = {:.2f}".format(numero,  raiz_quadrada))
