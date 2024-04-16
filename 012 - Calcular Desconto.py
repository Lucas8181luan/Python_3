# 1 ()
# **
# * / // %
# + -

# CALCULAR DESCONTO EM %

# 1° Passo, preço do produto
produto = float(input("Digite o preço do produto = "))

# 2° Passo, realize a soma
# user a porcentagem que desejar, aqui vou usar 8
soma_1 = (8 / 100)
soma_2 = soma_1 * produto
soma_final = soma_2 - produto

print("O produto custava R${:.2f}, agora com o desconto de 8% vai custar R${:.2f}".format(produto, soma_final))