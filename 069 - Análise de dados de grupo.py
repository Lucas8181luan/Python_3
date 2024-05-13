print("-" * 20)
print("CADASTRE UMA PESSOA")

cont_idade = cont_sexo =  cont_mulheres = 0

while True:
    print("-" * 20)
    idade = int(input("Idade = "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F] = ")).upper().strip()[0]
    print("-" * 20)
    continuar = ' ' 
    while continuar not in "SN":
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]

    if idade >= 18:
        cont_idade += 1

    if sexo == "M":
        cont_sexo += 1
    
    if sexo == "F" and idade < 20:
        cont_mulheres += 1
    
    if continuar == "N":
        break

print(f'''-> Total de pessoas com mais de 18 anos = {cont_idade}\n-> Ao todo temos {cont_sexo} homens cadastrados\n-> E temos {cont_mulheres} mulheres com menos de 20 anos''')
print("-=-" * 20)
print("FIM!")
