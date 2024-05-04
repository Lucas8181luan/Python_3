from datetime import date
atual = date.today().year

cont_menor = 0
cont_maior = 0

for pessoas in range(1, 8):

    nascimento = int(input("Em que ano a {}º pessoa nasceu = ".format(pessoas)))

    soma_idade = atual - nascimento

    if soma_idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print("Ao todo tivemos {} pessoas MAIOR de idade\nE {} pessoas MENOR de idade".format(cont_maior, cont_menor))
