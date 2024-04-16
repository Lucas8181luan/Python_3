# 1 ()
# **
# * / // %
# + -

# COMO CALCULAR CATETO E HIPOTENUSA

# Importa a math
import math

# Entrada, do cateto oposto, e o cateto adjacente
oposto = float(input("Comprimento do cateto oposto = "))

adjacente = float(input("Comprimento do cateto adjacente = "))

# Soma, usando a biblioteca math
soma = math.hypot(oposto, adjacente)

print("A hipotenusa vai medir {:.2F}".format(soma))
