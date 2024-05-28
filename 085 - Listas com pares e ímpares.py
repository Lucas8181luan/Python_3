lista = [[], []]

for i in range(1, 8):
    valor = int(input(f"Digite o {i}º valor = "))
    if valor % 2 == 0:
        par = lista[0]
        par.append(valor)       
    else:
        impar = lista[1]
        impar.append(valor)
# Para par [0]
# Para ímpar [1]
print(f"Os valores pares digitados foram = {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram = {sorted(lista[1])}")
