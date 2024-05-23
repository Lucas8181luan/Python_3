lista = []

while True:
    usuario = int(input("Digite um valor = "))
    lista.append(usuario)
    continuar = ' '
    while continuar not in "NS":
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]

    if continuar == "N":
        break

lista.sort(reverse=True)
print("-=" * 30)
print(f"Você digitou {len(lista)} elementos")
print(f"Os valores em ordem decrescente são = {lista}")
if 5 not in lista:
    cinco = print("O valor 5 não foi encontrado na lista!")
else:
    cinco = print("O valor 5 faz parte da lista!")
