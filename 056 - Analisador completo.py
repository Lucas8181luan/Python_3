idades= []
cont_idade = 0
nome_mais_velho = ''
cont_mulher = 0
for dados in range(1, 5):
    print("------ {}º PESSOA ------".format(dados))
    
    nome = str(input("Nome = ")).strip()
    
    idade = int(input("Idade = "))
    idades.append(idade)

    sexo = str(input("[M/F] = ")).upper()

    cont_idade += idade 
    soma_idade = cont_idade / dados

    idade_maxima = max(idades)
    
    if dados == 1 and sexo in "Mm":
        nome_mais_velho = nome
    
    if sexo in "Mm":
        nome_mais_velho = nome
    
    if sexo in "Mm" and idade < 20:
        cont_mulher += 1

print("A média de idade do grupo é de {} anos".format(soma_idade))

print("O homen mais velho tem {} anos e se chama {}".format(idade_maxima, nome_mais_velho))

print("Ao todo são {} mulheres com menos de 20 anos".format(cont_mulher))
