s = 0
quantos_numeros = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        s += soma
        quantos_numeros += 1
print("A soma de todos os {} valores é {}".format(quantos_numeros, s))
    