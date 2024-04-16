# 1 ()
# **
# * / // %
# + -

# UM PROGRAMA QUE LEIA UM VALOR EM METROS E CONVERTA EM CENTÍMETROS E MILÍMETROS

# 1° Passo, Entrada do valor em metros
medida = float(input("Uma Distância em Metros = "))

# Soma em Centimetros
centimetros = medida * 100

# Soma em Milímetros
milimetros = medida * 1000

print("A meidida de {:.2f} metros corresponde a {:.2f}cm e {:.2f}mm".format(medida, centimetros, milimetros))
