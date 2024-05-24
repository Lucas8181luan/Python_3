lista = []
par = []
ímpar = []

while True:
    valor = int(input("Digite um número = "))
    lista.append(valor)
    continuar = ' '
    while continuar not in "NS":
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]

    if continuar == "N":
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        ímpar.append(i)

print("-=" * 30)
print(f"A lista completa é = {lista}")
print(f"A lista de pares é = {par}")
print(f"A lista de ímpares é = {ímpar}")
