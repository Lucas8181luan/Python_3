maior = menro = 0

lista = []

for i in range(0,5):
    valor = int(input(f"Digite um valor para a posição {i} = "))

    lista.append(valor)

print("-=" * 30)

maior = max(lista)
menor = min(lista)

print(f"Você digitou os valores = {lista}")

print(f"O maior valor digitado foi {max(lista)} nas posições = ",end=" ")

for i, v in enumerate(lista):
    if v == maior:
       print(f"{i}... ",end=" ")

print()

print(f"O menor valor digitado foi {min(lista)} nas posições = ",end=" ")

for i, v in enumerate(lista):
    if v == menor:
       print(f"{i}... ",end=" ")
