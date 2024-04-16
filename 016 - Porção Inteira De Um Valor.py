# 1 ()
# **
# * / // %
# + -

# COMO DESCOBRIR A PORÇÃO INTEIRA DO NÚMERO

# Import a biblioteca math
import math

# Entrada, do numero
numero = float(input("Digite um valor = "))

# Realize a soma usando a biblioteca importada
soma = math.trunc(numero)

print("O valor e {} então sua porção inteira é = {:.0f}".format(numero, soma))