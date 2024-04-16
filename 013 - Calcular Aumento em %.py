# 1 ()
# **
# * / // %
# + -

# CALCULAR AUMENTO EM %

# 1° Passo, preço do produto
produto = float(input("Digite o preço do produto = "))

# 2° Passo, realize a soma
# user a porcentagem que desejar, aqui vou usar 20
soma_1 = (20 / 100)
soma_2 = soma_1 * produto
soma_final = soma_2 + produto

print("O produto custava R${:.2f}, agora com o aumento de 20% vai custar R${:.2f}".format(produto, soma_final))
