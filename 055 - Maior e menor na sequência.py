maior = 0
menor = 0
for balança in range(1, 6):
    peso = float(input("Peso da {}º pessoa = ".format(balança)))

    if balança == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print("O maior peso foi = {}kg".format(maior))
print("O menor peso foi = {}kg".format(menor))
