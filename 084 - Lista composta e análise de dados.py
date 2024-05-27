lista = []
pessoas = []
maior = menor = 0

while True:

    pessoas.append(str(input("Nome = ")))
    pessoas.append(float(input("Peso = ")))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    lista.append(pessoas[:])
    pessoas.clear()
        
    continuar = ' ' 
    while continuar not in "NS":
        continuar = str(input("Quer continuar [S/N] = ")).strip().upper()[0]

    if continuar == "N":
        break

print("-=" * 30)
print(f"Ao todo, você cadastrou {len(lista)} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de ", end=" ")
for p in lista:
    if p[1] == maior :
        print(f"[{p[0]}]", end=" ")

print()

print(f"O menor peso foi de {menor}kg. Peso de ", end=" ")
for p in lista:
    if p[1] == menor:
       print(f"[{p[0]}]", end=" ")
print()
