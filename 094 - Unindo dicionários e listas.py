import copy

pessoas = {}
lista_pessoas = []
mulheres = []
idades_acima = []
idades = 0

while True:
    nome = str(input("Nome = "))
    pessoas["nome"] = nome

    while True:
        sexo = str(input("Sexo [M/F] = ")).upper().strip()[0]

        if sexo not in 'MF':
            print("ERRO! Por favor, digite apenas M ou F.")
        else:
            pessoas["sexo"] = sexo
            break
    
    idade = int(input("Idade = "))
    pessoas["idade"] = idade
    
    copia_D = copy.deepcopy(pessoas)
    lista_pessoas.append(copia_D)

    while True:
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]

        if continuar not in "SN":
            print("ERRO! Responda apenas S ou N.")
        else:
            break
    
    if continuar == "N":
        break

print("=" * 40)

total_pessoas = len(lista_pessoas)

print(f"A) Ao todo temos {total_pessoas} pessoas cadastradas.")

for i in lista_pessoas:
    idades += i["idade"]
media_idade = idades / total_pessoas
print(f"B) A média de ídade é de {media_idade:.2f} anos.")

for i in lista_pessoas:
    sexos = (i["sexo"])
    if sexos == "F":
        mulheres.append(i["nome"])
print("C) As mulheres cadastradas foram = ",end="")
for i in mulheres:
    print(f"{i}, ",end="")

print()

print("D) Lista das pessoas que estão acima da média:")

for i in lista_pessoas:
    if i["idade"] >= media_idade:
        idades_acima.append(i)
        print(f"   Nome = {i["nome"]}; Sexo = {i["sexo"]}; idade = {i["idade"]}; ")

print("<< ENCERRADO >>")
