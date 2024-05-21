import time

lista = []

valor = int(input("Digite um valor = "))

lista.append(valor)

time.sleep(0.5)

print("Valor adicionado com sucesso...")

while True:

    continuar =' '
    while continuar not in "SN":
        continuar = str(input("Quer continuar = ")).strip().upper()[0]
    
    if continuar == "S":
        valor = int(input("Digite um valor = "))

        if valor == valor in lista:
            print("Valor duplicado! Não vou adicionar...")
        else:
            lista.append(valor)
            time.sleep(0.5)
            print("Valor adicionado com sucesso...")

    if continuar == "N":
        break

print("-=" * 30)
print(f"Você digitou os valores = {sorted(lista)}")
