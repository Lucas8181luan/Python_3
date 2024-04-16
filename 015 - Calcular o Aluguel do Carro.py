# 1 ()
# **
# * / // %
# + -

# {:.2f}
# soma = (nota_1 + nota_2) / 2

# CALCULAR O ALUGUEL DO CARRO
# A DIARIA CUSTA R$70 POR DIA
# E R$ 0,17 por km rodado

# 1°Passo, quantidades de dias alugado e quantidade de km percorrido
dias = int(input("Quantos dias alugados? "))
km = int(input("Quanto km rodados? "))

# Faça soma
custo_por_dia = 70
quilometragem = 0.17
soma_1 = (custo_por_dia * dias) 
soma_2 = (quilometragem * km)
soma_final = soma_1 + soma_2

print("O total a pagar é de R${:.2f}".format(soma_final))