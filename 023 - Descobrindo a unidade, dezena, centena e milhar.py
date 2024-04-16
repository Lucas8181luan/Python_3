# COMO DESCOBRIR A UNIDADE, DEZENA, CENTENA E MILHAR DE UM NÚMERO

# Entrada do número
numero = int(input("Digite um valor = "))

# Somando
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("Unidade = {}\nDezena = {} \nCentena = {}\n Milhar = {}".format(unidade, dezena, centena, milhar))


