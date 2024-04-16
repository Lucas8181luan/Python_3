# 1 ()
# **
# * / // %
# + -

# COMO CALCULAR O SENO, COSSENO E O TANGENTE

# Import math
import math

# Entrada, do ângulo desejado
angulo = float(input("Digite o ângulo você deseja = "))

# Convertendo para radianos e somando
soma_seno = math.sin(math.radians(angulo))
soma_cosseno = math.cos(math.radians(angulo))
soma_tangente = math.tan(math.radians(angulo))

print("O ângulo de {} tem o SENO = {:.2f}\nO ângulo de {} tem o COSSENO = {:.2f}\nO ângulo de {} tem o TANGENTE = {:.2f}".format(angulo, soma_seno, angulo, soma_cosseno, angulo, soma_tangente))


